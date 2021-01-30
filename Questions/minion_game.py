"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

For better understanding, see the image below:

banana.png

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Constraints



Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA
Sample Output

Stuart 12
Note :
Vowels are only defined as . In this problem,  is not considered a vowel.
"""
def minion_game(string):
    # that is because, we need the number of words starting with either vowel or consonant. 
    # So, subtracting the index of the found 'vowel' in this case, gives us the number of words starting from that index with a vowel at first. 
    # For the word "BANANA", the first vowel 'A' occurs at position 1, len("BANANA") = 6, so there are 6-1 = 5 substrings starting with this letter 'A': ['A', 'AN', 'ANA', 'ANAN', 'ANANA'], you add one extra letter to that specific letter 'A' until you get to the end of the word.
    
    vowel="AEIUO"
    s=0
    k=0
    for i in range(len(string)):
        if string[i] in vowel:
            k+=len(string)-i
        else:
            s+=len(string)-i
    if k>s:
        print("Kevin",k)
    elif k<s:
        print("Stuart",s)
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
