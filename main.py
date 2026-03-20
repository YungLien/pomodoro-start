from tkinter import *
from tkinter import ttk
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
time = None
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer.config(text="Short Break", fg=PINK)
    elif reps % 2 == 1:
        countdown(work_sec)
        timer.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # dynamic typing
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

check_mark = Label(fg=GREEN, bg=YELLOW)
check_mark.grid(row=3, column=1)

canvas = Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


style = ttk.Style()
style.theme_use('default')
style.configure("Custom.TButton",
                font=(FONT_NAME, 16),
                background="white",
                relief="flat",
                borderwidth=0)
start_button = ttk.Button(window, text="Start", style="Custom.TButton", command=start_timer)
start_button.grid(row=2, column=0, padx=20, pady=10)

reset_button = ttk.Button(window, text="Reset", style="Custom.TButton", command=timer_reset)
reset_button.grid(row=2, column=2, padx=20, pady=10)
window.mainloop()