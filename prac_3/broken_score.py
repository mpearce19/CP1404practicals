"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


import random


def main():
    """Get a score and display its status."""
    score = float(input("Enter score: "))  # got score from user
    print(determine_status(score))
    random_score = random.randint(0, 100)  # got random score
    print(determine_status(random_score))


def determine_status(score):
    """determine status of score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
