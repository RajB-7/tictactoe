import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(master, text=" ", width=10, height=3,
                                    command=lambda i=i, j=j: self.button_click(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

    def button_click(self, i, j):
        if self.board[i][j] == " ":
            self.buttons[i][j].config(text=self.current_player)
            self.board[i][j] = self.current_player

            if self.check_win():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_board()
            else:
                self.switch_player()

    def check_win(self):
        # Check rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
        # Check columns
        for j in range(3):
            if self.board[0][j] == self.board[1][j] == self.board[2][j] != " ":
                return True
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != " " or
            self.board[0][2] == self.board[1][1] == self.board[2][0] != " "):
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True

    def switch_player(self):
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")
                self.board[i][j] = " "

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()