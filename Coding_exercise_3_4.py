myPractice = open("myFile.txt", "w")
myPractice.write("The syntax of Python is almost similar to other programming languages, so I find it simple.")

myPractice = open("myFile.txt", "a")
myPractice.write("\nI plan to practice more to improve my programming skills.")
myPractice.write("\nBy creating programs using Python.")
myPractice.write("\nMy final goal is to become a video game developer, but my initial goal is to have enough programming skills and knowledge as a software developer.")

myPractice = open("myFile.txt", "r")
print(myPractice.read())
myPractice.close()
