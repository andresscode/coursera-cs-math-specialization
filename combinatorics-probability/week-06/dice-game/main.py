def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in dice1:
        for j in dice2:
            if i > j:
                dice1_wins = dice1_wins + 1
            elif j > i:
                dice2_wins = dice2_wins + 1

    return dice1_wins, dice2_wins


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)

    wins = [0] * len(dices)
    results = [[0] * len(dices) for _ in range(len(dices))]

    for i in range(len(dices) - 1):
        for j in range(i + 1, len(dices)):
            i_die, j_die = count_wins(dices[i], dices[j])
            if i_die > j_die:
                wins[i] = wins[i] + 1
                results[i][j] = 1
                results[j][i] = -1
            elif j_die > i_die:
                wins[j] = wins[j] + 1
                results[i][j] = -1
                results[j][i] = 1

    for i in range(len(wins)):
        if wins[i] == len(dices) - 1:
            return i, results

    return -1, results


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()

    best, results = find_the_best_dice(dices)

    if best != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = best
    else:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                if results[j][i] == 1:
                    strategy[i] = j

    return strategy


if __name__ == '__main__':
    input = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]
    print(compute_strategy(input))
