from collections import defaultdict


class GameAnalyzer :
    def __init__(self, cube_configuration) :
        self.cube_configuration = cube_configuration

    def is_possible(self, subsets) :
        # Check if the subsets are consistent with the given cube configuration
        count = defaultdict(int)

        for subset in subsets :
            count_str, color = subset
            count_str = int(count_str)
            count[color] = max(count[color], count_str)
            if count_str > self.cube_configuration.get(color, 0) :
                return False

        return True

    def possible_games(self, games) :
        # Initialize variables to store the results
        possible_id = 0
        sum_of_ids = 0

        # Iterate over each game in the input
        for game in games.split('\n') :
            is_possible_game = True
            # Split the game into ID and game data
            id_, game_data = game.split(':')
            subsets = defaultdict(int)

            # Iterate over each event in the game data
            for event in game_data.split(';') :
                # Iterate over each ball in the event
                for balls in event.split(',') :
                    color_configuration, color = balls.split()
                    color_configuration = int(color_configuration)
                    subsets[color] = max(subsets[color], color_configuration)
                    if color_configuration > self.cube_configuration.get(color, 0) :
                        is_possible_game = False

            # Calculate the score for the current game
            score = 1
            for subset in subsets.values() :
                score *= subset
            sum_of_ids += score

            # If the game is possible, add its ID to the total
            if is_possible_game :
                possible_id += int(id_.split()[-1])

        # Return the results
        return possible_id, sum_of_ids


class MainDriver :
    @staticmethod
    def main() :
        try :
            with open("../../input/day2/input.txt", "r") as file :
                games = file.read().strip()

            analyzer = GameAnalyzer({'red' : 12, 'green' : 13, 'blue' : 14})
            possible_id, sum_of_ids = analyzer.possible_games(games)

            print("Possible games:", possible_id)
            print("Sum of IDs of possible games:", sum_of_ids)

        except FileNotFoundError :
            print("File not found. Please check the file path.")
        except Exception as e :
            print(f"An error occurred: {e}")


if __name__ == "__main__" :
    main = MainDriver()
    main.main()
