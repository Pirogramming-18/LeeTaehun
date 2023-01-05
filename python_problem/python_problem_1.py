num = 0

inputNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
validInput = [1, 2, 3]

while(True):
  if not str.isdigit(inputNum):
    print("정수를 입력하세요")
    inputNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
  elif int(inputNum) not in validInput:
    print("1,2,3 중 하나를 입력하세요")
    inputNum = input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력가능) :")
  else:
    break
print(inputNum)

