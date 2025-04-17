import time, math, random, os, sys
from typing import Dict

def BMICalculator() -> None:
  height: float = float(input("Enter your height in cm: "))
  weight: float = float(input("Enter your weight in kg: "))
  slow_type("Your BMI is", weight / (height/100)**2 , ".")

def gradeCalculator() -> None:
  time.sleep(0.5)
  CorrectMarks: int = int(input("How many marks did you get? "))
  time.sleep(0.5)
  TotalMarks: int = int(input("How many marks were there? "))
  time.sleep(0.5) 
  percentage: float = CorrectMarks * 100 / TotalMarks
  time.sleep(0.5)
  if(percentage <= 100):
    time.sleep(0.5)
    slow_type("You got " + str(percentage) +"%")
    if (percentage >= 90):
        slow_type("You got an A.")
        time.sleep(0.5)
        slow_type("You passed.")
    elif (percentage >= 80):
        slow_type("You got a B.")
        time.sleep(0.5)
        slow_type("You passed.")
    elif (percentage >= 70):
        slow_type("You got a C.")
        time.sleep(0.5)
        slow_type("You passed.")
    elif (percentage >= 60):
        slow_type("You got a D.")
        time.sleep(0.5)
        slow_type("You passed.")
    elif (percentage >= 50):
        slow_type("You got an E.")
        time.sleep(0.5)
        slow_type("You failed the exam.")
    else:
        slow_type("You got an F.")
        time.sleep(0.5)
        slow_type("You failed the exam.")
  else:
      slow_type("Stop lying.")
  time.sleep(0.5)

def Calculate() -> None:
  Numbertimes: int = int(input("How many times should I repeat? "))
  Counter: int = 1
  while (Numbertimes >= Counter):
      Counter = Counter + 1
      slow_type("You can use '+ ,- ,* ,/ ,** ,nroot ,% ,log ,sin ,cos ,tan' as operators.")
      Operator: str = input("What's the operator? ")
      Number1: float = float(input("What is the first input number? "))
      if Operator == "log":
        print(math.log(Number1))
        continue
      elif Operator == "sin":
        print(math.sin(Number1))
        continue
      elif Operator == "cos":
        print(math.cos(Number1))
        continue
      elif Operator == "tan":
        print(math.tan(Number1))
        continue
      Number2: float = float(input("What is the second input number? "))
      if (Operator == "+"):
          print(Number1 + Number2)
      elif (Operator == "-"):
          print(Number1 - Number2)
      elif (Operator == "*"):
          print(Number1 * Number2)
      elif (Operator == "/"): 
        if (Number2 == 0):
          print ("answer is indeterminated.")
        else:
          print(Number1 / Number2)
      elif (Operator == "**"):
        print (Number1 ** Number2)
      elif (Operator == "nroot"):
        print (Number1 ** (1/Number2))
      elif (Operator == "%"):
        print (str(Number1 / Number2 * 100) + " %")
      else:
        print ('invalid input')

def Wordle() -> None:
  Clearconsole()
  list = []
  with open('Python\phone\words.txt', 'r') as file:
    for word in file:
      list.append(word.replace("\n", ""))
  hidden_word = random.choice(list)
  attempt = 5
  while attempt >= 0:
    guess = str(input("\n Guess the word: "))
    if guess == hidden_word:
      slow_type("You got it right.")
      slow_type("Congratulations, you just killed this program.")
      slow_type("Program dying...")
      time.sleep(3)
      exit()
    else:
      attempt = attempt - 1
      slow_type(f"you have {attempt} attempt(s)")
      for char, word in zip(hidden_word, guess):
        if word in hidden_word and word in char:
          slow_type(" ✅ ",end="")
        elif word in hidden_word:
          slow_type(" ➕ ",end="")
        else:
          slow_type(" ❌ ",end="")
    if attempt == 0:
      slow_type(" Game over !!!! ")
      slow_type("The word was", hidden_word + ".")
      slow_type("Noob!")
      time.sleep(3)
      exit()

