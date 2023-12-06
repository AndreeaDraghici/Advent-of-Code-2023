class BoatRaceSolver :
    def __init__(self, race_time, record_distance) :
        """
        Initialize the BoatRaceSolver with a single race time and record distance.

        Parameters:
        - race_time: Integer representing race time.
        - record_distance: Integer representing record distance.
        """
        self.race_time = race_time
        self.record_distance = record_distance

    def calculate_ways_to_beat_record(self) :
        """
        Calculate the total number of ways to beat the record for a single race.

        Returns:
        - int: Total number of ways to beat the record.
        """
        total_ways = 0

        # Iterate through possible holding times (from 14 to race_time - 14)
        for holding_time in range(14, self.race_time - 14) :
            distance_covered = holding_time * (self.race_time - holding_time)

            # Check if the distance covered is greater than or equal to the record distance
            if distance_covered >= self.record_distance :
                total_ways += 1

        return total_ways


def read_input_from_file(file_path) :
    """
    Read input from a file and extract a single race time and record distance.

    Parameters:
    - file_path: Path to the input file.

    Returns:
    - tuple: (Race time, Record distance)
    """
    with open(file_path, 'r') as file :
        lines = file.readlines()
        # Ignore spaces and join the numbers into a single string
        race_time_input = ''.join(lines[0].strip().split()[1 :])
        record_distance_input = ''.join(lines[1].strip().split()[1 :])

    race_time = int(race_time_input)
    record_distance = int(record_distance_input)

    return race_time, record_distance


def main() :
    """
    Main function to read input, solve the boat race problem, and print the result.
    """
    file_path = '../../input/day6/part2/input.txt'
    race_time, record_distance = read_input_from_file(file_path)

    solver = BoatRaceSolver(race_time, record_distance)
    result = solver.calculate_ways_to_beat_record()

    print(f"The total number of ways to beat the record in this single race is: {result}")


if __name__ == "__main__" :
    main()
