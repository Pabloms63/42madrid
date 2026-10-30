def constellation_mapper(stars: list[tuple[int, int]], dim: int) -> list[str]:
	matrix = [["." for _ in range(dim)] for _ in range(dim)]

	for filas, columnas in stars:
		if 0 <= filas < dim and 0 <= columnas < dim:
			matrix[filas][columnas] = "*"

	return ["".join(fila) for fila in matrix]

def main() -> int:
	print(constellation_mapper([(1, 0), (1, 1), (1, 2)], 3))

if __name__ == "__main__":
	main()