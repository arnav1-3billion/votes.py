import urllib.request
import json
from datetime import datetime

url = "https://games.roblox.com/v1/games/votes?universeIds=6035872082"

with urllib.request.urlopen(url) as response:
    data = json.loads(response.read())

up = data['data'][0]['upVotes']
next_milestone = ((up // 50000) + 1) * 50000
needed = next_milestone - up

entry = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "up_votes": up,
    "next_milestone": next_milestone,
    "votes_needed": needed
}

try:
    with open("votes.json", "r") as f:
        db = json.load(f)
except FileNotFoundError:
    db = []

db.append(entry)

with open("votes.json", "w") as f:
    json.dump(db, f, indent=2)

print(f"Up Votes:       {up:,}")
print(f"Next Milestone: {next_milestone:,}")
print(f"Votes Needed:   {needed:,}")
