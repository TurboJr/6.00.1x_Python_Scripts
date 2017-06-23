#Приветствие
print('Great Python Program')
print('Привет программист!')
name = input("Как Вас зовут: ")

print(name, ', добро пожаловать в мир Python!')

#Приглашение поработать
answer = input("Давайте поработаем? (Y/N/q) ")

if answer == 'Y':
    print('отлично!')
    print('я умею:')
elif answer == 'N':
    print('До свидания!')
else:
    print('Неизвестный ответ')

