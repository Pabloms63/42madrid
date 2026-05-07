def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
	for row in matrix:
		row.reverse()
	return matrix

if __name__ == "__main__":
	matrix = [[1, 2, 3], [4, 5, 6]]
	print(mirror_matrix(matrix))
