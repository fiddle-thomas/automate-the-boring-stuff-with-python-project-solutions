import random

# Note: This implementation counts non-overlapping streaks of exactly 6 heads or tails.
# Streaks are reset after each occurrence of 6 in a row.

total_streaks = 0

# Run the experiment 10,000 times
for _ in range(10000):
    flips = []
    # Generate 100 coin flips (0 for heads, 1 for tails)
    for _ in range(100):
        flips.append(random.randint(0, 1))

    # Count the streaks in 100 flips 
    streak_of_heads = 0
    streak_of_tails = 0
    for result in flips:
        if result == 0:  # Heads
            streak_of_heads += 1
            streak_of_tails = 0
            if streak_of_heads == 6:
                total_streaks += 1
                streak_of_heads = 0
        else:  # Tails
            streak_of_tails += 1
            streak_of_heads = 0
            if streak_of_tails == 6:
                total_streaks += 1
                streak_of_tails = 0

print(f"Chance of streak: {total_streaks / 10000}%")