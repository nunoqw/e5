import time
import tkinter as tk
from tkinter import messagebox

class FocusClock:
    def __init__(self, master):
        self.master = master
        self.master.title("专注时钟")
        self.master.geometry("300x150")

        self.label = tk.Label(master, font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="开始专注", command=self.start_focus)
        self.start_button.pack()

        self.remaining_time = 0
        self.focus_duration = 25 * 60  # 专注时长，默认为25分钟

    def start_focus(self):
        self.remaining_time = self.focus_duration
        self.update_label()
        self.start_timer()

    def update_label(self):
        minutes, seconds = divmod(self.remaining_time, 60)
        self.label.config(text="{:02d}:{:02d}".format(minutes, seconds))

    def start_timer(self):
        self.start_button.config(state="disabled")
        while self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time -= 1
            self.update_label()
            self.master.update()

        self.start_button.config(state="normal")
        messagebox.showinfo("专注结束", "专注时间结束，可以休息一下！")

if __name__ == "__main__":
    root = tk.Tk()
    focus_clock = FocusClock(root)
    root.mainloop()
