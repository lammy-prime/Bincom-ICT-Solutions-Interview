# import re
# import random
from collections import Counter
# from itertools import chain
import psycopg2

# Simulated color data extracted from the HTML table
color_data = [
    "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE",
    "GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE",
    "BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN",
    "GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE"
]

# Normalize and count colors
color_counts = Counter()
for day_colors in color_data:
    colors = day_colors.replace(" ", "").split(",")
    # Fix common typos
    colors = [color.upper() if color != "BLEW" else "BLUE" for color in colors] # Assuming 'BLEW' is a typo for 'BLUE'
    color_counts.update(colors)

# Find the mean color (most common color)
mean_color = color_counts.most_common(1)[0]  # Returns a list of the n most common elements and their counts
print(f"The 'mean' color, interpreted as the most common color, is: {mean_color[0]} with {mean_color[1]} appearances.")

# Which color is mostly worn throughout the week?
print(f"The color most worn throughout the week is: {mean_color[0]}")

# Assuming the task for the "mean color" is finding the most common color.
# Continue from the previous color_counts calculation

# 3. Which color is the median?
sorted_colors = color_counts.most_common()  # Sort colors by frequency
median_index = len(sorted_colors) // 2
median_color = sorted_colors[median_index][0] if len(sorted_colors) % 2 != 0 else "Ambiguous"
print(f"The median color is: {median_color}")

# 4. Variance of the colors - A simple interpretation using frequency as a measure of spread
# NOTE: This is not a statistical variance but gives an idea of spread or diversity in color choices
variances = [freq for color, freq in color_counts.items()]
mean_frequency = sum(variances) / len(variances)
variance = sum((xi - mean_frequency) ** 2 for xi in variances) / len(variances)
print(f"The 'variance' in color choice, interpreted through frequency spread, is: {variance}")

# 5. Probability that a chosen color is red
total_colors = sum(color_counts.values())
red_probability = color_counts["RED"] / total_colors
print(f"The probability that a randomly chosen color is red is: {red_probability:.2f}")


