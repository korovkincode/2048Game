from tkinter import *
from random import randint
import func

#Настраиваем DEBUG_MODE
DEBUG_MODE = True
if DEBUG_MODE:
	log_file = open('log_file.txt', 'w')

print('LOG FILE (DEBUG_MODE = TRUE)', file = log_file)

# Константы игры
SIZE_X = 725
SIZE_Y = 725
SIZE_CELL = 150

#Открываем окно
root = Tk()
root.title('2048 Game')
root.minsize(SIZE_X, SIZE_Y)
canv = Canvas(width = SIZE_X, height = SIZE_Y, bg = 'papaya whip')
canv.pack()

#Настройка поля
field = []
for _ in range(4):
	field.append([None, None, None, None])
field[randint(0, 3)][randint(0, 3)] = 2
randomX = randint(0, 3)
randomY = randint(0, 3)
while field[randomX][randomY] != None:
	randomX = randint(0, 3)
	randomY = randint(0, 3)
field[randomX][randomY] = 2

#Функция для выхода из игры
def exit_f():
	exit(0)

#Функция для вывода поля в лог файл
def log_field():
	for row in field:
		for element in row:
			print(element, end = ' ', file = log_file)
		print('' , file = log_file)

if DEBUG_MODE:
	print('FIELD GENERATED', file = log_file)
	log_field()

#Функция отрисовки поля
def draw_field(field):
	for row in range(len(field)):
		for cell in range(len(field[row])):
			if field[row][cell] == None:
				color = 'cornsilk3'
			if field[row][cell] == 2:
				color = 'gainsboro'
			if field[row][cell] == 4:
				color = 'snow2'
			if field[row][cell] == 8:
				color = 'dark orange'
			if field[row][cell] == 16:
				color = 'salmon'
			if field[row][cell] == 32:
				color = 'tomato'
			if field[row][cell] == 64:
				color = 'red'
			if field[row][cell] == 128:
				color = 'light goldenrod'
			if field[row][cell] == 256:
				color = 'gold2'
			if field[row][cell] == 512:
				color = 'goldenrod1'
			if field[row][cell] == 1024:
				color = 'tan1'
			if field[row][cell] == 2048:
				color = 'gold'
			canv.create_rectangle(25 + cell * 150 + 10 * cell, 25 + row * 150 + 10 * row, 25 + cell * 150 + 150 + 10 * cell, 25 + row * 150 + 150 + 10 * row, fill = color)
			if field[row][cell] != None:
				canv.create_text(25 + cell * 150 + 10 * cell + 75, 25 + row * 150 + 10 * row + 75, font = ('Purisa', 45), text = str(field[row][cell]))

#Спавн новой плитки(2 или 4) после хода
def after_move():
	randomposX = randint(0, len(field) - 1)
	randomposY = randint(0, len(field) - 1)
	flag = True
	for i in range(len(field)):
		for j in range(len(field)):
			if field[i][j] == None: flag = False
	if not flag:
		while field[randomposX][randomposY] != None:
			randomposX = randint(0, len(field) - 1)
			randomposY = randint(0, len(field) - 1)
		randomInt = randint(1, 100)
		#Шанс спавна 2 - 90%, 4 - 10%
		if randomInt % 10 == 0:
			field[randomposX][randomposY] = 4
		else:
			field[randomposX][randomposY] = 2
		if DEBUG_MODE:
			print(f'SPAWNED NEW TILE {field[randomposX][randomposY]} ON POSITION [{randomposX + 1}, {randomposY + 1}]', file = log_file)
			log_field()
		if not func.up_dir(field) and not func.down_dir(field) and not func.left_dir(field) and not func.right_dir(field):
			canv.delete('all')
			canv.create_text((360, 360), text = 'You lose')
			root.after(1000, exit_f)		 

#Движение вверх
def up_dir(event):
	print('UP SHIFT', file = log_file)
	flag = False
	for i in range(len(field)):
		#Формируем линию которую сдвигаем
		line = []
		for j in range(0, len(field)):
			line.append(field[j][i])
		line_f = line
		line = list(filter(lambda el : el != None, line))
		el = len(line) - 1
		#Делаем сдвиг по линии
		while el > 0:
			if line[el] == line[el - 1] and line[el] != None:
				line[el - 1] *= 2
				line[el] = None
				if DEBUG_MODE:
					print(f'NEW TILE {line[el - 1]} GENERATED AFTER ADDITION', file = log_file)
				el -= 1
			el -= 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.append(None)
		for j in range(0, len(field)):
			field[j][i] = line[j]
		if line_f != line: flag = True
	log_field()
	#Если был хоть один сдвиг, то спавним новую плитку
	if flag: after_move()
	draw_field(field)

#Движение вниз
def down_dir(event):
	print('DOWN SHIFT', file = log_file)
	flag = False
	for i in range(len(field)):
		line = []
		for j in range(0, len(field)):
			#Формируем линию которую сдвигаем
			line.append(field[j][i])
		line_f = line
		line = list(filter(lambda el : el != None, line))
		el = 0
		#Делаем сдвиг по линии
		while el < len(line) - 1:
			if line[el] == line[el + 1] and line[el] != None:
				line[el + 1] *= 2
				line[el] = None
				if DEBUG_MODE:
					print(f'NEW TILE {line[el + 1]} GENERATED AFTER ADDITION', file = log_file)
				el += 1
			el += 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.insert(0, None)
		for j in range(0, len(field)):
			field[j][i] = line[j]
		if line_f != line: flag = True
	log_field()
	#Если был хоть один сдвиг, то спавним новую плитку
	if flag: after_move()	
	draw_field(field)

#Движение вправо
def right_dir(event):
	print('RIGHT SHIFT', file = log_file)
	flag = False
	for i in range(len(field)):
		#Формируем линию которую сдвигаем
		line = field[i]
		line_f = field[i]
		line = list(filter(lambda el : el != None, line))
		el = 0
		#Делаем сдвиг по линии
		while el < len(line) - 1:
			if line[el] == line[el + 1] and line[el] != None:
				line[el + 1] *= 2
				line[el] = None
				if DEBUG_MODE:
					print(f'NEW TILE {line[el + 1]} GENERATED AFTER ADDITION', file = log_file)
				el += 1
			el += 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.insert(0, None)
		field[i] = line
		if line_f != line: flag = True
	log_field()
	#Если был хоть один сдвиг, то спавним новую плитку
	if flag: after_move()
	draw_field(field)

#Движение влево
def left_dir(event):
	print('LEFT SHIFT', file = log_file)
	flag = False
	for i in range(len(field)):
		#Формируем линию которую сдвигаем
		line = field[i]
		line_f = field[i]
		line = list(filter(lambda el : el != None, line))
		el = len(line) - 1
		#Делаем сдвиг по линии
		while el > 0:
			if line[el] == line[el - 1] and line[el] != None:
				line[el - 1] *= 2
				line[el] = None
				if DEBUG_MODE:
					print(f'NEW TILE {line[el - 1]} GENERATED AFTER ADDITION', file = log_file)
				el -= 1
			el -= 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.append(None)
		field[i] = line
		if line_f != line: flag = True
	log_field()
	#Если был хоть один сдвиг, то спавним новую плитку
	if flag: after_move()
	draw_field(field)	

#Отрисовываем поле в начале игры
draw_field(field)

#При нажатии на одну из стрелочек вызываем соответствующую функцию
root.bind('<Up>', up_dir)
root.bind('<Down>', down_dir)
root.bind('<Right>', right_dir)
root.bind('<Left>', left_dir)
root.mainloop()

log_file.close()