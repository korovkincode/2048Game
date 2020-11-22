#Движение вверх
def up_dir(field):
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
				el -= 1
			el -= 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.append(None)
		if line_f != line: flag = True
	return flag

#Движение вниз
def down_dir(field):
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
				el += 1
			el += 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.insert(0, None)
		if line_f != line: flag = True
	return flag

#Движение вправо
def right_dir(field):
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
				el += 1
			el += 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.insert(0, None)
		if line_f != line: flag = True
	return flag

#Движение влево
def left_dir(field):
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
				el -= 1
			el -= 1
		line = list(filter(lambda el : el != None, line))
		while len(line) < len(field[0]):
			line.append(None)
		if line_f != line: flag = True
	return flag