note = {}
note ["username"] = input("Как вас Зовут? ")  # username
note['title'] = input('Как будет называться тема? ') # titul
note['content'] = input("Содержание вашей темы: ") # content
note ['headline'] = []
for i in range (3):
    list = input(f"Ведите Название заголовки {i+1}: ")
    note ['headline'].append(list.capitalize())
note['status'] = input('Укажите статус (Активен/Сделано): ') # status
created_date = input("дата начала заметки (Пример: 11.12.2024): ") # created date
issue_date = input("дата окончание заметки (Пример: 12.12.2024): ") # issue date

note['new_created_date'] = created_date[0:5]
note['new_issue_date'] = issue_date[0:-5]

for key, value in note.items():
 print(f'{key}: {value}')


