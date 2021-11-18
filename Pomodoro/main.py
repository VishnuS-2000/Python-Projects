from tkinter import  *
import math
#--------------CONSTANTS---------------#

PINK="#F72464"
RED="#FF858A"
GREEN="#568564"
YELLOW="#FFF3A7"

FONT_NAME="Courier"

PREFIX="0"

WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20

#--------------Timer Reset ----------#



#-------------Timer Mechanism ----------#



#----------- Countdom Mechanism -------------#




#------------------- UI Setup --------------#

window=Tk()
window.minsize(width=640,height=480)
window.title("Pomodoro App")

window.config(padx=160,pady=100,bg=YELLOW)

reps=0
stage=""
timer=None

def countdown(count):

    minutes=str(math.floor(count/60))
    seconds=str(count%60)

    if int(minutes) < 10: minutes = PREFIX+minutes
    if int(seconds) < 10: seconds = PREFIX+seconds

    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    if(count>0):
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()

def start_timer():
    global reps
    reps+=1
    time=0
    if(reps%2==0 and not reps==3):
        countdown(SHORT_BREAK_MIN*60)
        title.config(text="Break",fg=RED)
        tick.config(text="✔"*math.floor(reps/2))
    elif(reps==3):
        countdown(LONG_BREAK_MIN*60)
        title.config(text="Long Break",fg=PINK)
    else:
        countdown(WORK_MIN*60)
        title.config(text="Work",fg=GREEN)

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps=0
    title.config(text="Timer")
    tick.config(text="")
    canvas.itemconfig(timer_text,text="00:00")


title=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,36,"bold"))
title.grid(column=1,row=0)



canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)


imageFile=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=imageFile)

timer_text=canvas.create_text(100,130,text="00:00",font=(FONT_NAME,24,"bold"),fill="white")


canvas.grid(column=1,row=1)

start=Button(text="Start",bg="white",border=0,highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)


reset=Button(text="Reset",bg="white",border=0,highlightthickness=0,command=reset_timer)
reset.grid(column=2,row=2)

tick=Label(text="",fg="green",bg=YELLOW,font=(FONT_NAME,20,"bold"))
tick.grid(column=1,row=3)

window.mainloop()



