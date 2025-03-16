from nba_api.stats.endpoints import LeagueLeaders
import pandas as pd

# Specify the season (format: "YYYY-YY")
SEASON = "2022-2023"

# Fetch league leaders (top 50 players)
league_leaders = LeagueLeaders(season=SEASON, season_type_all_star="Regular Season")
data = league_leaders.get_data_frames()[0]

# Save to CSV
data.to_csv(f"data/raw/player_stats_{SEASON}.csv", index=False)

print(f"✅ Player stats for {SEASON} saved to data/raw/player_stats_{SEASON}.csv")
