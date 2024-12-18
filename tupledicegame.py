import random
import pandas as pd  # Added for data analysis and storing roll history
import time  # Added for timing functions and delays

def roll_dice():
    """
    Simulates rolling two dice using tuples and random choices.
    Returns a tuple containing the values of two dice and their sum.
    """
    die1 = random.choice(range(1, 7))  # Random number between 1 and 6
    die2 = random.choice(range(1, 7))  # Random number between 1 and 6
    return die1, die2, die1 + die2  # Cleaner tuple return

def play_game():
    """
    Main function to simulate the tuple dice game.
    Tracks the player's cumulative score and high score.
    """
    print("🎲🎉 Welcome to the Tuple Dice Game! 🎉🎲")
    print("Try to get the highest score possible! 🚀")
    
    high_score = 0
    current_score = 0
    playing = True
    roll_history = pd.DataFrame(columns=["Die 1", "Die 2", "Total"])    

    while playing:
        input("👉 Press Enter to roll the dice... 🎲")
        dice_roll = roll_dice()
        # Add roll data to the DataFrame
        roll_history = roll_history.append({"Die 1": dice_roll[0], 
                                    "Die 2": dice_roll[1], 
                                    "Total": dice_roll[2]}, 
                                   ignore_index=True)
        print(f"🎲 You rolled: {dice_roll[0]} and {dice_roll[1]} (Total: {dice_roll[2]}) 🎲")
        
        current_score += dice_roll[2]
        print(f"Your current score is: {current_score}")
        
        # Update high score if current score exceeds it
        if current_score > high_score:
            high_score = current_score
            print(f"🏆 New high score: {high_score}! 🎉")
        
        # Ask if the player wants to roll again
        choice = input("Do you want to roll again? (yes/no): ").strip().lower()
        if choice != "yes":
            playing = False
    
    print("\n🎮 Game Over! 🎮")
    print(f"Your final score: {current_score}")
    print(f"🏅 Your high score: {high_score}")
    print("🎲 Thanks for playing!")

# Seed for consistent results during testing
random.seed(42)

# Start the game
play_game()
