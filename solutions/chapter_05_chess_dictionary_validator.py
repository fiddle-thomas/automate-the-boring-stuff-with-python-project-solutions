def is_valid_chessboard(chess_board: dict):
    # Dictionary to store the count of each piece on the board
    moved_board = {}
    # Dictionary defining valid piece names and their maximum allowed count
    valid_board = {
        "bpawn": 8, "wpawn": 8,
        "bknight": 2, "wknight": 2,
        "bbishop": 2, "wbishop": 2,
        "brook": 2, "wrook": 2,
        "bqueen": 1, "wqueen": 1,
        "bking": 1, "wking": 1
    }
    
    # Check if the board is empty
    if not chess_board:
        return False
    
    # Check if both kings are present
    if "bking" not in chess_board.values() or "wking" not in chess_board.values():
        return False

    # Validate board positions and piece names, and count the pieces
    for key, value in chess_board.items():
        if len(key) == 2 and key.startswith(("1", "2", "3", "4", "5", "6", "7", "8")) and key.endswith(("a", "b", "c", "d", "e", "f", "g", "h")):
            if value in valid_board.keys():
                moved_board.setdefault(value, 0)
                moved_board[value] += 1
            else:
                return False
        else:
            return False

    # Check if the number of each piece is within the allowed limit
    for key in moved_board.keys():
        if moved_board[key] > valid_board[key]:
            return False
    
    return True

# Test cases
if __name__ == "__main__":    
    # No black king, but white king present
    print(is_valid_chessboard({'1a': 'wking', '2b': 'bqueen', '3c': 'bpawn'}))  # Should return False

    # No white king, but black king present
    print(is_valid_chessboard({'1a': 'bking', '2b': 'wqueen', '3c': 'wpawn'}))  # Should return False

    # No kings at all
    print(is_valid_chessboard({'1a': 'bqueen', '2b': 'wqueen', '3c': 'bpawn'}))  # Should return False

    # Both kings present (valid case)
    print(is_valid_chessboard({'1a': 'bking', '8h': 'wking', '2b': 'bqueen', '7g': 'wqueen'}))  # Should return True

    # More than one black king
    print(is_valid_chessboard({'1a': 'bking', '2b': 'bking', '8h': 'wking'}))  # Should return False

    # More than one white king
    print(is_valid_chessboard({'1a': 'bking', '7g': 'wking', '8h': 'wking'}))  # Should return False

    # Too many pieces for one player (>16)
    print(is_valid_chessboard({
        '1a': 'bking', '1b': 'bqueen', '1c': 'brook', '1d': 'brook', '1e': 'bbishop', '1f': 'bbishop', '1g': 'bknight', '1h': 'bknight',
        '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
        '3a': 'bpawn',
        '8h': 'wking'
    }))  # Should return False

    # Too many pawns (>8)
    print(is_valid_chessboard({
        '1a': 'bking', '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn', '3a': 'bpawn',
        '8h': 'wking'
    }))  # Should return False

    # Invalid board position
    print(is_valid_chessboard({'1a': 'bking', '8h': 'wking', '9z': 'bpawn'}))  # Should return False

    # Invalid piece name
    print(is_valid_chessboard({'1a': 'bking', '8h': 'wking', '2a': 'bpony'}))  # Should return False

    # Empty board
    print(is_valid_chessboard({}))  # Should return False

    # Valid board with minimum pieces
    print(is_valid_chessboard({'1a': 'bking', '8h': 'wking'}))  # Should return True

    # Valid board with all pieces in starting position
    print(is_valid_chessboard({
        '1a': 'brook', '1b': 'bknight', '1c': 'bbishop', '1d': 'bqueen', '1e': 'bking', '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
        '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
        '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
        '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking', '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook'
    }))  # Should return True
