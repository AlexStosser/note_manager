user_name = "Александр" # username
title = 'Grade 1.1' # titul
content = 'Практическое задание 1' # content
status = 'В процессе' # status
created_date = '11-12-2024' # created date
issue_date = '12-12-2024' # issue date

new_created_date = created_date[:5]
new_issue_date = issue_date[:-5]

print("Имя пользователя: ", user_name) #
print("Титул: ", title) #
print('Содержание: ', content)
print("Дата начала заметки: ", new_created_date)
print('Дата окончания заметки: ', new_issue_date)