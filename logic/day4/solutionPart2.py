from collections import defaultdict


class ScratchcardSolver :
    def __init__(self, file_path) :
        self.file_path = file_path
        self.m = defaultdict(int)

    def calculate_copies(self, card) :
        a, b = [list(map(int, k.split())) for k in card.split(" | ")]
        j = sum(q in a for q in b)
        return j

    def total_scratchcards_from_file(self) :
        with open(self.file_path, 'r') as file :
            for i, line in enumerate(file) :
                if i not in self.m :
                    self.m[i] = 1

                copies = self.calculate_copies(line.split(":")[1].strip())

                for n in range(i + 1, i + copies + 1) :
                    self.m[n] = self.m.get(n, 1) + self.m[i]

    def display_results(self) :
        print(f"The total number of scratchcards is: {sum(self.m.values())}")

    def solve(self) :
        self.total_scratchcards_from_file()
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
