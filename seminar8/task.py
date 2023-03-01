import csv

def add_contact():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    
    with open("phonebook.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, patronymic, phone])
    
    print("Контакт успешно добавлен!\n")

def search_contact():
    with open("phonebook.csv", "r") as file:
        reader = csv.reader(file)
        found = False
        search_term = input("Введите имя, фамилию, отчество или номер телефона: ")
        
        for row in reader:
            if search_term.lower() in [x.lower() for x in row]:
                print(f"Имя: {row[0]}\nФамилия: {row[1]}\nОтчество: {row[2]}\nНомер телефона: {row[3]}\n")
                found = True
        
        if not found:
            print("Контакт не найден!\n")
            
def export_contacts():
    with open("phonebook.csv", "r") as file:
        reader = csv.reader(file)
        with open("phonebook_export.txt", "w") as export_file:
            for row in reader:
                export_file.write(f"{row[0]} {row[1]} {row[2]}: {row[3]}\n")
    
    print("Контакты успешно экспортированы в файл 'phonebook_export.txt'!\n")

def print_menu():
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Экспортировать контакты в файл")
    print("4. Выйти")

def main():
    while True:
        print_menu()
        choice = input("Выберите действие: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            export_contacts()
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.\n")

if __name__ == "__main__":
    main()