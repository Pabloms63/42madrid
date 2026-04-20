import os


class MazeVisualizer:
    def __init__(self, maze_data: list[list]) -> None:
        self.maze = maze_data
        self.show_path = False
        self.wall_color = "\033[1;37m"
        self.reset_color = "\033[0m"
        self.colors = {
            "red": "\033[0;31m",
            "green": "\033[0;32m",
            "blue": "\033[0;34m",
            "yellow": "\033[0;33m",
            "white": "\033[1;37m"
        }

    def draw(self, path_coords=None) -> None:
        if path_coords is None:
            path_coords = set()

        os.system('cls' if os.name == 'nt' else 'clear')
        for r, row in enumerate(self.maze):
            line = ""
            for c, cell in enumerate(row):
                if self.show_path and (r, c) in path_coords:
                    line += "\033[0;33m.\033[0m"
                elif cell == 1:
                    line += f"{self.wall_color}██{self.reset_color}"
                elif cell == 'E':
                    line += "\033[0;32mE\033[0m"
                elif cell == 'S':
                    line += "\033[0;31mS\033[0m"
                else:
                    line += "  "  # IMPORTANTE: Espacio para que no se deforme
            print(line)

    def change_color(self, color_name: str) -> None:
        if color_name in self.colors:
            self.wall_color = self.colors[color_name]

    def create_42_logo(self):
        pass


def main() -> None:
    # Laberinto de prueba
    test_maze = [
        [1, 1, 1, 1, 1, 1, 1],
        ['E', 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 'S'],
        [1, 1, 1, 1, 1, 1, 1],
    ]
    test_path = {(1, 1), (1, 2), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5)}

    maze_viz = MazeVisualizer(test_maze)

    while True:
        maze_viz.draw(test_path)
        print("\n=== A-Maze-Ing ===")
        print("1. Re-generate a new maze")
        print("2. Show/Hide path")
        print("3. Change colors")
        print("4. Quit")

        choice = input("\nChoice? (1-4): ")

        if choice == "1":
            # Aqui vendra backtracking recursivo
            print("Generating...")
        elif choice == "2":
            maze_viz.show_path = not maze_viz.show_path
        elif choice == "3":
            new_color = input("Color (red/green/blue/yellow/white): ").lower()
            maze_viz.change_color(new_color)
        elif choice == "4":
            break


if __name__== "__main__":
    main()
