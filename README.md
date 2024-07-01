# number-guessing-python-script

This script helps the computer guess a number you're thinking of. You set a range by giving the highest number. The computer guesses the middle number and asks if it's correct. You tell it if the number is right, or if your number is higher or lower. The computer changes its guess based on your answers until it finds your number. If it can't find the number, it thinks you might not be playing fair.

## Steps:

### Initialize Range:
The user is prompted to input the upper limit (**rear**) of the range, with (**front**) set to 1.

### Binary Search Loop:
The script calculates the middle point of the current range (**middle**).

It asks the user if the guessed number (**middle**) is correct.

If the guess is correct, it sets (**found**) to True and exits the loop. 

If the guess is incorrect, it asks whether the number is higher or lower than the guess. 

Based on the user's response, it adjusts the range: 

If higher, it sets (**front**) to middle + 1. 

If lower, it sets (**rear**) to middle - 1.

### Conclusion:
If the number is found, it prints the guessed number.

If the user didn't answer the questions honestly, it prints the message "You cheated."
