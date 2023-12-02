import re

def extract_calibration_values(lines, patterns_as_numbers=None):
    # Initialize the total sum to 0
    total_sum = 0

    # Iterate over each line in the input
    for line in lines:
        # List to store patterns that match, ordered by their index in the line
        patterns_that_match_ordered_by_index = []

        # Iterate over each pattern in patterns_as_numbers
        for pattern_as_number in patterns_as_numbers:
            # Check if the pattern is present in the line
            if pattern_as_number['pattern'] in line:
                # Find all matches of the pattern in the line
                all_matches = re.finditer(pattern_as_number['pattern'], line)
                for match in all_matches:
                    # Add the match details to the list
                    patterns_that_match_ordered_by_index.append({
                        'index': match.start(),
                        'pattern': pattern_as_number['pattern'],
                        'number': pattern_as_number['number']
                    })

        # Sort the list based on the index of matches
        patterns_that_match_ordered_by_index.sort(key=lambda x: x['index'])

        # Extract the first and last digits based on the matches
        first_digit = patterns_that_match_ordered_by_index[0]['number']
        last_digit = patterns_that_match_ordered_by_index[-1]['number']

        # Calculate the combined digit and add it to the total sum
        combined_digit = first_digit * 10 + last_digit
        total_sum += combined_digit

    # Return the final sum
    return total_sum


if __name__ == "__main__":
    # List of patterns and their corresponding numbers
    patterns_as_numbers = [
        {'pattern': 'one', 'number': 1},
        {'pattern': '1', 'number': 1},
        {'pattern': 'two', 'number': 2},
        {'pattern': '2', 'number': 2},
        {'pattern': 'three', 'number': 3},
        {'pattern': '3', 'number': 3},
        {'pattern': 'four', 'number': 4},
        {'pattern': '4', 'number': 4},
        {'pattern': 'five', 'number': 5},
        {'pattern': '5', 'number': 5},
        {'pattern': 'six', 'number': 6},
        {'pattern': '6', 'number': 6},
        {'pattern': 'seven', 'number': 7},
        {'pattern': '7', 'number': 7},
        {'pattern': 'eight', 'number': 8},
        {'pattern': '8', 'number': 8},
        {'pattern': 'nine', 'number': 9},
        {'pattern': '9', 'number': 9},
    ]

    try:
        # Read input from file and strip newline characters
        with open("../../input/day1/part2/input.txt", "r") as file:
            calibration_input = [line.strip() for line in file.readlines()]

        # Calculate the sum of all calibration values
        result = extract_calibration_values(calibration_input, patterns_as_numbers)

        # Print the result
        print(f"Sum of all of the calibration values is: {result}")

    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")
