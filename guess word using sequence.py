import os

def guess_word(prompt, correct_word, max_attempts=3):
    os.system("clear")
    print(prompt)

    for attempt in range(max_attempts):
        guess = input(">").strip()

        if guess.casefold() == correct_word.casefold():
            print("Great job!")
            return True

        print(f"Try again! Attempts left: {max_attempts - attempt - 1}")

    return False

def main():
    print("HELLO FELLOWS!".center(50, "*"))

    input("Press Enter to begin the guessing game!".center(50, "*"))

    correct1 = guess_word("Enter the word generated from this number sequence.\n6, 21, 14", "Fun")

    if correct1:
        while correct1:
            correct2 = guess_word("Enter the word generated from this number sequence.\n19, 15, 14, 7", "Song")

            if correct2:
                while correct2:
                    correct3 = guess_word("Enter the word generated from this number sequence.\n10, 21, 13, 16", "Jump")

                    if correct3:
                        while correct3:
                            correct4 = guess_word("Enter the word generated from this number sequence.\n3 15 13 16 21 20 5 18", "Computer")

                            if correct4:
                                print("Congratulations! You completed the game.")
                                return  # End the game

                            break  # Exit the innermost loop

                        if not correct4:
                            break  # Exit the middle loop

                    if not correct3:
                        break  # Exit the outer loop

                if not correct2:
                    break  # Exit the outermost loop

        input("Press Enter to end the game.")
        os.system("clear")

if __name__ == "__main__":
    main()
