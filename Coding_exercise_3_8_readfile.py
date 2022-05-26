Practice2 = open("myFile.txt", "r")
print(Practice2.read())

Practice2 = open("myFile.txt", "r")
print(Practice2.readline())

Practice2 = open("myFile.txt", "r")
for lines in Practice2:
    print(lines)

Practice2.close()