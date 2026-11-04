def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
	if not packages:
		return []

	pendientes = {}
	dependientes = {}
	
	for pendiente in packages:
		pendientes.setdefault(pendiente, 0)
		dependientes.setdefault(pendiente, [])

	for paquete, dependencias in packages.items():
		for dependencia in dependencias:
			if not dependencia in packages.keys():
				continue
			pendientes[paquete] += 1
			dependientes[dependencia].append(paquete)

	cola = []
	for paquete, num in pendientes.items():
		if num == 0:
			cola.append(paquete)
	cola = sorted(cola)

	resultado = []
	while cola:
		actual = cola.pop(0)
		resultado.append(actual)
		for siguiente in dependientes[actual]:
			pendientes[siguiente] -= 1
			if pendientes[siguiente] == 0:
				cola.append(siguiente)

	if len(packages) == len(resultado):
		return resultado

	return []

def main() -> int:
	print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))

if __name__ == "__main__":
	main()
