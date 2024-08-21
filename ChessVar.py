# Description: This program is a game of Atomic Chess, where whenever a piece is captured, an "explosion" occurs at the
# 8 squares immediately surrounding the captured piece in all the directions. This explosion kills all the pieces in its
# range except for pawns. In Atomic Chess, every capture is suicidal. Even the capturing piece is affected by the
# explosion and must be taken off the board

class ChessVar:
    """A class to represent a player in the Atomic Chess game, where the color ‘white’ starts first"""

    def __init__(self):
        """Constructor for the Chess class. Takes no parameters. Initializes the turn, white and black pieces,
        white and black pieces’ locations, and the possible moves for each piece. All data members are private."""
        # Turn starts with white pieces
        self._turn = 'white'
        self._white_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                              'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
        # White pieces position
        self._white_locations = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                                 (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
        self._black_pieces = ['rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook',
                              'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn']
        # Black pieces position
        self._black_locations = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                 (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

        # Initialize all piece possible moves
        self._king_possible_moves = self._generate_king_possible_moves()
        self._bishop_possible_moves = self._generate_bishop_possible_moves()
        self._knight_possible_moves = self._generate_knight_possible_moves()
        self._rook_possible_moves = self._generate_rook_possible_moves()
        self._update_pawn_possible_moves()

    def _generate_king_possible_moves(self):
        """Generate all possible moves for a king from each position on the board"""
        possible_moves = {}
        for row in range(8):
            for col in range(8):
                moves = []
                # Generate potential moves in all 8 directions
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue
                        new_row, new_col = row + dr, col + dc
                        if 0 <= new_row < 8 and 0 <= new_col < 8:
                            moves.append((new_row, new_col))
                possible_moves[(row, col)] = moves
        return possible_moves

    def _generate_bishop_possible_moves(self):
        """Generate all possible moves for a bishop from each position on the board"""
        directions = {
            'ne': (1, 1),
            'nw': (1, -1),
            'se': (-1, 1),
            'sw': (-1, -1)
        }

        possible_moves = {}
        for row in range(8):
            for col in range(8):
                moves = {'ne': [], 'nw': [], 'se': [], 'sw': []}
                for direction, (dr, dc) in directions.items():
                    r, c = row, col
                    while True:
                        r += dr
                        c += dc
                        if 0 <= r < 8 and 0 <= c < 8:
                            moves[direction].append((r, c))
                        else:
                            break
                possible_moves[(row, col)] = moves
        return possible_moves

    def _generate_knight_possible_moves(self):
        """Generate all possible moves for a knight from each position on the board"""
        knight_moves = [
            (2, 1), (1, 2), (-1, 2), (-2, 1),
            (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]

        possible_moves = {}
        for row in range(8):
            for col in range(8):
                moves = []
                for dr, dc in knight_moves:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        moves.append((new_row, new_col))
                possible_moves[(row, col)] = moves
        return possible_moves

    def _generate_rook_possible_moves(self):
        """Generate all possible moves for a rook from each position on the board"""
        directions = {
            'up': (0, 1),
            'down': (0, -1),
            'right': (1, 0),
            'left': (-1, 0)
        }

        possible_moves = {}
        for row in range(8):
            for col in range(8):
                moves = {'up': [], 'down': [], 'right': [], 'left': []}
                for direction, (dr, dc) in directions.items():
                    r, c = row, col
                    while True:
                        r += dr
                        c += dc
                        if 0 <= r < 8 and 0 <= c < 8:
                            moves[direction].append((r, c))
                        else:
                            break
                possible_moves[(row, col)] = moves
        return possible_moves

    def _update_pawn_possible_moves(self):
        """Update possible moves for pawns (implementation not shown)"""
        pass


    def _update_pawn_possible_moves(self):
        """Generate possible moves for white and black pawns from each position on the board"""
        self._white_pawn_possible_moves = self._generate_pawn_possible_moves('white')
        self._black_pawn_possible_moves = self._generate_pawn_possible_moves('black')

    def _generate_pawn_possible_moves(self, color):
        """Generate all possible moves for pawns of the given color"""
        pawn_moves = {}
        direction = 1 if color == 'white' else -1
        for row in range(8):
            for col in range(8):
                moves = []
                if (color == 'white' and row < 7) or (color == 'black' and row > 0):
                    # Move one square forward
                    if 0 <= row + direction < 8:
                        moves.append((row + direction, col))
                    # Move two squares forward from the starting row
                    if row == (1 if color == 'white' else 6) and 0 <= row + 2 * direction < 8:
                        moves.append((row + 2 * direction, col))
                pawn_moves[(row, col)] = moves
        return pawn_moves

    def get_game_state(self):
        """Returns the current state of the game, which could be 'Unfinished', ‘White won’, or ‘Black won’"""
        if 'king' in self._white_pieces and 'king' not in self._black_pieces:
            state = 'WHITE_WON'
        elif 'king' in self._black_pieces and 'king' not in self._white_pieces:
            state = 'BLACK_WON'
        else:
            state = 'UNFINISHED'
        return state

    def convert_square_to_location(self, square_moved):
        """Converts a square notation ('a1', 'e4', etc.) to a corresponding (column, row) coordinate on the chessboard.
        It calculates the column by subtracting the ASCII value of the given letter from the ASCII value of 'a',
        and the row by converting the second character to an integer and subtracting 1"""
        column = ord(square_moved[0]) - ord('a')
        row = int(square_moved[1]) - 1
        return (column, row)

    def make_move(self, square_moved_from, square_moved_to):
        """Translates the square notations into coordinates, identifies the piece being moved, verifies the move's
        validity, updates the board if the move is valid, and handles explosions if applicable"""
        if self.get_game_state() == 'BLACK_WON' or self.get_game_state() == 'WHITE_WON':
            return False
        # Converts square notations to coordinates
        from_location = self.convert_square_to_location(square_moved_from)
        to_location = self.convert_square_to_location(square_moved_to)
        # Determine piece being moved based on current turn
        if self._turn == 'white':
            if from_location not in self._white_locations:
                return False
            from_selection = self._white_locations.index(from_location)
            from_piece = self._white_pieces[from_selection]
        else:
            if from_location not in self._black_locations:
                return False
            from_selection = self._black_locations.index(from_location)
            from_piece = self._black_pieces[from_selection]
        # Initializing variable
        to_piece = None

        if from_piece == 'pawn':
            # Gets possible moves for a pawn piece
            moves_list = self.get_pawn_possible_moves(from_location, self._turn)
        elif from_piece == 'rook':
            # Gets possible moves for a rook piece
            moves_list = self.get_rook_possible_moves(from_location, self._turn)
        elif from_piece == 'knight':
            # Gets possible moves for a knight piece
            moves_list = self.get_knight_possible_moves(from_location, self._turn)
        elif from_piece == 'bishop':
            # Gets possible moves for a bishop piece
            moves_list = self.get_bishop_possible_moves(from_location, self._turn)
        elif from_piece == 'queen':
            # Gets possible moves for a queen piece
            moves_list = self.get_queen_possible_moves(from_location, self._turn)
        elif from_piece == 'king':
            # Gets possible moves for a king piece
            moves_list = self.get_king_possible_moves(from_location, self._turn)

        if to_location in moves_list:
            if self._turn == 'white':
                # To check if the destination location contains a black piece
                if to_location in self._black_locations:
                    # Checks if piece being moved is the king
                    if from_piece == "king":
                        return False
                    # Remove pieces from their lists
                    to_selection = self._black_locations.index(to_location)
                    self._white_locations.pop(from_selection)
                    self._white_pieces.pop(from_selection)
                    self._black_locations.pop(to_selection)
                    self._black_pieces.pop(to_selection)
                    # Handles explosion
                    self.explosion_handler(to_location)
                else:
                    # Updates white piece's location
                    self._white_locations[from_selection] = to_location
                # Switches turn to black
                self._turn = 'black'
            else:
                # To check if the destination location contains a white piece
                if to_location in self._white_locations:
                    # Checks if the piece being moved is the king
                    if from_piece == "king":
                        return False
                    # Remove pieces from their lists
                    to_selection = self._white_locations.index(to_location)
                    self._black_locations.pop(from_selection)
                    self._black_pieces.pop(from_selection)
                    self._white_locations.pop(to_selection)
                    self._white_pieces.pop(to_selection)
                    # Handles explosion
                    self.explosion_handler(to_location)
                else:
                    # Updates black piece's location
                    self._black_locations[from_selection] = to_location
                # Switches turn to white
                self._turn = 'white'
            # Checks for game end condition
            if 'king' not in self._white_pieces and 'king' not in self._black_pieces:
                return False
            return True
        else:
            return False

    def get_bishop_possible_moves(self, position, color):
        """Calculates and returns the possible moves for a bishop piece at a given position on the chessboard.
        It iterates over all possible diagonal directions ('se', 'sw', 'ne', 'nw'), determining valid moves until same
        colored pieces are encountered."""
        # Gets possible moves for the bishop from the given position
        moves_list_for_position = self._bishop_possible_moves.get(position)

        # Defines lists of opponent and ally pieces based on the bishop's color
        if color == 'white':
            opponent_list = self._black_locations
            ally_list = self._white_locations
        else:
            ally_list = self._black_locations
            opponent_list = self._white_locations

        result_moves_list = []

        # Iterates over possible diagonal directions
        # South East
        for bishop_position in moves_list_for_position.get('se'):
            # Checks if the position is not occupied by opponent or ally pieces
            if bishop_position not in ally_list and bishop_position not in opponent_list:
                result_moves_list.append(bishop_position)
            else:
                # Valid move if the position is occupied by an opponent piece
                if bishop_position in opponent_list:
                    result_moves_list.append(bishop_position)
                break

        # South West
        for bishop_position in moves_list_for_position.get('sw'):
            # Checks if the position is not occupied by opponent or ally pieces
            if bishop_position not in ally_list and bishop_position not in opponent_list:
                result_moves_list.append(bishop_position)
            else:
                # Valid move if the position is occupied by an opponent piece
                if bishop_position in opponent_list:
                    result_moves_list.append(bishop_position)
                break

        # North East
        for bishop_position in moves_list_for_position.get('ne'):
            # Checks if the position is not occupied by opponent or ally pieces
            if bishop_position not in ally_list and bishop_position not in opponent_list:
                result_moves_list.append(bishop_position)
            else:
                if bishop_position in opponent_list:
                    # Valid move if the position is occupied by an opponent piece
                    result_moves_list.append(bishop_position)
                break

        # North West
        for bishop_position in moves_list_for_position.get('nw'):
            # Checks if the position is not occupied by opponent or ally pieces
            if bishop_position not in ally_list and bishop_position not in opponent_list:
                result_moves_list.append(bishop_position)
            else:
                if bishop_position in opponent_list:
                    # Valid move if the position is occupied by an opponent piece
                    result_moves_list.append(bishop_position)
                break
        return result_moves_list

    def get_rook_possible_moves(self, position, color):
        """Calculates and returns the possible moves for a rook piece at a given position on the chessboard.
        Either moves in the directions of up, down, left, or right, stopping at same-colored pieces. Returns a list
        of tuples that represent the moves"""

        # Get possible moves for the rook from the given position
        moves_list_for_position = self._rook_possible_moves.get(position)

        # Defines lists of opponent and ally pieces based on the rook's color
        if color == 'white':
            opponent_list = self._black_locations
            ally_list = self._white_locations
        else:
            ally_list = self._black_locations
            opponent_list = self._white_locations

        result_moves_list = []

        # Iterate over possible directions
        # UP
        for rook_position in moves_list_for_position.get('up'):
            # Checks if the position is not occupied by ally or opponent pieces
            if rook_position not in ally_list and rook_position not in opponent_list:
                result_moves_list.append(rook_position)
            else:
                # Valid move if the position is occupied by an opponent piece
                if rook_position in opponent_list:
                    result_moves_list.append(rook_position)
                break

        # DOWN
        for rook_position in moves_list_for_position.get('down'):
            # Checks if the position is not occupied by ally or opponent pieces
            if rook_position not in ally_list and rook_position not in opponent_list:
                result_moves_list.append(rook_position)
            else:
                # Valid move if the position is occupied by an opponent piece
                if rook_position in opponent_list:
                    result_moves_list.append(rook_position)
                break

        # LEFT
        for rook_position in moves_list_for_position.get('left'):
            # Checks if the position is not occupied by ally or opponent pieces
            if rook_position not in ally_list and rook_position not in opponent_list:
                result_moves_list.append(rook_position)
            else:
                # Valid move if the position is occupied by an opponent piece
                if rook_position in opponent_list:
                    result_moves_list.append(rook_position)
                break

        # RIGHT
        for rook_position in moves_list_for_position.get('right'):
            # Checks if the position is not occupied by ally or opponent pieces
            if rook_position not in ally_list and rook_position not in opponent_list:
                result_moves_list.append(rook_position)
            else:
                # Valid move if the position is occupied by an opponent piece
                if rook_position in opponent_list:
                    result_moves_list.append(rook_position)
                break
        return result_moves_list

    def get_knight_possible_moves(self, position, color):
        """Calculates and returns the possible moves for a knight piece at a given position on the chessboard. Returns a
         list of tuples that represent the moves"""

        # Gets possible moves for the knight from the given position
        moves_list_for_position = self._knight_possible_moves.get(position)

        # Defines lists of opponent and ally pieces based on the knight's color
        if color == 'white':
            opponent_list = self._black_locations
            ally_list = self._white_locations
        else:
            ally_list = self._black_locations
            opponent_list = self._white_locations

        result_moves_list = []

        for knight_position in moves_list_for_position:
            # Check if the position is not occupied by an ally piece
            if knight_position not in ally_list:
                result_moves_list.append(knight_position)
        return result_moves_list

    def get_queen_possible_moves(self, position, color):
        """Calculates and returns the possible moves for a queen piece at a given position on the chessboard.
        It combines the possible moves of a rook and a bishop from the same position, covering all directions."""

        # Gets possible moves for the queen by combining moves of a bishop and a rook
        moves_list = self.get_bishop_possible_moves(position, color)
        second_list = self.get_rook_possible_moves(position, color)
        for i in range(len(second_list)):
            moves_list.append(second_list[i])
        return moves_list

    def get_king_possible_moves(self, position, color):
        """Calculates and returns the possible moves for a king piece at a given position on the chessboard."""

        # Gets possible moves for the king from the given position
        moves_list_for_position = self._king_possible_moves.get(position)

        # Defines lists of opponent and ally pieces based on the king's color
        if color == 'white':
            opponent_list = self._black_locations
            ally_list = self._white_locations
        else:
            ally_list = self._black_locations
            opponent_list = self._white_locations

        result_moves_list = []

        for king_position in moves_list_for_position:
            # Checks if the position is not occupied by an ally piece
            if king_position not in ally_list:
                result_moves_list.append(king_position)
        return result_moves_list

    def get_pawn_possible_moves(self, position, color):
        """Calculates and returns the possible moves for a pawn piece at a given position on the chessboard.
        It checks for valid pawn moves, including forward moves, captures, and double moves on
        the initial pawn placement. Returns a list of tuples that represent the moves"""
        result_moves_list = []
        if color == 'white':
            moves_list_for_position = self._white_pawn_possible_moves.get(position)
            opponent_list = self._black_locations
            ally_list = self._white_locations

            # Checks for double move on initial pawn placement and forward moves
            if (position[0], position[1] + 2) not in self._white_locations and \
                    (position[0], position[1] + 1) not in self._white_locations and \
                    (position[0], position[1] + 1) not in self._black_locations and \
                    (position[0], position[1] + 2) not in self._black_locations and position[1] == 1:
                result_moves_list.append((position[0], position[1] + 2))
            # Checks for captures
            if (position[0] + 1, position[1] + 1) in self._black_locations:
                result_moves_list.append((position[0] + 1, position[1] + 1))
            if (position[0] - 1, position[1] + 1) in self._black_locations:
                result_moves_list.append((position[0] - 1, position[1] + 1))
        else:
            moves_list_for_position = self._black_pawn_possible_moves.get(position)
            ally_list = self._black_locations
            opponent_list = self._white_locations
            # Checks for double move on initial pawn placement and forward moves
            if (position[0], position[1] - 2) not in self._white_locations and \
                    (position[0], position[1] - 1) not in self._white_locations and \
                    (position[0], position[1] - 1) not in self._black_locations and \
                    (position[0], position[1] - 2) not in self._black_locations and position[1] == 6:
                result_moves_list.append((position[0], position[1] - 2))
            # Checks for captures
            if (position[0] + 1, position[1] - 1) in self._white_locations:
                result_moves_list.append((position[0] + 1, position[1] - 1))
            if (position[0] - 1, position[1] - 1) in self._white_locations:
                result_moves_list.append((position[0] - 1, position[1] - 1))

        for pawn_position in moves_list_for_position:
            # Checks if the position is not occupied by ally or opponent pieces
            if pawn_position not in ally_list and pawn_position not in opponent_list:
                result_moves_list.append(pawn_position)
        return result_moves_list

    def explosion_handler(self, location):
        """Handles the explosion event caused by a piece. Removes surrounding pieces based on the explosion."""

        # Gets surrounding squares affected by the explosion
        explosive_squares = self.get_surrounding_squares(location)

        # Iterates over explosive squares
        for piece_coordinates in explosive_squares:
            # Checks if the square contains a white piece
            if piece_coordinates in self._white_locations:
                selection = self._white_locations.index(piece_coordinates)
                # Checks if the piece is not a pawn
                if self._white_pieces[selection] != 'pawn':
                    # Removal of piece from the board
                    self._white_locations.pop(selection)
                    self._white_pieces.pop(selection)
            # Checks if the square contains a black piece
            elif piece_coordinates in self._black_locations:
                selection = self._black_locations.index(piece_coordinates)
                # Checks if the piece is not a pawn
                if self._black_pieces[selection] != 'pawn':
                    # Removal of piece from the board
                    self._black_locations.pop(selection)
                    self._black_pieces.pop(selection)

    def get_surrounding_squares(self, position):
        """Calculates the coordinates of adjacent squares (up, down, left, right, and diagonal) around the
        given position, ensuring they are within the board boundaries. Returns a list of the surrounding squares"""
        surrounding_squares_list = []

        # Defines directions for surrounding squares
        targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]

        # Iterate over directions to calculate surrounding squares
        for i in range(8):
            target = (position[0] + targets[i][0], position[1] + targets[i][1])
            # Checks if target square is within board boundaries
            if 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
                surrounding_squares_list.append(target)
        return surrounding_squares_list

    def print_board(self):
        """Prints the current state of the chessboard, representing the pieces as characters."""
        # Initialize an 8x8 board
        board = [[' ' for _ in range(8)] for _ in range(8)]

        # White pieces on the board
        for i in range(len(self._white_locations)):
            piece = self._white_pieces[i]
            x, y = self._white_locations[i]
            # Displays knight piece in uppercase
            if piece == "knight":
                board[7 - y][x] = piece[1].upper()
            else:
                board[7 - y][x] = piece[0].upper()

        # Black pieces on the board
        for i in range(len(self._black_locations)):
            piece = self._black_pieces[i]
            x, y = self._black_locations[i]
            # Displays knight piece in lowercase
            if piece == "knight":
                board[7 - y][x] = piece[1]
            else:
                board[7 - y][x] = piece[0]
        # Prints board
        for row in board:
            print(' '.join(row))
