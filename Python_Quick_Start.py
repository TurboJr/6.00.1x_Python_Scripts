
import os
import psutil

#Приветствие
print('Great Python Program')
print('Привет программист!')
name = input("Как Вас зовут: ")

print(name, ', добро пожаловать в мир Python!')

#Приглашение поработать
answer = input("Давайте поработаем? (Y/N/q) ")

#Что делать при положительном ответе
if answer == 'Y':
    print('отлично!')
    print('я умею:')
	print('[1] - выведу список файлов')    
	print('[2] - выведу информацию о системе')
	print('[3] - выведу список процессов')
	print('[4] - ')
	print('[5] - ')
	print('[6] - ')
	
	#Выбор действия
	do = int(input('укажите номер действия'))

	if do == 1:
		print(os.listdir())
	elif do = 2:
		print('Вот что я знаю о системе:')			
		print('Количество процессоров: ', psutil.cpu_count())			
		print('Платформа: ', sys.platform)
		print('Кодировка файловой системы: ', sysgetfilesystemencoding())	
		print('Текущая директория: ', os.getcwd()) 
		print('Текущий пользователь: ', os.getlogin())
	
	elif do == 3:
		print(psutil.pids())		


#Что делать при отрицательном ответе
elif answer == 'N':
    print('До свидания!')

#Что делать в остальных случаях 
else:
    print('Неизвестный ответ')

