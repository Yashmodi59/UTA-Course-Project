
Name: Yash Modi
UTA ID: 1002086296
Language and version:Python 3.11.3
To run this code you must have python3 install
run the given code with given following configuration

Sample command: python3 red_blue_nim.py <num-red> <num-blue> [<first-player>] [<depth>]

by default first_player is computer if entered human than human 
depth is also optional
example:
pyhton3 red_blue_nim.py 3 4 computer 3
pyhton3 red_blue_nim.py 3 4 human 3
pyhton3 red_blue_nim.py 3 4 human
pyhton3 red_blue_nim.py 3 4 computer
pyhton3 red_blue_nim.py 3 4

for depth limited entering first_player is mandatory

Here num_red and num_blue has to be compulsory pass.
First player is not compulsory to pass which will decide who is the first player

Either "computer" or "human" must be entered

If the depth argument is not provided, the script will call the function red_blue_nim(), 
which presumably implements the game logic for Red-Blue Nim, passing in the number of red and blue pieces and the first player as arguments. 
If the depth argument is provided, the script will call a function called red_blue_nim_d() instead, 
passing in the same arguments as well as the depth.

If the script is run without enough arguments, 
it will print a usage statement and exit with a status code of 1.

Structure of code:
if __name__ == '__main__': will start working from Here
First will identify the first player who is either computer or human
than will see if depth is given than will call red_blue_nim_d
else red_blue_nim and will work accordingly

Explaination of each code id given seperate txt first_player
reference:
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
PPT gameplaying
http://estudies4you.blogspot.com/2021/06/learning-evaluation-functions-in.html#:~:text=An%20evaluation%20function%20improves%20the,game%20from%20a%20given%20position.

