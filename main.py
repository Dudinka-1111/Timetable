import tkinter as tk

def add_lesson():
    lesson = lesson_entry.get()
    if lesson:
        # Получаем текущее количество элементов в списке для нумерации
        current_count = lesson_listbox.size()
        numbered_lesson = f"{current_count + 1}. {lesson}"
        lesson_listbox.insert(tk.END, numbered_lesson)
        lesson_entry.delete(0, tk.END)

def delete_lesson():
    selected_lesson_index = lesson_listbox.curselection()
    if selected_lesson_index:
        lesson_listbox.delete(selected_lesson_index)
        # Обновляем нумерацию после удаления элемента
        update_numbers()

def update_numbers():
    # Обновляем нумерацию всех элементов в списке
    for index in range(lesson_listbox.size()):
        lesson = lesson_listbox.get(index)
        # Извлекаем текст без номера и точки
        actual_lesson_text = lesson.split(". ", 1)[-1]
        # Обновляем текст с новым номером
        lesson_listbox.delete(index)
        lesson_listbox.insert(index, f"{index + 1}. {actual_lesson_text}")

root = tk.Tk()
root.title("Расписание уроков")
root.geometry("300x300")
root.configure(bg="PapayaWhip")

# Метка с текстом "Введи название предмета"
label = tk.Label(root, text="Введи название предмета", bg="PapayaWhip")
label.pack(pady=5)

# Поле для ввода названия урока
lesson_entry = tk.Entry(root, width=30, bg="pink")
lesson_entry.pack(pady=10)

# Кнопка для добавления урока
add_button = tk.Button(root, text="Добавить урок", command=add_lesson)
add_button.pack(pady=5)

# Кнопка для удаления урока
delete_button = tk.Button(root, text="Удалить урок", command=delete_lesson)
delete_button.pack(pady=5)

# Метка с названием списка "Расписание уроков!"
list_label = tk.Label(root, text="Расписание уроков!", bg="PapayaWhip", font=("Arial", 10, "bold"))
list_label.pack(pady=5)

# Список уроков
lesson_listbox = tk.Listbox(root, width=40, height=10, bg="pink")
lesson_listbox.pack(pady=10)

root.mainloop()