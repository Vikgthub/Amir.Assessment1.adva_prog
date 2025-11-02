
#import tkinter and random
from tkinter import *
from random import randint, choice


#fix the window
root = Tk()
root.geometry("440x440")
root.title("Maths Quiz")

#create your variablens (for the question,answer,user's answer, the score, question number, difficulty level)
question = StringVar()
answer = StringVar()
userAnswer = StringVar()
score = IntVar()
questionNUM = IntVar()
difficulty = StringVar(value="Easy")

questionLabel = None
resultLabel = None
scoreLabel = None


#define a function to generate questions
def generateQuestion():

    #use the variables 
    global questionLabel

    #questions get added up
    questionNUM.set(questionNUM.get() + 1)

    # add dificulties
    level = difficulty.get()
    #if easy level is picked, then generate signle digit numbers in the quiz questions
    if level == "Easy":
        number1 = randint(1, 9)
        number2 = randint(1, 9)
    #if moderate level was picked, then generate double digits numbers in the quiz questions
    elif level == "Moderate":
        number1 = randint(10, 99)
        number2 = randint(10, 99)
    # otherwise*, if hard was picked, then generate triple digits numbers in the quiz questions
    else:  
        number1 = randint(100, 999)
        number2 = randint(100, 999)

    #allow the quiz to randomly use addition or subtraction operator 
    operator = choice(['+', '-'])
    #frame the questions (first number + operators(either + or -) + second number) 
    question.set(str(number1) + operator + str(number2))


    #remove the old question and give the second question
    if questionLabel:
        questionLabel.destroy()

    #display the question
    questionLabel = Label(root, text=f"Question {questionNUM.get()}: {question.get()}")
    questionLabel.place(x=49, y=180)




#define anoter function to see if the answer is correct or wrong
def checkAnswer():
    #once again get the variable
    global resultLabel

    #remove the previous result
    resultLabel.config(text="")

    #check for exception error
    try:
        #get the user input as integer
        useranswer = int(userAnswer.get())  
    #if the user gives answer other than a number, dont end the code, instead handle the error and ask user to give a valid answer
    #value error exception checks if the value is inappropriate or not
    except ValueError:
        resultLabel.config(text="Enter a valid number!")
        return

    # evaluate the correct answer
    correct_answer = eval(question.get())

    #if answer is correct add +10 score everytime and display correct answer
    if useranswer == correct_answer:
        resultLabel.config(text="Correct!")
        score.set(score.get() + 10)
    #if not then add +0 score and display incorrect answer
    else:
        resultLabel.config(text=f"Incorrect! Ans: {correct_answer}")
        score.set(score.get() + 0)

    #update the score
    scoreLabel.config(text=f"Score: {score.get()}")

    #clear the entry for next question
    userAnswer.set("")

    #if question number has not reached 10 then generate next question
    if questionNUM.get() < 10:
        generateQuestion()
    #otherwise end the questions
    else:
        resultLabel.config(text=f"Quiz Over! Final Score: {score.get()}")




#define another function to restart the quiz...
def restart():

    #sets the score and question number to zero and start from the begining 
    score.set(0)
    questionNUM.set(0)
    userAnswer.set("")
    scoreLabel.config(text="Score: 0")
    generateQuestion()



#create the user interface layout

#create a lable to display the heading "Maths Quiz"
headingLabel = Label(root, text="Maths Quiz")
headingLabel.place(x=173, y=46)

#create another label to display to user to select dificulty
difficultyLabel = Label(root, text="Select Difficulty:")
difficultyLabel.place(x=49, y=125)

#create option menu to display the dificulty level
difficultyMenu = OptionMenu(root, difficulty, "Easy", "Moderate", "Hard")
difficultyMenu.place(x=199, y=121)

#create a button to let user start the quiz
startButton = Button (root, text="Start", command=generateQuestion)
startButton.place(x=303, y=121)

#create entry to let user input the answer
answerEntry = Entry(root, textvariable=userAnswer, width=25)
answerEntry.place(x=49, y=210)

#create a button to submit the answer
submitButton = Button(root, text="Submit", command=checkAnswer)
submitButton.place(x=303, y=210)

#create label to display results
resultLabel = Label(root, text="Result")
resultLabel.place(x=49, y=269)

#create label to displauy score
scoreLabel = Label(root, text="Score: 0" )
scoreLabel.place(x=49, y=308)

#create button to let user restart the quiz
restartButton = Button(root, text="Restart", command=restart)
restartButton.place(x=176, y=364)

#end the loop
root.mainloop()



""" reference:

Python Tutorial, Tkinter OptionMenu. Available at: https://www.pythontutorial.net/tkinter/tkinter-optionmenu/

Vishesh Programming (2023), Create random question | Math Quiz using Python Tkinter - 2. Available at: https://www.youtube.com/watch?v=KhkI66p53Mw  
[disclaimer, the video's transcript is in different language. Youtube allows viewers to auto-translate the captions to English]

 """
