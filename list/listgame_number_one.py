import time  # Importing the time module to use the sleep function

print("Welcome to the Memory Challenge!")

# Initialize an empty list to store the words
word_list = []

# Ask the user for 5 words
for i in range(5):
    word = input(f"Enter word {i + 1}: ").strip()
    word_list.append(word)  # Add the word to the list

print("\nHere are the words you entered:")
print(word_list)  # Display the list to the user

# Wait for 5 seconds so the user can memorize the list
time.sleep(5)

# Clear the screen (just a placeholder message; real screen clearing depends on the environment)
print("\n" * 50)
print("Now, try to remember the words you entered!")

# Ask the user to recall the words
user_answers = []
for i in range(5):
    answer = input(f"What was word {i + 1}? ").strip()
    user_answers.append(answer)  # Collect the user's answers

# Compare the original list with the user's answers
print("\nComparing your answers with the original list...")
for i in range(5):
    if word_list[i] == user_answers[i]:
        print(f"Word {i + 1}: Correct! ({word_list[i]})")
    else:
        print(f"Word {i + 1}: Incorrect. You said '{user_answers[i]}', but it was '{word_list[i]}'.")

print("\nThanks for playing the Memory Challenge!")
