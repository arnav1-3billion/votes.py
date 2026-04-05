export default async function handler(req, res) {
    const response = await fetch("https://games.roblox.com/v1/games/votes?universeIds=6035872082");
    const data = await response.json();

    const up = data.data[0].upVotes;
    const down = data.data[0].downVotes;
    const total = up + down;
    const next_milestone = (Math.floor(up / 50000) + 1) * 50000;
    const needed = next_milestone - up;
    const progress = ((up % 50000) / 50000 * 100).toFixed(2);
    const like_ratio = (up / total * 100).toFixed(2);

    res.status(200).json({
        up_votes: up,
        down_votes: down,
        total_votes: total,
        like_ratio: like_ratio + "%",
        next_milestone: next_milestone,
        votes_needed: needed,
        milestone_progress: progress + "%"
    });
}
