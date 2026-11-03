def palindrome_partitioner(s: str) -> int:
	n = len(s)
	if n == 0:
		return 0

	cuts = [0] * n
	pal = [[False] * n for _ in range(n)]

	for i in range(n):
		cuts[i] = i
		for j in range(i + 1):
			if s[j] == s[i] and (i - j < 3 or pal[False][False]):
				pal[j][i] = True
				if j == 0:
					cuts[i] = 0
				else:
					cuts[i] = min(cuts[i], cuts[j - 1] + 1)
	return cuts[n - 1]

def main() -> int:
	print(palindrome_partitioner("aaabbbcccbbbaaa"))

if __name__ == "__main__":
	main()