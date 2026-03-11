import sys

print("=== Player Score Analytics ===")

if len(sys.argv) > 2:
	scores = []

	for score in sys.argv[1:]:
		scores.append(int(score))
	print(f"Total players: {len(scores)}")
	print(f"Total score: {sum(scores)}")
	print(f"Average score: {sum(scores) / len(scores)}")
	print(f"High score: {max(scores)}")
	print(f"High score: {min(scores)}")
	print(f"Score range: {max(scores) - min(scores)}")
else:
	print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")