import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of MVP winners on Basketball-Reference
url = "https://www.basketball-reference.com/awards/mvp.html"

# Add headers to mimic a real browser
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Parse the page
soup = BeautifulSoup(response.text, "html.parser")

# Find the correct table (Table 1)
table = soup.find("table", {"id": "mvp_NBA"})

# Check if the table was found
if table is None:
    print("Error: Could not find the MVP table. The website structure may have changed.")
    exit()

# Extract table rows
data = []
for row in table.find_all("tr")[1:]:  # Skip the header row
    cols = row.find_all("td")
    if cols:
        year = cols[0].text.strip()  # Season
        player = cols[1].text.strip()  # Player Name
        team = cols[2].text.strip() if len(cols) > 2 else "N/A"  # Team (if available)
        data.append([year, player, team])

# Convert to DataFrame
df = pd.DataFrame(data, columns=["Year", "Player", "Team"])

# Save to CSV
df.to_csv("data/raw/mvp_winners.csv", index=False)

print("✅ MVP data saved to data/raw/mvp_winners.csv")
