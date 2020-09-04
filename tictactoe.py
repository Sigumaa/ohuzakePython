the_board = {
	"top-L":" ","top-M":" ","top-R":" ",
	"mid-L":" ","mid-M":" ","mid-R":" ",
	"low-L":" ","low-M":" ","low-R":" ",
}


def print_board(board):
	print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
	print("-+-+-")
	print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
	print("-+-+-")
	print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"] + "\n")


turn = "X"
for i in range(9):
	print_board(the_board)
	print(turn + "の番です。どこに打つ？\n左上:top-L、上:top-M、右上:top-R\n中段、下段は同様に、中段の場合はtopのところをmidに、下段の場合はtopのところをlowに変えてください\n")
	move = input()
	the_board[move] = turn
	if turn == "X":
		turn = "O"
	else:
		turn = "X"


print_board(the_board)

end = input()