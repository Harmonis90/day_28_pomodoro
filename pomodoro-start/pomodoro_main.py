from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#ffccdf"
PURPLE = "#ecccff"
CREAM = "#FFECCC"
BROWN = "#8B7357"
BLUE = "#1ABEE8"
RED = "#D9534F"
GREEN = "#ccffec"
ORANGE = "#FFAD60"
YELLOW = "#FFEEAD"
GRAY = "#B2AB99"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CANV_WIDTH = 200
CANV_HEIGHT = 224
IMAGE_CENTER_X = round(CANV_WIDTH / 2)
IMAGE_CENTER_Y = round(CANV_HEIGHT / 2)
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(str(timer))
    main_canv.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=BROWN)
    main_canv.config(highlightthickness=2, highlightbackground=ORANGE)
    check_mark_label.config(bg=YELLOW, highlightcolor=YELLOW)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    if reps == 8:
        reps = 0

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=BROWN)
        main_canv.config(highlightbackground=BLUE)
    elif reps % 2 == 0 and reps % 8 != 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=BROWN)
        main_canv.config(highlightbackground=BLUE)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=BROWN)
        main_canv.config(highlightbackground=RED, highlightthickness=2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(num):
    global timer
    num_min = math.floor(num / 60)
    num_sec = num % 60
    format_time = f"{num_min:02d}:{num_sec:02d}"
    main_canv.itemconfig(timer_text, text=format_time)
    if num > 0:
        timer = window.after(1000, count_down, num - 1)
    else:
        start_timer()
        check_holder = ""
        gen_new_checkmark = math.floor(reps / 2)
        for check in range(gen_new_checkmark):
            check_holder += "✓"
        check_mark_label.config(text=check_holder, fg=GREEN, bg=PINK,
                                highlightcolor=BLUE, highlightthickness=2)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Time Manager")
window.config(padx=100, pady=50, bg=YELLOW)


main_canv = Canvas(width=CANV_WIDTH, height=CANV_HEIGHT, bg=CREAM, highlightthickness=3, highlightcolor=BLUE)
tomato_image = PhotoImage(file="tomato.gif")

main_canv.create_image(IMAGE_CENTER_X + 2, IMAGE_CENTER_Y, image=tomato_image)
timer_text = main_canv.create_text(IMAGE_CENTER_X + 2, IMAGE_CENTER_Y + 18, text="00:00", fill=CREAM,
                                   font=(FONT_NAME, 35, "bold"))

main_canv.grid(column=1, row=1)


# Top label text
# timer_label_outline = Label(text="Timer", font=(FONT_NAME, 38, "bold"), bg=YELLOW, fg=BLUE)
timer_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=BROWN)
timer_label.grid(column=1, row=0)
# timer_label_outline.grid(column=1, row=0)

button_left = Button(text="Start", font=(FONT_NAME, 10, "normal"), bg=BROWN, fg=CREAM)
button_left.config(activebackground=CREAM, command=start_timer)
button_left.grid(column=0, row=2)

button_right = Button(text="Reset", font=(FONT_NAME, 10, "italic"), bg=CREAM, fg=BROWN, command=reset_timer)
button_right.grid(column=2, row=2)

check_mark_label = Label(bg=YELLOW)
check_mark_label.grid(column=1, row=3)


window.mainloop()