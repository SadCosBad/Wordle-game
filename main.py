from game import Game
from gui import display_board, display_message

def main():
    game = Game()  # create game instanceword

    while not game.game_over:
        display_board(game)

        guess = input("Enter your guess: ").upper()

        if not game.is_valid_guess(guess):
            display_message("Invalid guess, try again.")
            continue

        result = game.make_guess(guess)

        display_message(result)

    # game ended
    display_board(game)

    if game.won:
        print("🎉 You won!")
    else:
        print(f"💀 You lost! The word was {game.secret_word}")

if __name__ == "__main__":
    main()