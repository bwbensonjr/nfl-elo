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
data file called [`nfl_latest_elo.csv`](nfl_latest_elo.csv)

```
python nfl_elo.py
```
