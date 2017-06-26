


#import the modules we need, for creating a GUI...
import tkinter
#...and for creating random numbers.
import random

#the list of possible colors.
colors = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
#the player's score and High Score, initially 0.
score=0
highscore=0
#the game time left, initially 30 seconds.
timeleft=30

#a function that will start the game.
def startGame(event):

    #if there's still time left...
    if timeleft == 30:
        #start the countdown timer.
        countdown()

    #run the function to choose the next colour.
    nextColour()

#function to choose and display the next colour.
def nextColour():

    #use the globally declared 'score' and 'play' variables above.
    global score
    global timeleft
    global highscore

    #if a game is currently in play...
    if timeleft > 0:

        #...make the text entry box active.
        e.focus_set()

        #if the colour typed is equal to the color of the text...
        if e.get().lower() == colors[1].lower():
            #...add one to the score.
            score += 1

        #clear the text entry box.
        e.delete(0, tkinter.END)
        #shuffle the list of colours.
        random.shuffle(colors)
        #change the colour to type, by changing the text _and_ the colour to a random colour value
        label.config(fg=str(colors[1]), text=str(colors[0]))
        #update the score.
        scoreLabel.config(text="Score: " + str(score))
        highscorelabel.config(text="High Score: " + str(highscore))
#a countdown timer function.
def countdown():

    #use the globally declared 'play' variable above.
    global timeleft

    #if a game is in play...
    if timeleft > 0:

        #decrement the timer.
        timeleft -= 1
        #update the time left label.
        timeLabel.config(text="Time left: " + str(timeleft))
        #run the function again after 1 second.
        timeLabel.after(1000, countdown)

#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Rglass")
#set the size.
root.geometry("400x400")

#add an instructions label.
instructions = tkinter.Label(root, text="Type in the color of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

#add a score label.
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()



#add a time left label.
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

#add a label for displaying the colours.
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

#add a text entry box for typing in colours.
e = tkinter.Entry(root)
#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)
e.pack()
#set focus on the entry box.
e.focus_set()

#start the GUI
root.mainloop()
