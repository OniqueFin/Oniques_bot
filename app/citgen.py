# coding=UTF-8
import os
import textwrap
import random
from time import strftime
from PIL import ImageFont
from PIL import ImageDraw
from PIL import Image

def create_cit(textto, username, trigger):

	# Форматирование сплошного текста
	textto = '«' + textto + '»'
	text = textwrap.wrap(textto, width=55)

	# Настройки
	title = u'Цитаты великих людей:'
	title_font_size = 40
	title_position = (75, 50)
	text_position = [75, 150]
	username_position = [800 - (8 * len(username)), 525]
	text_color = (255, 255, 255)
	font_size = 30
	username_font_size = 33
		
	# Шрифты
	font = ImageFont.truetype('../other/PTF56F.ttf', font_size)
	title_font = ImageFont.truetype('../other/RobotoCondensed-Regular.ttf', title_font_size)
	username_font = ImageFont.truetype('../other/RobotoCondensed-Regular.ttf', username_font_size)

	# Открывает картинку с фоном и создает для неё кисть, открывает аватарку
	img = Image.open('../other/blank.png').convert('RGBA')
	draw = ImageDraw.Draw(img)
	userpic = Image.open('../other/userpic.png').convert('RGBA')
	lion = Image.open('../other/lion.png').convert('RGBA').resize((160, 160))

	# Рисует полосочку
	draw.line([(75, 125), (919, 125)], fill=None, width=2)

	# Рисует заголовок, cамо сообщение и юзернейм
	draw.text(title_position, title, text_color, title_font)
	for i in range(0, len(text)):
		draw.text(text_position, text[i], text_color, font)
		text_position[1] += 35
	draw.text(username_position, username, fill=text_color, font=username_font)


	# Вставляет аватарку
	if trigger == True:
			img.paste(lion, (75, 400), lion)
	else:
		img.paste(userpic, (75, 400), userpic)

	# Сохраняет картинку. Если картинок слишком много - чистит папку и сохраняет
	quote_path = u'../quotes/quote_{0}'.format(strftime('%c')) + str(random.randint(0, 100)) + '.png'

	if len(os.listdir('../quotes')) <= 2500:
		img.save(quote_path, format='png')
	else:
		for file in os.listdir('quotes'):
			os.remove('../quotes/{0}'.format(file))
		img.save(quote_path, format='png')

	return quote_path
	
if __name__ == '__main__':
	test = u'TEST TEST TEST'
	create_cit(test * 30, u'TEST', False)