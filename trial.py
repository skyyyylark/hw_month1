plane = [
    ["*", "*", "*"],
    ["*", "*", "*"],
    ["*", "*", "*"],
]





def print_plane():
    for i in range(3):
        row = plane[i]
        print(f"{row[0]} | {row[1]} | {row[2]}")
        if i != 2:
            print("-" * 9)
def check():
    win = True
    player1 = input("Give your name (1st player): ")
    player2 = input("Give your name (2nd player): ")

    while win:

        player_1_x, player_1_y = int(input()) - 1, int(input()) - 1
        plane[player_1_x][player_1_y] = "x"
        print_plane()
        player_2_x, player_2_y = int(input()) - 1, int(input()) - 1
        plane[player_2_x][player_2_y] = "0"
        print_plane()


        for i in plane:
            if i[0] == i[1] == i[2] == "x":
                winner = "x"
                win = False
                break

            elif i[0] == i[1] == i[2] == "0":
                winner = "0"
                win = False
                break
            l = []
            for i in range(3):
                 for k in range(3):
                     l.append(plane[k][i])
                     if l.count("0") == 3 or l.count("x") == 3:
                         winner = l[0]
                         win = False
                 l.clear()
        row1 = plane[0]
        row2 = plane[1]
        row3 = plane[2]
        if row1[0] == row2[1] == row3[2] == "x" or row1[0] == row2[1] == row3[2] == "0":
            winner = row1[0]
            win = False
        elif row1[2] == row2[1] == row3[0] == "x" or row1[2] == row2[1] == row3[0] == "0":
            winner = row1[2]
            win = False
        list = []

        for i in range(3):
            for k in range(3):
                list.append(plane[k][i])
        num = list.count("*")
        if num == 0:
            winner = "tie"
            win = False

    if winner == "x":
        winner = player1
    elif winner == "0":
        winner == player2
    with open("./winner.txt", 'a+', encoding = "UTF-8"):
        if winner == "tie":
            file.write(f"{player1} | {player2} | no winner, it is a {winner} \n ")
        else:
            file.write(f"{player1} | {player2} | winner is {winner} \n ")
    print(winner)

check()