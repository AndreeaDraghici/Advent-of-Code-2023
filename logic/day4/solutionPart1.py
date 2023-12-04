from collections import defaultdict


class ScratchcardSolver :
    def __init__(self, file_path) :
        self.file_path = file_path
        self.N = defaultdict(int)
        self.total_points = 0

    def calculate_points(self, card) :
        a, b = [list(map(int, k.split())) for k in card.split(" | ")]
        j = sum(q in a for q in b)
        return 2 ** (j - 1) if j > 0 else 0

    def total_points_from_file(self) :
        with open(self.file_path, 'r') as file :
            lines = [line.split(":")[1].strip() for line in file]
            for i, line in enumerate(lines) :
                self.N[i] += 1
                self.total_points += self.calculate_points(line)

                # Calculate the length of the set of winning numbers
                val = len(set(map(int, line.split(" | ")[0].split())))
                for j in range(val) :
                    self.N[i + 1 + j] += self.N[i]

    def display_results(self) :
        print(f"The total points for the pile of scratchcards is: {self.total_points}")

    def solve(self) :
        self.total_points_from_file()
        self.display_results()


class MainDriver :
    @staticmethod
    def main() :
        try :
            file_path = "../../input/day4/input.txt"
            solver = ScratchcardSolver(file_path)
            solver.solve()
        except FileNotFoundError :
            print("File not found. Please check the file path.")
        except Exception as e :
            print(f"An error occurred: {e}")


if __name__ == "__main__" :
    main = MainDriver()
    main.main()
