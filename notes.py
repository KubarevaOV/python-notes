import json
import datetime

notes = []

def load_notes():
    global notes
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except:
        notes = []

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    note = {"id": len(notes)+1, "title": title, "body": body, "timestamp": str(datetime.datetime.now())}
    notes.append(note)
    save_notes()
    print("Заметка добавлена.\n")

def read_notes():
    print("Список заметок: \n")
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Дата создания: {note['timestamp']}")
        print(note['body'])
        print("\n")

def edit_note():
    id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note['id'] == id:
            note['title'] = input("Введите новый заголовок заметки: ")
            note['body'] = input("Введите новый текст заметки: ")
            note['timestamp'] = str(datetime.datetime.now())
            save_notes()
            print("Заметка отредактирована.\n")
            return
    print("Заметка не найдена.\n")

def delete_note():
    id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            save_notes()
            print("Заметка удалена.\n")
            return
    print("Заметка не найдена.\n")

def main():
    load_notes()
    while True:
        print("\n")
        print("1. Показать заметки")
        print("2. Добавить заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выход")
        print("\n")
        choice = input("Введите номер действия: ")
        if choice == "1":
            read_notes()
        elif choice == "2":
            add_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Некорректный ввод.\n")

if __name__ == "__main__":
    main()