def TicTacToe() -> None:
  start: str = input("Do you want to play against another player or againts a bot? p for player and b for bot ")
  def resetBoard() -> None:
    global board
    board: Dict[int, str] = {1: ' ' , 2: ' ' , 3: ' ' ,4: ' ' , 5: ' ' , 6: ' ' ,7: ' ' , 8: ' ' , 9: ' ' }
  def printBoard() -> None:
    slow_type(board[1] + '|' + board[2] + '|' + board[3] + "\n" + "-+-+-" + "\n" + board[4] + '|' + board[5] + '|' + board[6] + "\n" + "-+-+-" + "\n" + board[7] + '|' + board[8] + '|' + board[9])
  def playAgain() -> int:
    playAgain: str = input("Do you want to play again? ")
    if (playAgain == "yes"):
      global start
      start: str = input("Do you want to play against another player or againts a bot? p for player and b for bot ")
      game()
    elif (playAgain == "no"):
      return 0
    else:
      while (playAgain != "yes" or playAgain != "no"):
        slow_type("You have to type either yes or no")
        playAgain = input("So do you want to play again? ")
        if (playAgain == "yes"):
          game()
        elif (playAgain == "no"):
          return 0
  def compMove() -> int:
    move: int = 5
    if(board[5] == " "):
      move = 5
    elif(board[5] == board[9] == "o" and board[1] == " "):#win or stop loss
      move = 1
    elif(board[2] == board[3] == "o" and board[1] == " "):#win or stop loss
      move = 1
    elif(board[4] == board[7] == "o" and board[1] == " "):#win or stop loss
      move = 1
    elif(board[1] == board[3] == "o" and board[2] == " "):#win or stop loss
      move = 2
    elif(board[5] == board[8] == "o" and board[2] == " "):#win or stop loss
      move = 2
    elif(board[1] == board[2] == "o" and board[3] == " "):#win or stop loss
      move = 3
    elif(board[6] == board[9] == "o" and board[3] == " "):#win or stop loss
      move = 3
    elif(board[5] == board[7] == "o" and board[3] == " "):#win or stop loss
      move = 3
    elif(board[1] == board[7] == "o" and board[4] == " "):#win or stop loss
      move = 4
    elif(board[5] == board[6] == "o" and board[4] == " "):#win or stop loss
      move = 4
    elif(board[4] == board[6] == "o" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[1] == board[9] == "o" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[3] == board[7] == "o" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[2] == board[8] == "o" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[4] == board[5] == "o" and board[6] == " "):#win or stop loss
      move = 6
    elif(board[3] == board[9] == "o" and board[6] == " "):#win or stop loss
      move = 6
    elif(board[3] == board[5] == "o" and board[7] == " "):#win or stop loss
      move = 7
    elif(board[1] == board[4] == "o" and board[7] == " "):#win or stop loss
      move = 7
    elif(board[8] == board[9] == "o" and board[7] == " "):#win or stop loss
      move = 7
    elif(board[2] == board[5] == "o" and board[8] == " "):#win or stop loss
      move = 8
    elif(board[7] == board[9] == "o" and board[8] == " "):#win or stop loss
      move = 8
    elif(board[7] == board[8] == "o" and board[9] == " "):#win or stop loss
      move = 9
    elif(board[1] == board[5] == "o" and board[9] == " "):#win or stop loss
      move = 9
    elif(board[3] == board[6] == "o" and board[9] == " "):#win or stop loss
      move = 9
    elif(board[5] == board[9] == "x" and board[1] == " "):#win or stop loss
      move = 1
    elif(board[2] == board[3] == "x" and board[1] == " "):#win or stop loss
      move = 1
    elif(board[4] == board[7] == "x" and board[1] == " "):#win or stop loss
      move = 1
    elif(board[1] == board[3] == "x" and board[2] == " "):#win or stop loss
      move = 2
    elif(board[5] == board[8] == "o" and board[2] == " "):#win or stop loss
      move = 2
    elif(board[1] == board[2] == "x" and board[3] == " "):#win or stop loss
      move = 3
    elif(board[6] == board[9] == "x" and board[3] == " "):#win or stop loss
      move = 3
    elif(board[5] == board[7] == "x" and board[3] == " "):#win or stop loss
      move = 3
    elif(board[1] == board[7] == "x" and board[4] == " "):#win or stop loss
      move = 4
    elif(board[5] == board[6] == "x" and board[4] == " "):#win or stop loss
      move = 4
    elif(board[4] == board[6] == "x" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[1] == board[9] == "x" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[3] == board[7] == "x" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[2] == board[8] == "x" and board[5] == " "):#win or stop loss
      move = 5
    elif(board[4] == board[5] == "x" and board[6] == " "):#win or stop loss
      move = 6
    elif(board[3] == board[9] == "x" and board[6] == " "):#win or stop loss
      move = 6
    elif(board[3] == board[5] == "x" and board[7] == " "):#win or stop loss
      move = 7
    elif(board[1] == board[4] == "x" and board[7] == " "):#win or stop loss
      move = 7
    elif(board[8] == board[9] == "x" and board[7] == " "):#win or stop loss
      move = 7
    elif(board[2] == board[5] == "x" and board[8] == " "):#win or stop loss
      move = 8
    elif(board[7] == board[9] == "x" and board[8] == " "):#win or stop loss
      move = 8
    elif(board[7] == board[8] == "x" and board[9] == " "):#win or stop loss
      move = 9
    elif(board[1] == board[5] == "x" and board[9] == " "):#win or stop loss
      move = 9
    elif(board[3] == board[6] == "x" and board[9] == " "):#win or stop loss
      move = 9
    elif(board[1] == board[9] == "x" and board[5] == "o" and board[2] == " "):#stop getting double attacked
      move = 2
    elif(board[3] == board[7] == "x" and board[5] == "o" and board[2] == " "):#stop getting double attacked
      move = 2
    elif(board[1] == board[6] == "x" and board[5] == "o" and board[2] == " "):#stop getting double attacked
      move = 2
    elif(board[3] == board[4] == "x" and board[5] == "o" and board[2] == " "):#stop getting double attacked
      move = 2
    elif(board[3] == board[8] == "x" and board[5] == "o" and board[4] == " "):#stop getting double attacked
      move = 4
    elif(board[2] == board[9] == "x" and board[5] == "o" and board[4] == " "):#stop getting double attacked
      move = 4
    elif(board[2] == board[7] == "x" and board[5] == "o" and board[6] == " "):#stop getting double attacked
      move = 6
    elif(board[1] == board[8] == "x" and board[5] == "o" and board[6] == " "):#stop getting double attacked
      move = 6
    elif(board[1] == board[6] == board[8] == "x" and board[5] == board[2] == "o" and board[7] == " "):#stop getting double attacked 2
      move = 7
    elif(board[1] == board[8] == board[9] == "x" and board[5] == board[2] == "o" and board[7] == " "):#stop getting double attacked 2
      move = 7
    elif(board[6] == board[7] == "x" and board[5] == "o" and board[8] == " "):#stop getting double attacked
      move = 8
    elif(board[9] == board[4] == "x" and board[5] == "o" and board[8] == " "):#stop getting double attacked
      move = 8
    elif(board[3] == board[4] == board[8] == "x" and board[5] == board[2] == "o" and board[9] == " "):#stop getting double attacked 2
      move = 9
    elif(board[6] == board[8] == "x" and board[5] == "o" and board[9] == " "):#stop getting double attacked
      move = 9
    elif board[1] == " ":#corner
      move = 1
    elif board[3] == " ":#corner
      move = 3
    elif board[7] == " ":#corner
      move = 7
    elif board[9] == " ":#corner
      move = 9
    elif board[2] == " ":#edge
      move = 2
    elif board[4] == " ":#edge
      move = 4
    elif board[6] == " ":#edge
      move = 6
    elif board[8] == " ":#edge
      move = 8
    return move
  def gameOver() -> None:
    if count >= 5 and count != 9 :
      if (board[7] == board[8] == board[9] != ' ' or board[4] == board[5] == board[6] != ' ' or board[1] == board[2] == board[3] != ' ' or board[1] == board[4] == board[7] != ' ' or board[2] == board[5] == board[8] != ' ' or board[3] == board[6] == board[9] != ' ' or board[7] == board[5] == board[3] != ' ' or board[1] == board[5] == board[9] != ' '):
        slow_type("Game Over.")
        slow_type(turn + " won.") 
        printBoard()
        playAgain()
    elif count == 9:
      slow_type("Game Over. It is a tie")
      printBoard()
      playAgain()
  def movecode(turn) -> None:
    if turn == "x":
        printBoard()
        slow_type("It's your turn, Soham. Which place do you want to move to?"),
        move: int = int(input())
        while board[move] != ' ':
          Clearconsole()
          printBoard()
          slow_type("That place is already filled.Which place do you want to move to?")
          move: int = int(input())
        board[move] = "x"
        Clearconsole()
    else:
      if start == "p":
        printBoard()
        slow_type("It's your turn, o. Which place do you want to move to?"),
        move: int = int(input())
        while board[move] != ' ':
          Clearconsole()
          printBoard()
          slow_type("That place is already filled.Which place do you want to move to?")
          move: int = int(input())
        board[move] = "o"
        Clearconsole()
      else:
        move: int = compMove()
        board[move] = "o"
        Clearconsole()
  def game() -> None:
    resetBoard()
    global count,turn
    count: int = 0
    turn: str = "x"
    for i in range(10):
      count += 1
      movecode(turn)
      gameOver()
      if(turn == "x"):
          turn = "o"
      elif(turn == "o"):
          turn = "x"
  game()

