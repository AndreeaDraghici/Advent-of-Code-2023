class MazeSolver :
    def __init__(self) :
        pass

    @staticmethod
    def gcd(a, b) :
        """Compute the greatest common divisor using Euclid's algorithm."""
        while b :
            a, b = b, a % b
        return a

    @staticmethod
    def part1(input_lines) :
        """Solve Part 1 of the puzzle."""
        instructions = input_lines[0]
        edges = {}
        # Parse the input and build the graph
        for line in input_lines[2 :] :
            parts = line.split(" ")
            node = parts[0]
            lhs = parts[2][1 :-1]
            rhs = parts[3][0 :-1]
            edges[node] = [lhs, rhs]

        ret = 0
        curr = "AAA"
        # Follow the instructions until reaching 'ZZZ'
        while curr != "ZZZ" :
            go = instructions[ret % len(instructions)]
            idx = 0 if go == 'L' else 1
            curr = edges[curr][idx]
            ret += 1
        return ret

    @staticmethod
    def part2(input_lines) :
        """Solve Part 2 of the puzzle."""
        instructions = input_lines[0]
        edges = {}
        # Parse the input and build the graph
        for line in input_lines[2 :] :
            parts = line.split(" ")
            node = parts[0]
            lhs = parts[2][1 :-1]
            rhs = parts[3][0 :-1]
            edges[node] = [lhs, rhs]

        ret = 1
        # Iterate through nodes ending with 'A' and calculate the cycle length
        for cand in edges.keys() :
            if cand[-1] != 'A' :
                continue
            length = 0
            now = cand
            while now[-1] != 'Z' :
                go = instructions[length % len(instructions)]
                idx = 0 if go == 'L' else 1
                now = edges[now][idx]
                length += 1
            # Calculate the least common multiple of current cycle length and the result so far
            ret = ret // MazeSolver.gcd(ret, length) * length
        return ret

    @staticmethod
    def read_input(filename) :
        """Read the input file and return a list of lines."""
        with open(filename) as f :
            return f.read().strip().split('\n')

    def main(self) :
        try :
            input_of_part1 = self.read_input("../../input/day8/part1/input.txt")
            print(f"Takes : {self.part1(input_of_part1)} steps")

            input_of_part2 = self.read_input("../../input/day8/part2/input.txt")
            print(f"Takes : {self.part2(input_of_part2)} steps before you're only on nodes that end with Z")
        except FileNotFoundError :
            print("File not found. Please check the file path.")
        except Exception as e :
            print(f"An error occurred: {e}")


if __name__ == "__main__" :
    solver = MazeSolver()
    solver.main()