import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def check_streak(flips, streak_length):
    count = 1  # Start counting from the first element
    streak_count = 0  # Variable to count how many streaks of the given length happen

    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:  # Check if the current flip is the same as the previous one
            count += 1
            if count == streak_length:
                streak_count += 1  # Increment the streak count if a streak is found
                count = 1  # Reset the count after detecting a streak (optional behavior)
        else:
            count = 1  # Reset the count if the flip is different

    return streak_count

def coin_flip_game():
    flips = []  # List to store the coin flips
    streak_length = 6  # Define the streak length you're looking for

    # Simulate 100 coin flips
    for _ in range(100):
        flips.append(flip_coin())
    
    print(f"Coin flips: {flips}")
    
    streaks = check_streak(flips, streak_length)
    
    if streaks > 0:
        print(f"There were {streaks} streak(s) of {streak_length} consecutive flips!")
    else:
        print(f"No streak of {streak_length} consecutive flips found.")

# Run the game
coin_flip_game()
