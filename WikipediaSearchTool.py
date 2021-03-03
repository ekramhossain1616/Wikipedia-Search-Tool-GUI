import tkinter as tk
import wikipedia

# from tkinter import ttk

win  = tk.Tk()
# win.geometry('480x360')
win.resizable(0,0)
win.title('Wikipedia Search Tool')

def search_me():
    entry_text = entry1.get()
    text_box.delete(1.0, tk.END)
    try:
        answer = wikipedia.summary(entry_text)

        text_box.insert(tk.INSERT, answer)
    except:
        text_box.insert(tk.INSERT, f'Nothing found with {entry_text} or check your internet connection.')


top_frame = tk.Frame(win)
top_frame.pack(pady=10)
entry1 = tk.Entry(top_frame, width=30)
entry1.pack()
search_btn = tk.Button(top_frame, text='Search', command = search_me)
search_btn.pack(pady=4)

bottom_frame = tk.Frame(win)
bottom_frame.pack()

scroll_bar = tk.Scrollbar(bottom_frame, )
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_box = tk.Text(bottom_frame, width=80, height = 30, wrap='word', yscrollcommand= scroll_bar.set)
scroll_bar.config(command=text_box.yview)
text_box.pack(side=tk.LEFT, padx=8, pady=8)


win.mainloop()


