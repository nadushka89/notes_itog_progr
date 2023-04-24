import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_file():
    """Открывает файл для редактирования"""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_result.delete("1.0", tk.END)
    with open(filepath, "r", encoding="UTF-8") as input_file:
        text = input_file.read()
        text_result.insert(tk.END, text)
    window.title(f"Мои заметки - {filepath}")


window = tk.Tk()
"""Создается новое окно с заголовком "Мои заметки"""
window.title("Мои заметки")

window.rowconfigure(1, minsize=100, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

title = tk.Text(window)
text_body = tk.Text(window)
text_result = tk.Text(window, background="grey")

fr_buttons = tk.Frame(window)
btn_open = tk.Button(fr_buttons, text = "Открыть заметку", command=open_file)
btn_all_notes = tk.Button(fr_buttons, text = "Посмотреть все заметки")
btn_add = tk.Button(fr_buttons, text = "Добавить заметку")
btn_find_id = tk.Button(fr_buttons, text = "Найти по ID")
btn_find_date = tk.Button(fr_buttons, text = "Найти по дате")
btn_update = tk.Button(fr_buttons, text = "Изменить заметку")
btn_delete = tk.Button(fr_buttons, text = "Удалить заметку")
btn_save = tk.Button(fr_buttons, text = "Сохранить заметку")
btn_exit = tk.Button(fr_buttons, text = "Выход")

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_all_notes.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_add.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_find_id.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_find_date.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_update.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_delete.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
btn_exit.grid(row=8, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
title.grid(row=0, column=1, sticky="nsew")
text_body.grid(row=1, column=1, sticky="nsew")
text_result.grid(row=2, column=1, sticky="nsew")

window.mainloop()






