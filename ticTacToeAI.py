from tkinter import *
import tkinter as tk

bestR = -1
bestC = -1
bestValue = -10


def minimax(ismax, depth, f, alpha, beta):
    global bestR
    global bestC
    global bestValue
    result = check_winner_for_minimax()
    if result != 1 or depth == 0:
        return result
    if ismax:                 # maximizing
        maxfinalscore = -10
        for ro in range(3):
            for co in range(3):
                if game_btns[ro][co]['text'] == "":
                    game_btns[ro][co]['text'] = "o"
                    score = minimax(False, depth - 1, 0, alpha, beta)
                    game_btns[ro][co]['text'] = ""
                    if f:
                        if score > bestValue:
                            bestValue = score
                            bestR = ro
                            bestC = co
                    if score > maxfinalscore:
                        maxfinalscore = score
                    if score > alpha:
                        alpha = score
                    if alpha >= beta:
                        return maxfinalscore

        return maxfinalscore
    else:            # minimizing
        finalscore = 10
        for roo in range(3):
            for coo in range(3):
                if game_btns[roo][coo]['text'] == "":
                    game_btns[roo][coo]['text'] = "x"
                    score = minimax(True, depth - 1, 0, alpha, beta)
                    game_btns[roo][coo]['text'] = ""
                    if score < finalscore:
                        finalscore = score
                    if score < beta:
                        beta = score
                    if alpha >= beta:
                        return finalscore
        return finalscore


def next_turn(row, col):
    global player
    global bestR
    global bestC
    global bestValue
    if game_btns[row][col]['text'] == "" and check_winner() == 1:
        game_btns[row][col]['text'] = player
        if check_winner() == 1:
            player = players[1]  ## o (Ai)
            label.config(text=(players[1] + " turn" + ' ( Wait )'))
            window.update()
            minimax(1, 8, 1, -10, 10)
            game_btns[bestR][bestC]['text'] = 'o'
            bestValue = -10   # the initial value for the next turn
            bestR = -1
            bestC = -1
            if check_winner() == 1:
                player = players[0]   ## x (player)
                label.config(text=(players[0] + " turn"))
            elif check_winner() == 2:  
                label.config(text=(players[1] + " wins!")) ##o win Ai 
            elif check_winner() == 0:
                label.config(text=("Tie, No Winner!"))
        elif check_winner() == -2:
            label.config(text=(players[0] + " wins!")) ##x win Player
        elif check_winner() == 0:
            label.config(text=("Tie, No Winner!"))


def check_winner():
    # check all 3 horizontal conditions
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] == "x":
            game_btns[row][0].config(bg="green")
            game_btns[row][1].config(bg="green")
            game_btns[row][2].config(bg="green")
            return -2
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] == "o":
            game_btns[row][0].config(bg="light green")
            game_btns[row][1].config(bg="light green")
            game_btns[row][2].config(bg="light green")
            return 2
    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] == "x":
            game_btns[0][col].config(bg="green")
            game_btns[1][col].config(bg="green")
            game_btns[2][col].config(bg="green")
            return -2
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] == "o":
            game_btns[0][col].config(bg="light green")
            game_btns[1][col].config(bg="light green")
            game_btns[2][col].config(bg="light green")
            return 2
    # check diagonals conditions
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] == "x":
        game_btns[0][0].config(bg="green")
        game_btns[1][1].config(bg="green")
        game_btns[2][2].config(bg="green")
        return -2
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] == "o":
        game_btns[0][0].config(bg="light green")
        game_btns[1][1].config(bg="light green")
        game_btns[2][2].config(bg="light green")
        return 2
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] == "x":
        game_btns[0][2].config(bg="green")
        game_btns[1][1].config(bg="green")
        game_btns[2][0].config(bg="green")
        return -2
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] == "o":
        game_btns[0][2].config(bg="light green")
        game_btns[1][1].config(bg="light green")
        game_btns[2][0].config(bg="light green")
        return 2

    # if there are no empty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                game_btns[row][col].config(bg='red')
        return 0              # tie

    else:
        return 1             # continue the game


def check_winner_for_minimax():
    # check all 3 horizontal conditions
    for row in range(3):
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] == "x":
            return -2
        if game_btns[row][0]['text'] == game_btns[row][1]['text'] == game_btns[row][2]['text'] == "o":
            return 2
    # check all 3 vertical conditions
    for col in range(3):
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] == "x":
            return -2
        if game_btns[0][col]['text'] == game_btns[1][col]['text'] == game_btns[2][col]['text'] == "o":
            return 2
    # check diagonals conditions
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] == "x":
        return -2
    if game_btns[0][0]['text'] == game_btns[1][1]['text'] == game_btns[2][2]['text'] == "o":
        return 2
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] == "x":
        return -2
    elif game_btns[0][2]['text'] == game_btns[1][1]['text'] == game_btns[2][0]['text'] == "o":
        return 2

    # if there are no empty spaces left
    if check_empty_spaces() == False:
        return 0

    else:
        return 1


def check_empty_spaces():
    spaces = 9
    for row in range(3):
        for col in range(3):
            if game_btns[row][col]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def start_new_game():
    global player
    player = players[0]
    label.config(text=(player + " turn"))
    for row in range(3):
        for col in range(3):
            game_btns[row][col].config(text="", bg="#FFF5E1",fg='#8B4513',highlightbackground="#FFF5E1")


window = tk.Tk()
window.title("Tic Tac Toe")
window.configure(bg="#FFF5E1")  ##creme

ourMessage = "Good luck, but the AI doesn't believe in luck."
messageVar = Message(window, text=ourMessage,justify="left")
messageVar.config(bg='#8B4513',fg='#D2B48C') ## brown , beige
messageVar.pack(fill=tk.X)

players = ["x", "o"]
player = players[0]

game_btns = [
    ["x", "o", "x"],
    ["o", "", ""],
    ["x", "o", "x"]
]

label = Label(text=(player + " turn"), font=('consolas', 40),bg="#D2B48C",
    fg="#8B4513" )
label.pack(side="top")

restart_btn = Button(text="restart",
    font=('consolas', 20),
    command=start_new_game ,
    activebackground="#D2B48C",
    activeforeground="#8B4513",  
    bg="#8B4513",
    fg="#FFF5E1"  )
restart_btn.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()
for r in range(3):
    for c in range(3):
        game_btns[r][c] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,bg="#FFF5E1",fg='#8B4513',borderwidth=1,
                                    relief="raised",  
                                    highlightbackground="#FFF5E1", 
                                    highlightcolor="#8B4513",
                                 command=lambda row=r, col=c: next_turn(row, col))
        game_btns[r][c].grid(row=r, column=c)
window.mainloop()
