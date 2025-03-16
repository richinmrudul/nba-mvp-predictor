import pandas as pd

# Load player stats and team standings
df_players = pd.read_csv("data/raw/player_stats_2023-24.csv")
df_teams = pd.read_csv("data/raw/team_standings_2023.csv")

# Load MVP winners data
df_mvp = pd.read_csv("data/raw/mvp_winners.csv")

# Ensure all values in 'PLAYER' and 'Player' columns are strings before processing
df_players["PLAYER"] = df_players["PLAYER"].astype(str).str.upper().str.strip()
df_mvp["Player"] = df_mvp["Player"].astype(str).str.upper().str.strip()

# Merge MVP labels
df = df_players.merge(df_mvp[["Player", "Year"]], left_on="PLAYER", right_on="Player", how="left")

# Create MVP column (1 if player won MVP, else 0)
df["MVP"] = df["Year"].notna().astype(int)

# Ensure all values in 'TEAM' and 'Team' columns are strings before processing
df_players["TEAM"] = df_players["TEAM"].astype(str).str.upper().str.strip()
df_teams["Team"] = df_teams["Team"].astype(str).str.upper().str.strip()

# Merge team standings
df = df.merge(df_teams, left_on="TEAM", right_on="Team", how="left")

# Convert 'Wins' to numeric (handle missing values)
df["Wins"] = pd.to_numeric(df["Wins"], errors="coerce").fillna(0)

# Drop unnecessary columns
df.drop(columns=["Year", "Player", "Team"], inplace=True)

# Save the updated dataset
df.to_csv("data/processed/cleaned_data_with_team_wins.csv", index=False)

print("✅ Player stats merged with MVP labels and team wins! Saved to data/processed/cleaned_data_with_team_wins.csv")
