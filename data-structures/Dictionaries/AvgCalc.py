print("Hello! Please enter your grades in 0-100 format in order to be formatted into Letter format! When you're done, please enter an empty value!")
hunAvg = 0.0

letAvg = {93 : "A", 90 : "A-", 87 : "B+", 83 : "B",
          80 : "B-", 77 : "C+", 70 : "C", 60 : "D", 0 : "F"}

avgTotal = 0
courseNum = 0
done = False
def calcLetter(y):
    for x in letAvg.keys():
        if y >= x:
            return letAvg[x]
            break




while not done:
    grade = input()
    if grade == "":
        done = True
    elif not grade.isnumeric:
        print("You have entered something that isnt a number, please try again.")
    elif int(grade) > 100.0 or int(grade) < 0.0:
        print("You have entered a number that is greater than 100 or less than 0, try again.")\
        
    else:
        courseNum +=1
        avgTotal += float(grade)
if courseNum > 0:
    hunAvg = avgTotal / courseNum
    print(hunAvg)
    print("Your letter grade is " + calcLetter(hunAvg)) 
    



