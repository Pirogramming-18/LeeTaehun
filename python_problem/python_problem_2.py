
studentInformation = dict()

  #############  menu 1
def Menu1(inputList):
    #사전에 학생 정보 저장하는 코딩 
  global studentInformation
  if len(inputList) != 3:   # data number is not 3
    print("Number of data is not 3!")
  elif inputList[0] in studentInformation:  # student name already exist
    print("Already exist name!")
  elif not (str.isdigit(inputList[1]) and str.isdigit(inputList[2])):  # score is not intger
    print("Score is not positive integer!")
  elif int(inputList[1]) <= 0 or int(inputList[2]) <=0:  # score is not positive
    print("Score is not positive integer!")
  else:                                                                        # add a key and value pair to dictionary
    studentInformation[inputList[0]] = [int(inputList[1]), int(inputList[2])]  # key : name, value : [mid-score, final-score]
    
##############  menu 2
def Menu2():
    #학점 부여 하는 코딩
    grade = ""
    if not studentInformation:  # there is no student data
      print("No student data!")
    else:
      for key in studentInformation:   
        if len(studentInformation[key]) == 2:   # student not graded yet
          # grading
          meanScore = (studentInformation[key][0] +studentInformation[key][1])/2
          if meanScore >= 90:
            grade = "A"
          elif meanScore >= 80:
            grade = "B"
          elif meanScore >= 70:
            grade = "C"
          else:
            grade = "D"
          studentInformation[key].append(grade) # now value is [mid-score, final-score, grade]
      print("Grading to all students.")
      

##############  menu 3
def Menu3():
    #출력 코딩
    allGradingComplete = True
    if not studentInformation:  #there is no student data
      print("No student data!")
    else:
      for key in studentInformation:
        if len(studentInformation[key]) != 3:  # there is student data not graded yet
          allGradingComplete = False
      if not allGradingComplete: #not all graded case
        print("There is a student who didn't get grade.")
      elif allGradingComplete:   #all graded case
        print()
        print("--------------------------------")
        print("name      mid    final    grade")
        print("--------------------------------")
        for key2 in studentInformation:
          print(f"{key2:<10}{studentInformation[key2][0]:>3}{studentInformation[key2][1]:>9}{studentInformation[key2][2]:>9}")

##############  menu 4
def Menu4():
    #학생 정보 삭제하는 코딩
    if not studentInformation:  #there is no student data
      print("No student data!")
    else:
      name = input("Enter the name to delete : ")
      if name not in studentInformation:  #there is no student name to delete
        print("Not exist name!")
      else:                               #delete the student information
        del studentInformation[name]
        print(f"{name} student information is deleted.")


#학생 정보를 저장할 변수 초기화

print(not str.isdigit("34.5"))
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출
        inputList = input("Enter name mid-score final-score : ").split()
        Menu1(inputList)

        
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        Menu2()

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        Menu3()

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        Menu4()
    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit Program!")
        break

    else :
        print("Wrong number. Choose again.")