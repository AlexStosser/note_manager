note = {}

note ["имя_пользователя"] = input("Как вас Зовут? ")  # username
note['Тема'] = input('Как будет называться тема? ') # titul
note['содержание'] = input("Содержание вашей темы: ") # content
заголовка = []
for i in range (3):
    note['заголовки'] = input(f"Ведите Название заголовки {i+1}: ")

note['статус'] = input('Укажите статус (Активен/Сделано): ') # status
note['дата_начала_заметки'] = input("дата начала заметки (Пример: 11.12.2024): ") # created date
note['дата_окончания_заметки'] = input("дата окончание заметки (Пример: 12.12.2024): ") # issue date

дата_начала = note['дата_начала_заметки']
дата_окончания = note['дата_окончания_заметки']

for key, value in note.items():
 print(f'{key}: {value}')


