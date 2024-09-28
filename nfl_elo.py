from elo import Elo
import datetime
import pandas as pd
import numpy as np

GAME_CSV_URL = (
    "https://raw.githubusercontent.com/nflverse/"
    "nfldata/master/data/games.csv"
)
OUT_FILE = "nfl_latest_elo.csv"

def main():
    print(f"Reading games from {GAME_CSV_URL}...")
    nfl_games = pd.read_csv(GAME_CSV_URL)
    print(f"Retrieved {len(nfl_games)} games.")
    nfl_teams = set(
        list(nfl_games["home_team"].unique()) +
        list(nfl_games["away_team"].unique())
    )
    print(f"Teams: {nfl_teams}")
    nfl_elo = Elo(teams=nfl_teams)
    games_with_elo = process_game_elo(nfl_elo, nfl_games)
    print(f"Writing games with updated Elo to {OUT_FILE}...")
    games_with_elo.to_csv("nfl_latest_elo.csv", index=False)
    print("Writing Markdown table file...")
    write_markdown_output(games_with_elo)
    print("Done.")

def process_game_elo(elo, games_input, verbose=False):
    # Copy for output
    games = games_input.copy()
    for season in range(1999, 2025):
        print(f"{season} Season...")
        season_games = games[games["season"] == season]
        for ix, game in season_games.iterrows():
            if pd.isna(game["home_score"]):
                # Predict upcoming game, rather than update model
                home_team = game["home_team"]
                away_team = game["away_team"]
                away_elo = elo.team_rating(away_team)
                home_elo = elo.team_rating(home_team)
                home_win_prob = elo.home_win_prob(home_team, away_team)
                away_win_prob = 1 - home_win_prob
                point_spread = elo.point_spread(home_team, away_team)
                if verbose:
                    print(f"{game.season}, week {game.week}: "
                          f"{away_team} ({away_elo:.0f} - {away_win_prob:.0%}) "
                          f"{point_spread:.0f} at {home_team} ({home_elo:.0f} "
                          f"- {home_win_prob:.0%})")
                # Update model with game predictions
                games.at[ix, "home_elo"] = home_elo
                games.at[ix, "away_elo"] = away_elo
                games.at[ix, "home_win_prob"] = home_win_prob
                games.at[ix, "away_win_prob"] = away_win_prob
                games.at[ix, "point_spread"] = point_spread
            else:
                # Update model with games results
                home_team = game["home_team"]
                away_team = game["away_team"]
                away_elo = elo.team_rating(away_team)
                home_elo = elo.team_rating(home_team)
                home_win_prob = elo.home_win_prob(home_team, away_team)
                away_win_prob = 1 - home_win_prob
                point_spread = elo.point_spread(home_team, away_team)
                home_elo, away_elo, home_elo_post, away_elo_post = update_elo(elo, game)
                if verbose:
                    print(f"{game.season}, week {game.week}: "
                          f"{game.away_team} ({away_elo:.0f}-{away_elo_post:.0f}) "
                          f"{game.away_score:.0f} at {game.home_team} ({home_elo:.0f} "
                          f"- {home_elo_post:.0f}) {game.home_score:.0f}")
                # Update row with Elo values
                games.at[ix, "home_elo"] = home_elo
                games.at[ix, "away_elo"] = away_elo
                games.at[ix, "home_elo_post"] = home_elo_post
                games.at[ix, "away_elo_post"] = away_elo_post
                games.at[ix, "home_win_prob"] = home_win_prob
                games.at[ix, "away_win_prob"] = away_win_prob
                games.at[ix, "point_spread"] = point_spread
        print(f"End of season {season}")
        if season != 2024:
            print("Regressing towards the mean between seasons...")
            elo.regress_towards_mean()
    return games
            
def update_elo(elo, game):
    home_team = game["home_team"]
    away_team = game["away_team"]
    pre_home = elo.team_rating(home_team)
    pre_away = elo.team_rating(away_team)
    elo.update_ratings(
        home_team,
        game["home_score"],
        away_team,
        game["away_score"],
    )
    post_home = elo.team_rating(home_team)
    post_away = elo.team_rating(away_team)
    return (
        pre_home,
        pre_away,
        post_home,
        post_away,
    )

def write_markdown_output(games):
    games_tbl = (games
                 .query("season == 2024")
                 .assign(actual_spread = lambda x: (x["away_score"] -
                                                    x["home_score"]))
                 .fillna(np.nan)
                 .replace([np.nan], None)
                 .filter(items=["week",
                                "away_team",
                                "away_elo",
                                "away_win_prob",
                                "away_score",
                                "home_team",
                                "home_elo",
                                "home_win_prob",
                                "home_score",
                                "point_spread",
                                "actual_spread"]))
    time_update_str = datetime.datetime.now().ctime()
    with open("nfl_elo_table.md", "w") as out_file:
        out_file.write("## NFL Elo\n\n")
        out_file.write(f"*Updated {time_update_str}\n\n")
        out_file.write(games_tbl.to_markdown(
            index=False,
            tablefmt="pipe",
            floatfmt=[".0f", "", ".0f", ".0%", ".0f", "", ".0f", ".0%", ".0f", ".0f", ".0f"],
            missingval="",
        ))


if __name__ == "__main__":
    main()
