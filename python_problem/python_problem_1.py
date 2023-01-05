num = 0
endGame = False
validInput = [1, 2, 3]
playerName = ["playerA", "playerB"]

def brGame(playerNum):
  global num
  global endGame
  inputNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")

  while(True):
    if not str.isdigit(inputNum):
      print("정수를 입력하세요")
      inputNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
    elif int(inputNum) not in validInput:
      print("1,2,3 중 하나를 입력하세요")
      inputNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
    else:
      inputNum = int(inputNum)
      break

  for i in range(inputNum):

    num += 1
    print(f"{playerName[playerNum]}: {num}")
    if num == 31:
      endGame = True
      break
  if endGame:
    print(f"{playerName[1-playerNum]} win!")

while not endGame:
  brGame(0)
  if endGame:
    break
  brGame(1)
  