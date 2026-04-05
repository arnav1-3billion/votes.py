from http.server import BaseHTTPRequestHandler
import urllib.request
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = "https://games.roblox.com/v1/games/votes?universeIds=6035872082"
        
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        up = data['data'][0]['upVotes']
        down = data['data'][0]['downVotes']
        total = up + down
        next_milestone = ((up // 50000) + 1) * 50000
        needed = next_milestone - up
        progress = round((up % 50000) / 50000 * 100, 2)
        like_ratio = round(up / total * 100, 2) if total > 0 else 0

        result = json.dumps({
            "up_votes": up,
            "down_votes": down,
            "total_votes": total,
            "like_ratio": str(like_ratio) + "%",
            "next_milestone": next_milestone,
            "votes_needed": needed,
            "milestone_progress": str(progress) + "%"
        })

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(result.encode())
