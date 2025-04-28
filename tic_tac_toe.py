import random

def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("-----------")

def check_winner(board):
    # Baris
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return board[i]
    
    # Kolom
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    
    # Diagonal
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]
    
    # Cek seri
    if " " not in board:
        return "Seri"
    
    return None

def player_move(board):
    while True:
        try:
            move = int(input("Pilih posisi (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            else:
                print("Posisi tidak valid atau sudah terisi!")
        except ValueError:
            print("Masukkan angka antara 1-9!")

def computer_move(board):
    # Cari posisi kosong
    empty_positions = [i for i, spot in enumerate(board) if spot == " "]
    return random.choice(empty_positions)

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"  # X adalah pemain, O adalah komputer
    
    print("Selamat bermain Tic Tac Toe!")
    print("Posisi papan:")
    print_board([str(i+1) for i in range(9)])
    print("\nAnda adalah X, komputer adalah O")
    
    while True:
        print("\nPapan saat ini:")
        print_board(board)
        
        if current_player == "X":
            move = player_move(board)
        else:
            print("\nKomputer berpikir...")
            move = computer_move(board)
        
        board[move] = current_player
        
        winner = check_winner(board)
        if winner:
            print("\nPapan akhir:")
            print_board(board)
            if winner == "Seri":
                print("\nHasil: Seri!")
            elif winner == "X":
                print("\nSelamat! Anda menang!")
            else:
                print("\nAnda kalah! Komputer menang.")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        play_again = input("\nMain lagi? (y/n): ").lower()
        if play_again != 'y':
            print("Terima kasih telah bermain!")
            break
