
class SeedFertilizer :
    def __init__(self, function_str) :
        # Parse the string to extract information about the function
        lines = function_str.split('\n')[1 :]  # discard the function name
        # Extract the tuples (dst, src, sz) from each line and add them to the list of tuples
        self.tuples = [[int(x) for x in line.split()] for line in lines]

    def apply_one(self, x: int) -> int :
        # Apply the function for a specific value x
        for (dst, src, sz) in self.tuples :
            if src <= x < src + sz :
                return x + dst - src
        return x

    def apply_range(self, ranges) :
        # Apply the function for a list of ranges
        result = []
        for (destination, src, sz) in self.tuples :
            src_end = src + sz
            new_ranges = []
            while ranges :
                (st, ed) = ranges.pop()
                before = (st, min(ed, src))
                inter = (max(st, src), min(src_end, ed))
                after = (max(src_end, st), ed)
                if before[1] > before[0] :
                    new_ranges.append(before)
                if inter[1] > inter[0] :
                    result.append((inter[0] - src + destination, inter[1] - src + destination))
                if after[1] > after[0] :
                    new_ranges.append(after)
            ranges = new_ranges
        return result + ranges


def main() :
    # Path to the input file
    input_file_path = "../../input/day5/input.txt"

    # Reading the input data from the file
    with open(input_file_path, 'r') as file :
        input_data = file.read()

    # Separating the components from the input
    components = input_data.split('\n\n')
    seeds, *function_data = components

    # Processing the seeds
    seed_values = [int(x) for x in seeds.split(':')[1].split()]

    # Creating Function objects
    functions = [SeedFertilizer(func_data) for func_data in function_data]

    # Part 1: Applying functions to seeds and finding the minimum value
    result_part_1 = []
    for x in seed_values :
        for func in functions :
            x = func.apply_one(x)
        result_part_1.append(x)
    print("Lowest location number for seeds:", min(result_part_1))

    # Part 2: Applying functions to pairs of seeds and finding the minimum value
    seed_pairs = list(zip(seed_values[: :2], seed_values[1 : :2]))
    result_part_2 = []
    for st, sz in seed_pairs :
        intervals = [(st, st + sz)]
        for func in functions :
            intervals = func.apply_range(intervals)
        result_part_2.append(min(intervals)[0])
    print("Lowest location number for seed pairs:", min(result_part_2))


if __name__ == "__main__" :
    main()
