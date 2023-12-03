class EngineSchematicSolver :
    def __init__(self, engine_schematic) :
        # Initialize the solver with the engine schematic and calculate its dimensions
        self.engine_schematic = engine_schematic
        self.width = len(engine_schematic[0])
        self.height = len(engine_schematic)
        self.part_numbers_sum = 0  # Final sum of part numbers

    # Function that returns a list of coordinates of neighbors
    def get_adjacents(self, x, y) :

        coordinates_of_neighbors = []

        for dx in range(-1, 2) :
            for dy in range(-1, 2) :
                if dx == 0 and dy == 0 :
                    continue

                nx = x + dx
                ny = y + dy

                if 0 <= nx < self.width and 0 <= ny < self.height :
                    coordinates_of_neighbors.append((nx, ny))

        return coordinates_of_neighbors

    def find_part_numbers(self) :
        # Iterate through each element in the engine schematic to find part numbers
        for y in range(self.height) :
            x = 0
            while x < self.width :
                if not self.engine_schematic[y][x].isdigit() :
                    x += 1
                    continue

                checks = self.get_adjacents(x, y)
                num = self.engine_schematic[y][x]

                for i in range(x + 1, self.width) :
                    if not self.engine_schematic[y][i].isdigit() :
                        break

                    num += self.engine_schematic[y][i]
                    checks.extend(self.get_adjacents(i, y))
                    x += 1

                if any(
                        self.engine_schematic[ny][nx] != "." and not self.engine_schematic[ny][nx].isdigit()
                        for nx, ny in checks
                ) :
                    self.part_numbers_sum += int(num)

                x += 1

        return self.part_numbers_sum


class MainDriver :
    @staticmethod
    def main() :
        with open('../../input/day3/input.txt', 'r') as file :
            engine_schematic = [line.strip() for line in file]

        solver = EngineSchematicSolver(engine_schematic)
        result = solver.find_part_numbers()
        print("Sum of part numbers:", result)


if __name__ == "__main__" :
    main = MainDriver()
    main.main()
