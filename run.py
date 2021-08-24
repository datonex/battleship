grid_size = 9
board = [['.'] * grid_size for i in range(grid_size)]

# def print_board(board_in):
#     for row in board_in:
#         if row[0]:
#             for i in row[0]:
#                 i = 1
#                 i += 1
#                 print(i)
#             #print(row[0]) 
#         #print(" ".join(row))

def print_board(board_in):
    print("\n  " + " ".join(str(i) for i in range(1, grid_size + 1)))
    for i in range(grid_size):
        print(str(i + 1) + " " + " ".join(str(i) for i in board_in[i]))
    print()
            
print_board(board)


