import word
import random
import logo

print(logo.title)
placeholder = ""
# Generate a random name
random_name = random.choice(word.collections)
print(random_name)

# Generate as many blanks in chosen random word
lives = 6
word_length = len(random_name)
for letter in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

# Ask user to guess letter
game_over = False
correct_letters = []
while not game_over:
    print(
        f"****************************{lives} LIVES LEFT****************************")

    guess = input("Guess any one letter").lower()
    if guess in correct_letters:
        print(f"You have already guessed  {guess}")
    diplay = ""
    for i in random_name:
        if i == guess:
            diplay += i
            correct_letters.append(guess)
        elif i in correct_letters:
            diplay += i
        else:
            diplay += "_"

    print("Word to guess: " + diplay)
    if guess not in random_name:
        lives -= 1
        print(f"You guessed {guess} it's not in the word")
        if lives == 0:
            game_over = True
            print(
                f"***********************IT WAS {chosen_word} YOU LOSE**********************")
    if "_" not in diplay:
        game_over = True
        print("****************************YOU WIN****************************")

    print(logo.stages[lives])
