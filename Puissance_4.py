def afficher_grille(grille):
    i = 0
    print("  0 1 2 3 4 5 6")
    for row in grille:
        print(i,end=" ")
        print(" ".join(row))
        i += 1


def check_winner(grille, player):
    # Check horizontally
    for row in grille:
        for i in range(len(row) - 3):
            if all(cell == player for cell in row[i:i+4]):
                return True

    # Check vertically
    for col in range(len(grille[0])):
        for i in range(len(grille) - 3):
            if all(grille[row][col] == player for row in range(i, i+4)):
                return True

    # Check diagonally (from top-left to bottom-right)
    for row in range(len(grille) - 3):
        for col in range(len(grille[0]) - 3):
            if all(grille[row+i][col+i] == player for i in range(4)):
                return True

    # Check diagonally (from top-right to bottom-left)
    for row in range(len(grille) - 3):
        for col in range(3, len(grille[0])):
            if all(grille[row+i][col-i] == player for i in range(4)):
                return True
    return False


def is_full(grille):
    for row in grille:
        if " " in row:
            return False
    return True


def play_game():
    rows = 6
    cols = 7
    grille = [[" " for _ in range(cols)] for _ in range(rows)]
    player = "0"

    while True:
        afficher_grille(grille)

        column = int(input(f"Player {player}, choose a column (1-{cols}): ")) - 1

        # Check if the column is valid
        if 0 <= column < cols and grille[0][column] == " ":
            # Find the lowest available row in the selected column
            for i in range(rows - 1, -1, -1):
                if grille[i][column] == " ":
                    grille[i][column] = player
                    break

            if check_winner(grille, player):
                afficher_grille(grille)
                print(f"Player {player} wins!")
                break
            elif is_full(grille):
                afficher_grille(grille)
                print("It's a draw!")
                break

            # Switch players
            player = "0" if player == "1" else "1"
        else:
            print("Invalid move. Please choose a valid column.")

if __name__ == "__main__":
    play_game()
