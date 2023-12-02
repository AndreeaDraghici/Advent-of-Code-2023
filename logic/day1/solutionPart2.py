import re


class CalibrationExtractor :
    def __init__(self, file_path, patterns_as_numbers) :
        self.file_path = file_path
        self.patterns_as_numbers = patterns_as_numbers

    def extract_calibration_values(self, lines) :
        total_sum = 0

        for line in lines :
            patterns_that_match_ordered_by_index = []

            for pattern_as_number in self.patterns_as_numbers :
                if pattern_as_number['pattern'] in line :
                    all_matches = re.finditer(pattern_as_number['pattern'], line)
                    for match in all_matches :
                        patterns_that_match_ordered_by_index.append({
                            'index' : match.start(),
                            'pattern' : pattern_as_number['pattern'],
                            'number' : pattern_as_number['number']
                        })

            patterns_that_match_ordered_by_index.sort(key=lambda x : x['index'])

            if patterns_that_match_ordered_by_index :
                first_digit = patterns_that_match_ordered_by_index[0]['number']
                last_digit = patterns_that_match_ordered_by_index[-1]['number']
                combined_digit = first_digit * 10 + last_digit
                total_sum += combined_digit

        return total_sum

    def process_calibration_file(self) :
        try :
            with open(self.file_path, "r") as file :
                calibration_input = [line.strip() for line in file.readlines()]

            result = self.extract_calibration_values(calibration_input)

            print(f"Sum of all calibration values is: {result}")

        except FileNotFoundError :
            print("File not found. Please check the file path.")
        except Exception as e :
            print(f"An error occurred: {e}")


class MainDriver :
    @staticmethod
    def main() :
        # List of patterns and their corresponding numbers
        patterns_as_numbers = [
            {'pattern' : 'one', 'number' : 1},
            {'pattern' : '1', 'number' : 1},
            {'pattern' : 'two', 'number' : 2},
            {'pattern' : '2', 'number' : 2},
            {'pattern' : 'three', 'number' : 3},
            {'pattern' : '3', 'number' : 3},
            {'pattern' : 'four', 'number' : 4},
            {'pattern' : '4', 'number' : 4},
            {'pattern' : 'five', 'number' : 5},
            {'pattern' : '5', 'number' : 5},
            {'pattern' : 'six', 'number' : 6},
            {'pattern' : '6', 'number' : 6},
            {'pattern' : 'seven', 'number' : 7},
            {'pattern' : '7', 'number' : 7},
            {'pattern' : 'eight', 'number' : 8},
            {'pattern' : '8', 'number' : 8},
            {'pattern' : 'nine', 'number' : 9},
            {'pattern' : '9', 'number' : 9},
        ]

        file_path = "../../input/day1/part2/input.txt"

        extractor = CalibrationExtractor(file_path, patterns_as_numbers)
        extractor.process_calibration_file()


if __name__ == "__main__" :
    main = MainDriver()
    main.main()
