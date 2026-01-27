# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NFL Elo rating calculator that processes historical game data from nflverse, computes team ratings, and generates predictions for upcoming games. Updated weekly via GitHub Actions.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run the Elo calculations (fetches data, processes games, outputs CSV and Markdown)
python nfl_elo.py
```

## Architecture

**Two-file design with clear separation:**

- `elo.py` - Generic Elo algorithm class, reusable for any sport. Handles rating calculations, win probabilities, point spreads, and rating updates.
- `nfl_elo.py` - NFL-specific orchestration. Fetches game data, processes seasons sequentially, applies between-season regression, outputs results.

**Data flow:**
1. Fetch games from nflverse CSV
2. Initialize Elo system with all teams at rating 1500
3. Process games chronologically, updating ratings after each completed game
4. For upcoming games (no score), record predictions without updating ratings
5. Between seasons, regress ratings 33% toward mean (1505)
6. Output enriched data to `nfl_latest_elo.csv` and `nfl_elo_table.md`

**Key parameters in `nfl_elo.py`:**
- `K = 22` - Rating volatility
- `HOME_FIELD = 40` - Home field advantage in Elo points

**Elo algorithm details (`elo.py`):**
- Win probability: `1 / (1 + 10^(elo_diff/400))`
- Point spread: `elo_diff / 25`
- Rating change includes score margin: `K * log(score_diff + 1) * forecast_delta`

## Output Files

- `nfl_latest_elo.csv` - All games with pre/post Elo ratings, win probabilities, point spreads
- `nfl_elo_table.md` - Current season games in Markdown table format
