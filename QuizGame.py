print("Hey! Welcome to my game zone i'm Danat ")
playing = input("Do you want to know about the world that you are living at?  ")
if playing.lower() == "yes":
    print("this is the exact game for you")
    print("okay let's play then")
else:
    quit()    

score = 0
#***************************
answer=input("what is the capital city of USA?")
if (answer.lower() == "washington d.c"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")    


answer=input("what is the capital city of India?")
if (answer.lower() == "new delhi"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")    


answer=input("what is the capital city of Ethiopia?")
if (answer.lower() == "addis ababa"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")   



answer=input("what is the capital city of Japan?")
if (answer.lower() == "tokyo"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")        



answer=input("what is the capital city of China?")
if (answer.lower() == "beijing"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")   


answer=input("what is the capital city of Canada?")
if (answer.lower() == "ottawa"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")   




answer=input("what is the capital city of England?")
if (answer.lower() == "london"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")   


answer=input("what is the capital city of Germany?")
if (answer.lower() == "berlin"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")   






answer=input("what is the capital city of France?")
if (answer.lower() == "paris"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")       





answer=input("what is the capital city of Italy?")
if (answer.lower() == "rome"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")       



answer=input("what is the capital city of Australia?")
if (answer.lower() == "canberra"):
    print("you got it!")
    score += 1
else:
    print("incorrect answer")       


print("You answered " + str(score) + " questions correct out of 11 questions.") 
print ("You answered " + str((score)/11 *100) + "%.") 

print("HAVE A GOOD TIME FROM ME..............DANAT")