def Clearconsole() -> None:
  command: str = 'clear'
  if os.name in ('nt', 'dos'):
    command = 'cls'
  os.system(command)

def slow_type(t) -> None:
  for l in t:
    sys.stdout.write(l)
    sys.stdout.flush()
    time.sleep(0.000001)
  print('')

while True:
  Clearconsole()
  #slow_type("What do you want to do?(1:calculation, 2:TicTacToe, 3:Wordle) ",end="")
  which: int = input("What do you want to do?(1:calculation, 2:TicTacToe, 3:Wordle) ")
  if which == "1":
    #slow_type("What do you want calculate?(1: grade,2: BMI,3: all) ",end="")
    calculate: int = input("What do you want calculate?(1: grade,2: BMI,3: all) ")
    if calculate == "1":
      gradeCalculator()
      time.sleep(2)
    elif calculate == "2":
      BMICalculator()
      time.sleep(2)
    elif calculate == "3":
      Calculate()
      time.sleep(2)
    else:
      while calculate != "1" or calculate != "2" or calculate != "3":
        calculate = input("What do you want calculate? grade, BMI, all ")
        if calculate == "1":
          gradeCalculator()
          time.sleep(2)
        elif calculate == "2":
          BMICalculator()
          time.sleep(2)
        elif calculate == "3":
          Calculate()
          time.sleep(2)
  elif which == "2":
    TicTacToe()
    time.sleep(2)
  elif which == "3":
    Wordle()
    time.sleep(2)
