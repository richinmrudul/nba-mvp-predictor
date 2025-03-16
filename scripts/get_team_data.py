import pandas as pd
import requests
from bs4 import BeautifulSoup

# NBA Team Standings URL (Update year as needed)
year = "2023"
url = f"https://www.basketball-reference.com/leagues/NBA_{year}_standings.html"

# Request and parse page
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract standings table
tables = soup.find_all("table")
standings_table = tables[0]  # First table is usually the standings

# Convert table to DataFrame
team_data = []
for row in standings_table.find_all("tr")[1:]:  
    cols = row.find_all("td")
    if cols:
        team = cols[0].text.strip()
        wins = cols[1].text.strip()
        team_data.append([team, wins])

df_teams = pd.DataFrame(team_data, columns=["Team", "Wins"])

# Save to CSV
df_teams.to_csv(f"data/raw/team_standings_{year}.csv", index=False)
print(f"✅ Team standings for {year} saved!")
