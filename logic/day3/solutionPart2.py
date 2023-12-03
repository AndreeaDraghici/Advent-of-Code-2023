from collections import defaultdict


class GearRatioSolver :
    def __init__(self, engine_schematic) :
        # Initialize the solver with the engine schematic and calculate its dimensions
        self.engine_schematic = engine_schematic
        self.width = len(engine_schematic[0])
        self.height = len(engine_schematic)
        self.gear_ratios_sum = 0  # Final sum of gear ratios
        self.d = defaultdict(list)  # Dictionary to store found gear ratios

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

    def find_gear_ratios(self) :
        # Iterate through each element in the engine schematic to find gear ratios
        for y in range(self.height) :
            x = 0
            while x < self.width :
                if not self.engine_schematic[y][x].isdigit() :
                    x += 1
                    continue

                checks = self.get_adjacents(x, y)
                num = int(self.engine_schematic[y][x])

                for i in range(x + 1, self.width) :
                    if not self.engine_schematic[y][i].isdigit() :
                        break

                    num = num * 10 + int(self.engine_schematic[y][i])
                    checks.extend(self.get_adjacents(i, y))
                    x += 1

                for nx, ny in checks :
                    if self.engine_schematic[ny][nx] == "*" :
                        self.d[(nx, ny)].append(num)
                        break

                x += 1

        # Calculate the final sum of gear ratios
        for nums in self.d.values() :
            if len(nums) > 1 :
                result = 1
                for num in nums :
                    result *= num
                self.gear_ratios_sum += result

        return self.gear_ratios_sum


class MainDriver :
    @staticmethod
    def main() :
        with open('../../input/day3/input.txt', 'r') as file :
            engine_schematic = [line.strip() for line in file]

        solver = GearRatioSolver(engine_schematic)
        result = solver.find_gear_ratios()
        print("Sum of gear ratios:", result)


if __name__ == "__main__" :
    main = MainDriver()
    main.main()
