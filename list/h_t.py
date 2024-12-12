import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def check_streak(flips, streak_length):
    # This function checks if there are any streaks of a given length
    count = 1  # Start counting from the first element
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            count += 1
            if count == streak_length:
                return True  # Streak found
        else:
            count = 1  # Reset the streak count if the flip is different
    return False

def coin_flip_game():
    flips = []  # List to store the coin flips
    streak_length = 6  # Define the streak length you're looking for

    # Simulate 100 coin flips
    for _ in range(10000):
        flips.append(flip_coin())
    
    print(f"Coin flips: {flips}")
    
    if check_streak(flips, streak_length):
        print(f"There is a streak of {streak_length} consecutive flips!")
    else:
        print(f"No streak of {streak_length} consecutive flips found.")

# Run the game
coin_flip_game()
