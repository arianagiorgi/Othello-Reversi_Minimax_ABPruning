from engines import Engine
from copy import deepcopy
import timeit

class StudentEngine(Engine):
    """ Game engine that implements a simple fitness function maximizing the
    difference in number of pieces in the given color's favor. """
    def __init__(self):
        self.alpha_beta = False
        self.cutoff = 2 #define number of levels to search in minimax func
        self.node_count = 0
        self.branch_count = 0
        self.branch_list = []
        self.list_of_boards = []
        self.duplicates = 0

    def minimax (self, board, depth, color, maximixingPlayer):
        if (depth == 0) or (len(board.get_legal_moves(color)) == 0):
            #if depth = 0 || no moves can be made 
            #heuristic to calculate value taken from 'An Analysis of Heuristics in Othello' via U of Washington - see report
            #coin parity
            if (maximixingPlayer):
                cp = 100 * (board.count(color) - board.count(-color))/(board.count(color) + board.count(-color))
            else:
                cp = 100 * (board.count(-color) - board.count(color))/(board.count(color) + board.count(-color))

            #mobility
            if (len(board.get_legal_moves(color)) + len(board.get_legal_moves(-color)) != 0):
                if (maximixingPlayer):
                    m = 100 * (len(board.get_legal_moves(color)) - len(board.get_legal_moves(-color)))/(len(board.get_legal_moves(color)) + len(board.get_legal_moves(-color)))
                else:
                    m = 100 * (len(board.get_legal_moves(-color)) - len(board.get_legal_moves(color)))/(len(board.get_legal_moves(color)) + len(board.get_legal_moves(-color)))
            else:
                m = 0
    
            #corners captured
            corners = [(0,0),(7,7),(0,7),(7,0)] #define corners of the board

            if (maximixingPlayer):
                max_num_corners = 0
                min_num_corners = 0
                for corner in corners:
                    if corner in board.get_squares(color):
                        max_num_corners = max_num_corners + 1
                    elif corner in board.get_squares(-color):
                        min_num_corners = min_num_corners + 1
            else:
                max_num_corners = 0
                min_num_corners = 0
                for corner in corners:
                    if corner in board.get_squares(-color):
                        max_num_corners = max_num_corners + 1
                    elif corner in board.get_squares(color):
                        min_num_corners = min_num_corners + 1

            if (max_num_corners + min_num_corners != 0):
                c = 100 * (max_num_corners - min_num_corners)/(max_num_corners + min_num_corners)
            else:
                c = 0

            #final value
            value = (3 * c) +(2 * m) + cp

            #self.node_count = self.node_count + 1

            ''''duplicates 
            #grab the display
            current_board = " "
            for y in range(7,-1,-1):
                # Print the row number
                for x in range(8):
                    # Get the piece to print
                    piece = board[x][y]
                    if piece == -1:
                        current_board = current_board + "B"
                    elif piece == 1:
                        current_board = current_board + "W"
                    else:
                        current_board = current_board + "."

            if current_board in self.list_of_boards:
                self.duplicates = self.duplicates + 1
            else:
                self.list_of_boards.append(current_board)'''

            return (value, None, None)
        else:
            if (maximixingPlayer):
                moves = board.get_legal_moves(color)
                #self.branch_count = self.branch_count + 1
                bestValue = float('-inf')
                for i in range(len(moves)):
                    #self.node_count = self.node_count + 1
                    b = deepcopy(board)
                    b.execute_move(moves[i], color)

                    '''duplicates
                    #grab the display
                    current_board = " "
                    for y in range(7,-1,-1):
                    # Print the row number
                        for x in range(8):
                    # Get the piece to print
                            piece = board[x][y]
                            if piece == -1:
                                current_board = current_board + "B"
                            elif piece == 1:
                                current_board = current_board + "W"
                            else:
                                current_board = current_board + "."

                    if current_board in self.list_of_boards:
                        self.duplicates = self.duplicates + 1
                    else:
                        self.list_of_boards.append(current_board)'''




                    value = self.minimax(b, depth-1, -color, False)[0]
                    if (value > bestValue):
                        bestValue = value
                        move = moves[i]
                return (value, move)
            else: #minimizing player (opponent)
                moves = board.get_legal_moves(color)
                #self.branch_count = self.branch_count + 1
                bestValue = float('inf')
                for i in range(len(moves)):
                    #self.node_count = self.node_count + 1
                    b = deepcopy(board)
                    b.execute_move(moves[i], color)

                    '''duplicates
                    #grab the display
                    current_board = " "
                    for y in range(7,-1,-1):
                    # Print the row number
                        for x in range(8):
                    # Get the piece to print
                            piece = board[x][y]
                            if piece == -1:
                                current_board = current_board + "B"
                            elif piece == 1:
                                current_board = current_board + "W"
                            else:
                                current_board = current_board + "."

                    if current_board in self.list_of_boards:
                        self.duplicates = self.duplicates + 1
                    else:
                        self.list_of_boards.append(current_board)'''



                    value = self.minimax(b, depth-1, -color, True)[0]
                    if (value < bestValue):
                        bestValue = value
                        move = moves[i]
                return (value, move)

    def alpha_beta_minimax (self, board, depth, color, alpha, beta, maximixingPlayer):
        if (depth == 0) or (len(board.get_legal_moves(color)) == 0):
            #if depth = 0 || no moves can be made 
            #heuristic to calculate value taken from 'An Analysis of Heuristics in Othello' via U of Washington - see report
            #coin parity
            if (maximixingPlayer):
                cp = 100 * (board.count(color) - board.count(-color))/(board.count(color) + board.count(-color))
            else:
                cp = 100 * (board.count(-color) - board.count(color))/(board.count(color) + board.count(-color))

            #mobility
            if (len(board.get_legal_moves(color)) + len(board.get_legal_moves(-color)) != 0):
                if (maximixingPlayer):
                    m = 100 * (len(board.get_legal_moves(color)) - len(board.get_legal_moves(-color)))/(len(board.get_legal_moves(color)) + len(board.get_legal_moves(-color)))
                else:
                    m = 100 * (len(board.get_legal_moves(-color)) - len(board.get_legal_moves(color)))/(len(board.get_legal_moves(color)) + len(board.get_legal_moves(-color)))
            else:
                m = 0

            #corners captured
            corners = [(0,0),(7,7),(0,7),(7,0)] #define corners of the board

            if (maximixingPlayer):
                max_num_corners = 0
                min_num_corners = 0
                for corner in corners:
                    if corner in board.get_squares(color):
                        max_num_corners = max_num_corners + 1
                    elif corner in board.get_squares(-color):
                        min_num_corners = min_num_corners + 1
            else:
                max_num_corners = 0
                min_num_corners = 0
                for corner in corners:
                    if corner in board.get_squares(-color):
                        max_num_corners = max_num_corners + 1
                    elif corner in board.get_squares(color):
                        min_num_corners = min_num_corners + 1

            if (max_num_corners + min_num_corners != 0):
                c = 100 * (max_num_corners - min_num_corners)/(max_num_corners + min_num_corners)
            else:
                c = 0

            #final value
            value = (3 * c) + (2 * m) + cp
            #self.node_count = self.node_count + 1

            '''duplicates
            #grab the display
            current_board = " "
            for y in range(7,-1,-1):
                # Print the row number
                for x in range(8):
                    # Get the piece to print
                    piece = board[x][y]
                    if piece == -1:
                        current_board = current_board + "B"
                    elif piece == 1:
                        current_board = current_board + "W"
                    else:
                        current_board = current_board + "."

            if current_board in self.list_of_boards:
                self.duplicates = self.duplicates + 1
            else:
                self.list_of_boards.append(current_board)'''


            return (value, None)
        else:
            if (maximixingPlayer):
                moves = board.get_legal_moves(color)
                #self.branch_count = self.branch_count + 1
                move = None
                for i in range(len(moves)):
                    #self.node_count = self.node_count + 1
                    b = deepcopy(board)
                    b.execute_move(moves[i], color)

                    '''duplicates
                    #grab the display
                    current_board = " "
                    for y in range(7,-1,-1):
                    # Print the row number
                        for x in range(8):
                    # Get the piece to print
                            piece = board[x][y]
                            if piece == -1:
                                current_board = current_board + "B"
                            elif piece == 1:
                                current_board = current_board + "W"
                            else:
                                current_board = current_board + "."

                    if current_board in self.list_of_boards:
                        self.duplicates = self.duplicates + 1
                    else:
                        self.list_of_boards.append(current_board)'''


                    value = self.alpha_beta_minimax(b, depth-1, -color, alpha, beta, False)[0]
                    if (value > alpha):
                        alpha = value
                        move = moves[i]
                    if (beta <= alpha):
                        break #beta cut-off
                return (alpha, move)
            else:
                moves = board.get_legal_moves(color)
                #self.branch_count = self.branch_count + 1
                move = None
                for i in range(len(moves)):
                    #self.node_count = self.node_count + 1
                    b = deepcopy(board)
                    b.execute_move(moves[i], color)

                    '''duplicates
                    #grab the display
                    current_board = " "
                    for y in range(7,-1,-1):
                    # Print the row number
                        for x in range(8):
                    # Get the piece to print
                            piece = board[x][y]
                            if piece == -1:
                                current_board = current_board + "B"
                            elif piece == 1:
                                current_board = current_board + "W"
                            else:
                                current_board = current_board + "."

                    if current_board in self.list_of_boards:
                        self.duplicates = self.duplicates + 1
                    else:
                        self.list_of_boards.append(current_board)'''


                    value = self.alpha_beta_minimax(b, depth-1, -color, alpha, beta, True)[0]
                    if (value < beta):
                        beta = value
                        move = moves[i]
                    if (beta <= alpha):
                        break #alpha cut-off
                return (beta, move)

    def get_move(self, board, color, move_num=None,
                 time_remaining=None, time_opponent=None):
        """ Return a move for the given color that maximizes the difference in 
        number of pieces for that color. """
        # Get a list of all legal moves.
        #moves = board.get_legal_moves(color)


        #minimax code
        if (self.alpha_beta == False):
            #start_time = timeit.default_timer()
            res = self.minimax(board, self.cutoff, color, True)
            #end_time = timeit.default_timer()
        else:
            #start_time = timeit.default_timer()
            res = self.alpha_beta_minimax(board, self.cutoff, color, float('-inf'), float('inf'), True)
            #end_time = timeit.default_timer()

        '''Statistics'''
        #print self.node_count: minimax:6215
        #print self.node_count: alphabeta:1692
        #print (end_time - start_time)
        #minimax time range, depth 2: [0.028, 2.585]; depth 3: [0.150, 10.72]; depth 4: [0.662, 72.06]
        #alphabet time range, depth 2: [0.012, 1.711]; depth 3: [0.078, 4.601]; depth 4: [0.312, 6.750]
        #self.branch_list.append(self.branch_count)     
        #avg = sum(self.branch_list)/len(self.branch_list)
        #print avg: minimax: 162, alphabeta: 166
        #print self.duplicates minimax: 1907, alphabeta: 854

        #return the move
        return res[1]

        # Return the best move according to our simple utility function:
        # which move yields the largest different in number of pieces for the
        # given color vs. the opponent?
        #return max(moves, key=lambda move: self._get_cost(board, color, move))

    def _get_cost(self, board, color, move):
        """ Return the difference in number of pieces after the given move 
        is executed. """

        # Create a deepcopy of the board to preserve the state of the actual board
        newboard = deepcopy(board)
        newboard.execute_move(move, color)

        # Count the # of pieces of each color on the board
        num_pieces_op = len(newboard.get_squares(color*-1))
        num_pieces_me = len(newboard.get_squares(color))

        # Return the difference in number of pieces
        return num_pieces_me - num_pieces_op

engine = StudentEngine
