import random
import pandas as pd  # Added for data analysis and storing roll history
import time  # Added for timing functions and delays

def roll_dice():
    die1 = random.choice(range(1, 7))  # Random number between 1 and 6
    die2 = random.choice(range(1, 7))  # Random number between 1 and 6
    die3 = random.choice(range(1, 7))  # Random number between 1 and 6
    return die1, die2, die3, die1 + die2 + die3  # Return three dice and their sum

def play_game():
    """
    Main function to simulate the tupled dice game.
    Tracks the player's cumulative score and high score.
    """
    print("🎲🎉 Welcome to the Tuple Dice Game! 🎉🎲")
    print("Try to get the highest score possible! 🚀")
    
    high_score = 0
    current_score = 0
    playing = True
    roll_history = pd.DataFrame(columns=["Die 1", "Die 2", "Die 3", "Total"])   
    
    start_time = time.time()  # Record the game start time

    while playing:
        input("👉 Press Enter to roll the dice... 🎲")
        dice_roll = roll_dice()

        # Check for "Tupled out" (all three dice are the same)
        if dice_roll[0] == dice_roll[1] == dice_roll[2]:
            print(f"🚨 Tupled Out! You rolled three {dice_roll[0]}'s! 🚨")
            print(f"🎮 Game Over! 🎮")
            print(f"Your final score: {current_score}")
            print(f"🏅 Your high score: {high_score}")
            print("🎲 Thanks for playing!")
            break
        
        # Add roll data to the DataFrame
        roll_history = roll_history.append({"Die 1": dice_roll[0], 
                                    "Die 2": dice_roll[1], 
                                    "Die 3": dice_roll[2], 
                                    "Total": dice_roll[3]}, 
                                   ignore_index=True)
        print(f"🎲 You rolled: {dice_roll[0]}, {dice_roll[1]}, and {dice_roll[2]} (Total: {dice_roll[3]}) 🎲")
        
        current_score += dice_roll[2]
        print(f"Your current score is: {current_score}")
        
        # Update high score if current score exceeds it
        if current_score > high_score:
            high_score = current_score
            print(f"🏆 New high score: {high_score}! 🎉")
    
        # Track dice that have the same value
        fixed_dice = [False, False, False]  # False means not fixed
        
        if dice_roll[0] == dice_roll[1]:
            fixed_dice[0] = fixed_dice[1] = True
        if dice_roll[0] == dice_roll[2]:
            fixed_dice[0] = fixed_dice[2] = True
        if dice_roll[1] == dice_roll[2]:
            fixed_dice[1] = fixed_dice[2] = True
        
        # Re-roll the non-fixed dice
        rerolled = False
        while not all(fixed_dice):
            print(f"Fixed dice: {fixed_dice}")  # Display which dice are fixed
            rerolled_dice = []
            if not fixed_dice[0]:
                rerolled_dice.append(1)
            if not fixed_dice[1]:
                rerolled_dice.append(2)
            if not fixed_dice[2]:
                rerolled_dice.append(3)
            
            dice_roll = list(dice_roll[:3])  # Convert to a list for easier modification
            
            for die_index in rerolled_dice:
                dice_roll[die_index - 1] = random.choice(range(1, 7))  # Re-roll the die

            dice_roll.append(sum(dice_roll[:3]))  # Update the total sum of the dice

            print(f"🎲 You rolled: {dice_roll[0]}, {dice_roll[1]}, and {dice_roll[2]} (Total: {dice_roll[3]}) 🎲")
            
            # Check again if the player has "tupled out"
            if dice_roll[0] == dice_roll[1] == dice_roll[2]:
                print(f"🚨 Tupled Out! You rolled three {dice_roll[0]}'s! 🚨")
                print(f"🎮 Game Over! 🎮")
                print(f"Your final score: {current_score}")
                print(f"🏅 Your high score: {high_score}")
                print("🎲 Thanks for playing!")
                break
            
            # Ask if the player wants to roll again
            choice = input("Do you want to roll again? (yes/no): ").strip().lower()
            if choice != "yes":
                playing = False
                break
            rerolled = True
        
        # Add roll data to the DataFrame after all rolls
        roll_history = roll_history.append({"Die 1": dice_roll[0], 
                                            "Die 2": dice_roll[1], 
                                            "Die 3": dice_roll[2], 
                                            "Total": dice_roll[3]}, 
                                           ignore_index=True)
            
    end_time = time.time()  # Record the game end time
    duration = end_time - start_time  # Calculate the total game duration
    print(f"\n⏱️ Total playtime: {duration:.2f} seconds")  # Display game duration

    print("\n📊 Your Dice Roll History:")
    print(roll_history) # Display dice roll history
    
    print("\n🎮 Game Over! 🎮")
    print(f"Your final score: {current_score}")
    print(f"🏅 Your high score: {high_score}")
    print("🎲 Thanks for playing!")

# Seed for consistent results during testing
random.seed(42)

# Start the game
play_game()
