
draw_tile = {
  -1: "O",
  0: " ",
  1: "X",
}

def draw_board(board):
  t = [draw_tile[player] for player in board]
  print("   l  m  r")
  print(f"t {t[0]} | {t[1]} | {t[2]} ")
  print("  —————————")
  print(f"m {t[3]} | {t[4]} | {t[5]} ")
  print("  —————————")
  print(f"b {t[6]} | {t[7]} | {t[8]} ")

from_row = {
  "t": 0,
  "m": 1,
  "b": 2,
}

from_col = {
  "l": 0,
  "m": 1,
  "r": 2,
}

def splitter(a):
  row = from_row[a[0]]
  col = from_col[a[1]]
  index = col + (3 * row)
  return index

def update_board(board, index, player):
  if board[index] == 0:
    board[index] = player
    return board
  # this is an invalid move!
  return None

def build_check(board):
  to_check = []
  for row in range(3):
    to_check.append(board[3*row:3*row+3])
  for col in range(3):
    to_check.append(board[col:col+9:3])
  to_check.append(board[0:9:4])
  to_check.append(board[2:7:2])
  return to_check

def three_in_a_row(board):
  to_check = build_check(board)

  for check in to_check:
    if abs(sum(check)) == 3:
      return True

  return False
  

  
board = [0 for _ in range(9)]
player = 1

for _ in range(9):
  draw_board(board)

  # asking the player for a move until they make a valid move
  while True:
    answer = input("Where would you like to go? ")
    index = splitter(answer)
    maybe_new_board = update_board(board, index, player)
    if board is not None:
      board = maybe_new_board
      break

  # winning
  if three_in_a_row(board):
    print("The winner is", player)
    break
  # switching turns
  player *= -1

print("It's a draw!")
