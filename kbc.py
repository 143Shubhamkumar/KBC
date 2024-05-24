questions = [
  [
    "Which language was used to create fb?", "Python", "French", "JavaScript",
    "Php", 4
  ],
  [
    "What is the capital of France?", "Paris", "France", "India", "Japan", 1
  ],
  [
    "In which year did World War II end?", "1944", "1945", "1946", "1947", 2
  ],
  [
    "Which ocean is the largest?", "Pacific Ocean", "Indian Ocean", "Atlantic Ocean", "Arctic Ocean", 1
  ],
  [
    "How are String represented in memory in C?", "An array of characters", "The object of some class", "Same as othe primitive data types", "LinkedList of characters", 1
  ],
  [
    "In which year did the Titanic sink?", "1910", "1911", "1912", "1913", 3
  ],
  [
    "What is the smallest prime number?", "0", "1", "3", "2", 4
  ],
  [
    "What is the longest river in the world?", "Amazon River", "Ganga River", "Nile", "Lena", 1 
  ],
  [
    "In which year did the American Civil War end?" ,"1864", "1865", "1866", "1867", 2
  ],
  [
    "How is the 3rd element in an array accessed based on pointer notation?", "*a+3", "*(a+3)", "*(*a+3)", "&(a+3)", 2
  ],
  [
    "What is an example of iteration in C?", "for", "while", "do-while", "all of the mentioned", 4
  ],
]

levels = [
  1000, 2000, 3000, 4000, 5000, 10000, 20000, 40000, 80000, 160000, 320000
]
name = input("Enter your name: ")
import time

t = time.strftime('%H:%M:%S')
hours = int(time.strftime('%H'))
# hours = int(input("Enter the hours: "))
# print(hours)

if (hours >= 0 and hours <= 12):
  print("Good Morning " + name)
elif (hours >= 15 and hours < 19):
  print("Good Evening " + name)
elif (hours >= 19 and hours < 0):
  print("Good Night " + name)
else:
  print("Good Afternoon " + name)


money = 0
for i in range(0, len(questions)):
  question = questions[i]
  
  print(f"\n \n Qustion for Rs. {levels[i]}")
  print(f"Q. {question[0]}")
  print(f"a. {question[1]}       b. {question[2]} ")
  print(f"c. {question[3]}       d. {question[4]} ")
  reply = int(input("Enter your answer (1-4) or 0 to quit: "))
  if(reply == 0):
    money = levels[i-1]
    break
  if (reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if (i == 4):
      money = 10000
    elif (i == 9):
      money = 320000
    elif (i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break

print("Congratulations " + name)
print(f"You won this money {money}")