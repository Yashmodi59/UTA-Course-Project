import sys

def evaluate_state(num_red, num_blue):
    """
    A helper function to evaluate the current state of the game.
    Returns the score of the current state for the computer player.
    """
    #     # The idea behind this evaluation function is to count the number of piles
    # # that have an odd number of stones in them. The more such piles, the better
    # # the current state for the computer player. This is because if there are an odd
    # # number of piles with an odd number of stones, the computer player can always
    # # force a win.
    # count = 0
    # if num_red % 2 != 0:
    #     count += 1
    # if num_blue % 2 != 0:
    #     count += 1
    # return count
    return 2 * num_red + 3 * num_blue # Scoring Based on weight and no. of red and blue marbles respectively
def eval_state(num_red, num_blue, maximizing):
    """
    The Helper Function to evaluate the total number of marble and then evaluating based on final leaf node 
    """
    su = num_red+num_blue # sum of marbles
    if maximizing: # checking for maximizing
        if su % 2 == 1:
            return 2 +evaluate_state(num_red,num_blue) # normal evaluation of state with addition of 2
        else:
            return -2 -evaluate_state(num_red,num_blue) # negetive normal evalution of state with addition of -2
    else:
        if su % 2 == 1:
            return -2 + -evaluate_state(num_red,num_blue)
        else:
            return 2 + evaluate_state(num_red,num_blue)



def is_terminal(num_red, num_blue): # checking of terminal state
    if num_red == 0 or num_blue==0:
        return True
    return False

def get_poss_moves(num_red,num_blue): # get all possible state with given no. of marbles
    """
    This method returns all possible moves from the current state (i.e., all possible combinations of red and blue marbles that can be removed from the board).
    """
    moves = []
    if num_red == 0:
        moves.append((0,num_blue-1))
    if num_blue == 0:
        moves.append((num_red-1,0))
    elif num_red > 0 and num_blue > 0:
        moves.append((num_red-1,num_blue))
        moves.append((num_red,num_blue-1))
    return moves
# applies the Minimax and Alpha-beta pruning to find the best strategy

# decide based on the current state
    
def alpha_beta_d(num_red, num_blue, maximizing, alpha, beta,depth):
    """
    This is the main function that applies the Minimax algorithm with Alpha-beta pruning to find the best strategy. It uses the eval_state function to evaluate the current state and the is_terminal function to check whether the current state is a terminal state. The alpha and beta parameters are used for Alpha-beta pruning, and the depth parameter is used to set the depth of the search tree
    """
    if is_terminal(num_red, num_blue) or depth == 0:
        return eval_state(num_red, num_blue,maximizing)
    if maximizing:
        best = float("-inf")
        # Recur for left and right children
        for i in get_poss_moves(num_red, num_blue):
            red, blue = i
            val = alpha_beta_d(red, blue, False, alpha, beta,depth-1)
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
        
    else:
        best = float("inf")
        # Recur for left and
        # right children
        for i in get_poss_moves(num_red, num_blue):
            red, blue = i
            val = alpha_beta_d(red, blue, True, alpha, beta,depth-1)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best


