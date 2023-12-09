from collections import Counter


class CamelCards :
    def __init__(self) :
        pass

    def modify_hand(self, hand, is_modified) :
        # Modify the hand based on the given rules
        hand = hand.replace('T', chr(ord('9') + 1))
        hand = hand.replace('J', chr(ord('2') - 1) if is_modified else chr(ord('9') + 2))
        hand = hand.replace('Q', chr(ord('9') + 3))
        hand = hand.replace('K', chr(ord('9') + 4))
        hand = hand.replace('A', chr(ord('9') + 5))
        return hand

    def calculate_strength(self, hand, is_modified) :
        # Calculate the strength of the hand based on the modified rules
        modified_hand = self.modify_hand(hand, is_modified)
        counter = Counter(modified_hand)

        if is_modified :
            target = list(counter.keys())[0]
            for k in counter :
                if k != '1' :
                    if counter[k] > counter[target] or target == '1' :
                        target = k
            assert target != '1' or list(counter.keys()) == ['1']
            if '1' in counter and target != '1' :
                counter[target] += counter['1']
                del counter['1']
            assert '1' not in counter or list(counter.keys()) == ['1'], f'{counter} {hand}'

        if sorted(counter.values()) == [5] :
            return 10, modified_hand
        elif sorted(counter.values()) == [1, 4] :
            return 9, modified_hand
        elif sorted(counter.values()) == [2, 3] :
            return 8, modified_hand
        elif sorted(counter.values()) == [1, 1, 3] :
            return 7, modified_hand
        elif sorted(counter.values()) == [1, 2, 2] :
            return 6, modified_hand
        elif sorted(counter.values()) == [1, 1, 1, 2] :
            return 5, modified_hand
        elif sorted(counter.values()) == [1, 1, 1, 1, 1] :
            return 4, modified_hand
        else :
            assert False, f'{counter} {hand} {sorted(counter.values())}'

    def calculate_winnings(self, hands_and_bids, is_modified) :
        # Calculate the total winnings based on the hand strength
        hands_and_bids_sorted = sorted(hands_and_bids, key=lambda hb : self.calculate_strength(hb[0], is_modified))
        total_winnings = 0
        for i, (hand, bid) in enumerate(hands_and_bids_sorted) :
            total_winnings += (i + 1) * int(bid)
        return total_winnings


if __name__ == "__main__" :
    try :
        with open('../../input/day7/input.txt', "r") as file :
            hands_and_bids_input = [tuple(line.split()) for line in file]

        poker_game = CamelCards()

        # Use is_modified=False for the original logic and is_modified=True for the modified logic
        total_winnings_result = poker_game.calculate_winnings(hands_and_bids_input, is_modified=True)
        print(f"The total winnings: {total_winnings_result}")

    except FileNotFoundError :
        print("File not found. Please check the file path.")
    except Exception as e :
        print(f"An error occurred: {e}")
