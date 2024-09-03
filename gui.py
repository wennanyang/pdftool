import threading
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from make_result import main
from tkinter import messagebox
from pathlib import Path
import sys
class GUI():
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.fang_var = tk.StringVar()
        self.fu_var = tk.StringVar()
        self.validate_var = tk.StringVar()
        self.progress_lable_var = tk.StringVar()
        self.root.title("PDF字段提取程序")
        self.root.configure(bg="skyblue")
        self.root.minsize(200, 80)  # width, height
        self.root.maxsize(500, 150)
        self.root.geometry("600x300+250+250")
        self.root.iconbitmap(self.resource_path(r"ico\cloud.ico"))
        fang_frame = tk.Frame(self.root, bg="#6FAFE7")
        # 设置第一行放线路径的label, entry, button
        fang_frame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        fang_label = tk.Label(fang_frame, text="PDF文件夹", bg="#6FAFE7")
        fang_label.grid(row=0, column=0)
        self.fang_entry = tk.Entry(fang_frame, bd=3, width=50, textvariable=self.fang_var)
        self.fang_entry.grid(row=0, column=1)
        choose_fang_dir = tk.Button(fang_frame, text="选择目录", 
                                    command=lambda: self.select_directory(self.fang_var))
        choose_fang_dir.grid(row=0, column=2)
        # 设置第2行执行
        self.description_var = tk.StringVar()
        excute_frame = tk.Frame(self.root, bg="#6FAFE7")
        excute_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')
        self.turn_on = tk.Button(excute_frame, text="开始执行", command=self.excute)
        self.turn_on.grid(row=0, column=0)
        self.description_label = tk.Label(excute_frame, bg="#6FAFE7", textvariable=self.description_var)
        self.description_label.grid(row=0, column=1)

        ## 第3行的进度条
        progress_fram = tk.Frame(self.root, bg="#6FAFE7")
        progress_fram.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        self.progress_var = tk.IntVar()
        self.progressbar = ttk.Progressbar(progress_fram, orient="horizontal", length=400, mode="determinate", 
                                              variable=self.progress_var)
        self.progressbar["value"] = 0
        self.progressbar["maximum"] = 100
        self.pogress_label = tk.Label(progress_fram, text="进度", bg="#6FAFE7", textvariable=self.progress_lable_var)
        self.progressbar.grid(row=0, column=0)
        self.pogress_label.grid(row=0, column=1)
    def resource_path(self, relative_path) -> Path:
        """将相对路径转为exe运行时资源文件的绝对路径"""
        if hasattr(sys, '_MEIPASS'):
            base_path = Path(sys._MEIPASS)  # 只有通过exe运行时才会进入这个分支，它返回的是exe运行时的临时目录路径
        else:
            base_path = Path(".")
        return base_path.resolve().joinpath(relative_path) 
    def mainloop(self):
        self.root.mainloop()
    def select_directory(self, stringvar):
        directory = Path(filedialog.askdirectory()).resolve()
        if directory:
            stringvar.set(directory)
    def excute(self):
        threading.Thread(target=self.long_running_task,args=(), daemon=True).start()
    def update_progress(self, value, description):
        self.progress_var.set(value)
        self.progress_lable_var.set(f"{value : .2f}%")
        self.description_var.set(description)
        self.root.update_idletasks() 
    def long_running_task(self):
        main(pdf_dir=self.fang_entry.get(), 
             progress_callback=self.update_progress)
        self.description_var.set("")
        self.progress_var.set(0)
        self.progress_lable_var.set("")
        messagebox.showinfo("成功", "提取属性成功！") 
    
if __name__ == '__main__':
    gui = GUI()
    gui.mainloop()