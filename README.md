# nfl-elo

Basic NFL Elo calculations using historical results

## Dependencies

This Python program requires the [pandas](https://pandas.pydata.org/)
library and uses NFL game data from
[nflverse](https://github.com/nflverse/nflverse/) GitHub repository.

## Calculating NFL Elo

Running the program downloads the historical and upcoming data from
`nflverse`, computes the before and after Elo for the historic data
and the projected Elo for upcoming games, and writes out a summary
data file called [`nfl_latest_elo.csv`](nfl_latest_elo.csv).

```
python nfl_elo.py
```

It also creates the [`nfl_elo_table.md`](nfl_elo_table.md) for looking
at the current season calculations.

## Weekly Updates

This repository is configured with a [GitHub
Action](.github/workflows/update_elo.yml) on Tuesdays after the week's
games to get the latest data, run the Elo calculations, and save the
output Markdown and CSV files.


