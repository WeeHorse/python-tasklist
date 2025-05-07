import tkinter as tk
from tkinter import messagebox, simpledialog
import psycopg2

# Update with your database details
conn = psycopg2.connect(
    dbname='your_dbname',
    user='your_user',
    password='your_password',
    host='localhost',
    port='5432'
)
cursor = conn.cursor()

class TaskApp:
    def __init__(self, master):
        self.master = master
        master.title("Task List App")

        self.user_listbox = tk.Listbox(master)
        self.user_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.user_listbox.bind("<<ListboxSelect>>", self.load_lists)

        self.list_listbox = tk.Listbox(master)
        self.list_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
        self.list_listbox.bind("<<ListboxSelect>>", self.load_tasks)

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.add_task_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_task_button.pack(side=tk.BOTTOM)

        self.load_users()

    def load_users(self):
        self.user_listbox.delete(0, tk.END)
        cursor.execute("SELECT id, username FROM users")
        self.users = cursor.fetchall()
        for user in self.users:
            self.user_listbox.insert(tk.END, user[1])

    def load_lists(self, event):
        self.list_listbox.delete(0, tk.END)
        self.task_listbox.delete(0, tk.END)
        idx = self.user_listbox.curselection()
        if not idx:
            return
        self.selected_user = self.users[idx[0]]
        cursor.execute("SELECT id, name FROM lists WHERE user_id = %s", (self.selected_user[0],))
        self.lists = cursor.fetchall()
        for lst in self.lists:
            self.list_listbox.insert(tk.END, lst[1])

    def load_tasks(self, event):
        self.task_listbox.delete(0, tk.END)
        idx = self.list_listbox.curselection()
        if not idx:
            return
        self.selected_list = self.lists[idx[0]]
        cursor.execute("SELECT description, done FROM tasks WHERE list_id = %s", (self.selected_list[0],))
        tasks = cursor.fetchall()
        for task in tasks:
            prefix = "[✓] " if task[1] else "[ ] "
            self.task_listbox.insert(tk.END, prefix + task[0])

    def add_task(self):
        if not hasattr(self, "selected_list"):
            messagebox.showwarning("No list selected", "Please select a list first.")
            return
        task = simpledialog.askstring("New Task", "Enter task description:")
        if task:
            cursor.execute("INSERT INTO tasks (description, list_id) VALUES (%s, %s)",
                           (task, self.selected_list[0]))
            conn.commit()
            self.load_tasks(None)

root = tk.Tk()
app = TaskApp(root)
root.mainloop()
