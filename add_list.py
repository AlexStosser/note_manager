user_name = input("Как вас Зовут? ")  # username
title = input('Как будет называться тема? ') # titul
content = input("Содержание вашей темы: ") # content
headline = []
for i in range (3):
    list = input(f"Ведите Название заголовки {i+1}: ")
    headline.append(list.capitalize())
status = input('Укажите статус (Активен/Сделано): ') # status
created_date = input("дата начала заметки (Пример: 11.12.2024): ") # created date
issue_date = input("дата окончание заметки (Пример: 12.12.2024): ") # issue date

new_created_date = created_date[:5]
new_issue_date = issue_date[:-5]

print("Здравстуйте, ", user_name.capitalize()) #
print("Тема: ", title.upper()) #
print('Содержание: ', content.capitalize())
print('Ваши заголовки: ', headline)
print('Ваш статус: ', status.capitalize())
print("Дата начала заметки: ", new_created_date)
print('Дата окончания заметки: ', new_issue_date)