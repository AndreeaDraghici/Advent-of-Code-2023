import re


class BoatRaceSolver :
    def __init__(self, race_times, record_distances) :
        """
        Initialize the BoatRaceSolver with race times and record distances.

        Parameters:
        - race_times: List of integers representing race times.
        - record_distances: List of integers representing record distances.
        """
        self.race_times = race_times
        self.record_distances = record_distances

    def calculate_ways_to_beat_record(self) :
        """
        Calculate the total number of ways to beat the record based on race times and distances.

        Returns:
        - int: Total number of ways to beat the record.
        """
        number_of_ways = 1

        def util_helper(race_time, record_distance) :
            """
            Helper function to calculate the ways to beat the record for a single race.

            Parameters:
            - race_time: Race time (milliseconds).
            - record_distance: Record distance (millimeters).

            Returns:
            - int: Ways to beat the record.
            """
            result = 0
            for var in range(race_time + 1) :
                dx = var * (race_time - var)
                if dx >= record_distance :
                    result += 1
            return result

        for i in range(len(self.race_times)) :
            number_of_ways *= util_helper(self.race_times[i], self.record_distances[i])

        return number_of_ways


def read_input_from_file(file_path) :
    """
    Read input from a file and extract race times and record distances.

    Parameters:
    - file_path: Path to the input file.

    Returns:
    - tuple: (List of race times, List of record distances)
    """
    with open(file_path, 'r') as file :
        lines = file.readlines()
        race_times_input = lines[0].strip()
        record_distances_input = lines[1].strip()

    race_times = [int(x) for x in re.findall(r'\d+', race_times_input)]
    record_distances = [int(x) for x in re.findall(r'\d+', record_distances_input)]

    return race_times, record_distances


def main() :
    """
    Main function to read input, solve the boat races problem, and print the result.
    """
    file_path = '../../input/day6/part1/input.txt'
    race_times, record_distances = read_input_from_file(file_path)

    solver = BoatRaceSolver(race_times, record_distances)
    result = solver.calculate_ways_to_beat_record()

    print(f"The total number of ways to beat the records is: {result}")


if __name__ == "__main__" :
    main()
