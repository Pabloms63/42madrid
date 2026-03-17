if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")
    print("=== List Comprehension Examples ===")
    players = [
        {"name": "alice", "score": 2700, "achievements": ["first_kill", "level_5", "boss_slayer"], "region": "north"},
        {"name": "bob", "score": 1800, "achievements": ["first_kill", "level_3"], "region": "east"},
        {"name": "charlie", "score": 2150, "achievements": ["level_10", "boss_slayer"], "region": "central"},
        {"name": "diana", "score": 2050, "achievements": ["first_kill", "level_7"], "region": "north"},
        {"name": "pablo", "score": 0, "achievements": ["die_without_killing"], "region": None},
    ]
    high_scores = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scores}")
    scores_doubled = [(p["score"] * 2) for p in players]
    print(f"Scores doubled: {scores_doubled}")
    active_players = [p["name"] for p in players if p["score"] > 0]
    print(f"Active players: {active_players}")

    print("\n=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players}
    print(f"Player scores: {player_scores}")
    score_categories = {
        "high": len([p for p in players if p["score"] >= 2500]),
        "medium": len([p for p in players if p["score"] >= 1500 and p["score"] <= 2500]),
        "low": len([p for p in players if p["score"] < 1500])
    }
    print(f"Score categories: {score_categories}")
    achievement_counts = {p["name"]: len(p["achievements"]) for p in players}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")
    unique_achievements = {a for p in players for a in p["achievements"]}
    print(f"Unique achievements: {unique_achievements}")
    active_regions = {p["region"] for p in players if p["region"] != None}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")
    total_players = len(players)
    print(f"Total players: {total_players}")
    total_unique_achievements = len({a for p in players for a in p["achievements"]})
    print(f"Total unique achievements: {total_unique_achievements}")
    total_scores = len(players)
    sum_scores = sum(p["score"] for p in players)
    print(f"Average score: {sum_scores / total_scores}")
    top_player = players[0]
    for p in players:
        if p["score"] > top_player["score"]:
            top_player = p
    print(f"Top performer: {top_player['name']} ({top_player['score']} points, {len(top_player['achievements'])} achievements)")