def alpha_beta(num_red, num_blue, maximizing, alpha, beta):
    if is_terminal(num_red, num_blue) and maximizing:
        return -evaluate_state(num_red, num_blue)
    if is_terminal(num_red,num_blue) and not maximizing:
        return evaluate_state(num_red,num_blue)
    if maximizing:
        best = float("-inf")
        # Recursion for left and right children of the current state 
        for i in get_poss_moves(num_red, num_blue):
            red, blue = i
            val = alpha_beta(red, blue, False, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
        
    else:
        best = float("inf")
        # Recursion  for left and right children of the current state
        for i in get_poss_moves(num_red, num_blue):
            red, blue = i
            val = alpha_beta(red, blue, True, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
def red_blue_nim_d(num_red, num_blue, first_player="computer",depth=3):
    """
    This is the main function that runs the Red-Blue Nim game. It initializes the board with the given number of red and blue marbles and sets the initial turn based on the first_player parameter. It then runs a loop until the game is over, alternately asking the human player and the computer player to make moves based on the best strategy determined by the alpha_beta_d function.
    """
    board = {'red': num_red, 'blue': num_blue}
    score = {'human': 0, 'computer': 0}
    if first_player == 'human':
        turn = 'human'
    else:
        turn = 'computer'
    while True:
        print(f"Current board state: {board}")
        if board['red'] == 0 or board['blue'] == 0:
            print("\nThe Game Over!!")
            print(f"{turn.capitalize()} wins with {evaluate_state(board['red'] ,board['blue'])}")
            break
        if turn == 'human':
            print("\nYour turn!")
            while True:
                pile = input("Choose a pile (red or blue): ")
                if pile not in ('red', 'blue'):
                    print("Invalid pile. Please choose red or blue.")
                elif board[pile] == 0:
                    print("That pile is empty. Please choose another pile.")
                else:
                    break
            board[pile] -= 1
            # score['human'] = (evaluate_state(board['red'], board['blue']))
            turn = 'computer'
        else:
            print("\nComputer Turn!\n")
            best_score = float("-inf")
            num_red, num_blue = board['red'], board['blue']
            best_move = None
            alpha = -float('inf')
            beta = float('inf')
            # maxTurn = True
            # state = [num_red, num_blue]
            # val, res = decide(state, alpha, beta, maxTurn)
            # next_state = res[1]
            # move = [next_state[i] - state[i] for i in range(len(state))]

            # print("Computer move: ", move)
            print(f"Choices to perform by computer {get_poss_moves(num_red, num_blue)}")
            for move in get_poss_moves(num_red, num_blue):
                red, blue = move
                score= alpha_beta_d(red, blue, True,alpha,beta,depth)
                if score>best_score:
                    best_score = score
                    best_move = move

            print(f"Computer Will perform {best_move}")       
            board['red'], board['blue'] = best_move
            print(f"Current board state after computer's turn: {board}")                    
            # # while True:
            # #     pile = input("Choose a pile (red or blue): ")
            # #     if pile not in ('red', 'blue'):
            # #         print("Invalid pile. Please choose red or blue.")
            # #     elif board[pile] == 0:
            # #         print("That pile is empty. Please choose another pile.")
            # #     else:
            # #         break
            # board[pile] -= 1
            # score['computer'] = evaluate_state(board['red'], board['blue'])
            turn = 'human'

def red_blue_nim(num_red, num_blue, first_player="computer"):
    board = {'red': num_red, 'blue': num_blue}
    score = {'human': 0, 'computer': 0}
    if first_player == 'human':
        turn = 'human'
    else:
        turn = 'computer'
    while True:
        print(f"Current board state: {board}")
        if board['red'] == 0 or board['blue'] == 0:
            print("The Game Over!!")
            print()
            print(f"{turn.capitalize()} wins with {evaluate_state(board['red'] ,board['blue'])}")
            break
        if turn == 'human':
            print("\nYour turn!")
            while True:
                pile = input("Choose a pile (red or blue): ")
                if pile not in ('red', 'blue'):
                    print("Invalid pile. Please choose red or blue.")
                elif board[pile] == 0:
                    print("That pile is empty. Please choose another pile.")
                else:
                    break
            board[pile] -= 1 # subtracting 1 from given pile
            # score['human'] = (evaluate_state(board['red'], board['blue']))
            turn = 'computer'
        else:
            print("\nComputer Turn!")
            best_score = float("-inf")
            num_red, num_blue = board['red'], board['blue']
            best_move = None
            alpha = -float('inf')# -inf
            beta = float('inf')#inf
            # maxTurn = True
            # state = [num_red, num_blue]
            # val, res = decide(state, alpha, beta, maxTurn)
            # next_state = res[1]
            # move = [next_state[i] - state[i] for i in range(len(state))]

            # print("Computer move: ", move)
            print(f"Choices to perform by computer {get_poss_moves(num_red, num_blue)}")
            for move in get_poss_moves(num_red, num_blue): # getting all possible states
                red, blue = move
                score= alpha_beta(red, blue, True,alpha,beta) # call alpha beta
                if score>best_score:
                    best_score = score
                    best_move = move

            print(f"Computer Will perform {best_move}")       
            board['red'], board['blue'] = best_move
            print(f"Current board state after computer's turn: {board}")
                    
            # # while True:
            # #     pile = input("Choose a pile (red or blue): ")
            # #     if pile not in ('red', 'blue'):
            # #         print("Invalid pile. Please choose red or blue.")
            # #     elif board[pile] == 0:
            # #         print("That pile is empty. Please choose another pile.")
            # #     else:
            # #         break
            # board[pile] -= 1
            # score['computer'] = evaluate_state(board['red'], board['blue'])
            turn = 'human'
if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: red_blue_nim.py <num-red> <num-blue> [<first-player>] [<depth>]')
        sys.exit(1)

    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])

    first_player = 'computer'
    if len(sys.argv) > 3:
        first_player = sys.argv[3]

    depth = None
    if len(sys.argv) > 4:
        depth = int(sys.argv[4])
    if depth == None:
        red_blue_nim(num_red, num_blue, first_player.lower())
    else:
        red_blue_nim_d(num_red,num_blue,first_player.lower(),depth)
# red_blue_nim(5,6,'human')