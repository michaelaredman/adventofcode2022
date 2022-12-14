
def calculate_points(pair: tuple[str, str]) -> int:
    points = 0
    hand_points = {"X": 1, "Y": 2, "Z": 3}
    points += hand_points[pair[1]]
    if ((pair[0] == "A" and pair[1] == "X") or
            (pair[0] == "B" and pair[1] == "Y") or (pair[0] == "C" and pair[1] == "Z")):
        points += 3  # draw
    elif ((pair[0] == "A" and pair[1] == "Y") or
            (pair[0] == "B" and pair[1] == "Z") or (pair[0] == "C" and pair[1] == "X")):
        points += 6  # win
    return points


example = [("A", "Y"), ("B", "X"), ("C", "Z")]

print(sum([calculate_points(x) for x in example]))

with open("inputs/day2", "r") as f:
    hands = [tuple(pair.strip().split()) for pair in f]

total_points = sum(calculate_points(pair) for pair in hands)
print(f"The total number of points for the strategy is {total_points}.")


def explained_score(pair: tuple[str, str]) -> int:
    points = 0
    implied_match_score = {"X": 0, "Y": 3, "Z": 6}
    points += implied_match_score[pair[1]]
    winning_hand_implied_points = {"A": 2, "B": 3, "C": 1}
    drawing_hand_implied_points = {"A": 1, "B": 2, "C": 3}
    losing_hand_implied_points = {"A": 3, "B": 1, "C": 2}
    if pair[1] == "X":
        points += losing_hand_implied_points[pair[0]]
    elif pair[1] == "Y":
        points += drawing_hand_implied_points[pair[0]]
    else:
        points += winning_hand_implied_points[pair[0]]
    return points


print(f"The total score of the decrypted strategy is \
{sum(explained_score(pair) for pair in hands)}.")
