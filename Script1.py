import random

def print_score(score, player_names, serving_player):
    score_names = ['0', '15', '30', '40', 'Adv.']
    if score[0] == score[1] == 3:
        print("Deuce")
    elif score[0] >= 4 and score[1] >= 3 and score[0] - score[1] == 1:
        print(f"Adv - {score_names[score[1]]}")
    elif score[1] >= 4 and score[0] >= 3 and score[1] - score[0] == 1:
        print(f"{score_names[score[0]]} - Adv")
    elif max(score) >= 4 and abs(score[0] - score[1]) >= 2:
        leading_player = player_names[0] if score[0] > score[1] else player_names[1]
        print(f"{leading_player} wins the game!")
        return leading_player
    else:
        print(f"{score_names[score[0]]}-{score_names[score[1]]} ({serving_player} serving)")

def play_game(player_names, serving_player):
    score = [0, 0]
    while True:
        try:
            player = input(f"Enter name of player who scored the point ({player_names[0]} or {player_names[1]}): ")
        except ValueError:
            print("Invalid input.")
            continue

        if player not in player_names:
            print("Invalid input.")
            continue

        score[player_names.index(player)] += 1

        if max(score) >= 4 and abs(score[0] - score[1]) >= 2:
            return print_score(score, player_names, serving_player)

        print_score(score, player_names, serving_player)

def play_set(player_names):
    games = [0, 0]
    serving_player = random.choice(player_names)
    print(f"{serving_player} will serve")
    while True:
        winner = play_game(player_names, serving_player)
        leading_player = 0 if winner == player_names[0] else 1
        games[leading_player] += 1
        print(f"Games: {games[0]}-{games[1]}")
        print(f"{serving_player} will serve")
        if games[leading_player] >= 6 and abs(games[0] - games[1]) >= 2:
            return player_names[0] if games[0] > games[1] else player_names[1]
        if sum(games) % 2 == 0:
            print(f"Change of court.{serving_player} will serve")
            serving_player = player_names[(player_names.index(serving_player) + 1) % 2]

def main():
    player1_name = input("Enter name of Player 1: ")
    player2_name = input("Enter name of Player 2: ")

    while True:
        try:
            sets_to_win = int(input("Enter number of sets to win the match (must be odd): "))
            assert sets_to_win % 2 != 0, "Number of sets must be odd"
            break
        except (ValueError, AssertionError) as e:
            print("Invalid input.")

    player1_sets = 0
    player2_sets = 0

    while True:
        winner = play_set([player1_name, player2_name])
        leading_player = player1_name if winner == player1_name else player2_name
        print(f"Set won by {leading_player}")
        if leading_player == player1_name:
            player1_sets += 1
        else:
            player2_sets += 1
        print(f"Sets: {player1_name} - {player1_sets}, {player2_name} - {player2_sets}")
        if max(player1_sets, player2_sets) == (sets_to_win + 1) // 2:
            break

    print(f"{leading_player} wins the match!")

if __name__ == "__main__":
    main()