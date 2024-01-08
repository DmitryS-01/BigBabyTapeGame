from turtle import *
from random import choice, randint
import requests
import re


# проверка на меткость
def is_button(x, y):
    goto(x, y)
    if -1.35 * delta <= x <= 1.35 * delta and -0.05 * delta <= y <= 0.45 * delta:
        clear()
        Screen().bgcolor('grey10')
        Screen().onclick(b_b_t)


# тейпи
def b_b_t(x, y):
    goto(x, y)
    color(choice(colors))
    try:
        string = next(text)
        write(string, False, 'center', (choice(fonts), randint(5, 15), 'bold'))
    except StopIteration:
        clear()
        write(f'''теперь ты не позер, поздравляю
              ну а еще я теперь знаю твой ip: {ip}''', False, 'center', ('calibri', 25, 'bold'))


# настройки

side = 720
Screen().setup(side, side)
Screen().title('big boss benzo 0.1')
Screen().bgcolor('dodgerblue')
speed(0)
hideturtle()
pu()


# ip

html = requests.get('https://2ip.ru').text
pattern = r'\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}'
ip = re.search(pattern, html).group()


start_button = '[кольнуться]'
button_color = 'ivory1'

fonts = ['calibri', 'arial', 'times new roman', 'courier', 'georgia', 'verdana', 'helvetica', 'comic sans ms']
colors = ['#FF0000', '#FF3300', '#FF6600', '#FF9900', '#FFCC00', '#FFFF00', '#CCFF00', '#99FF00', '#66FF00', '#33FF00',
          '#00FF00', '#00FF33', '#00FF66', '#00FF99', '#00FFCC', '#00FFFF', '#00CCFF', '#0099FF', '#0066FF', '#0033FF',
          '#0000FF', '#3300FF', '#6600FF']

song = '''DJ Tape
Damn, Aarne goin' crazy
Эй, эй, эй
Я не могу лизать пизду — у меня виниры, baby
У нас есть бомбы, мама, мы бомбардиры, baby (бум)
Escalade большой паркую на бордюры, baby
Это паркур, то, как я прыгнул в эти лямы, baby (эй, эй)
Я про деньги, baby, Тейпи любит лямы, baby (лямы, baby)
Тэйпа любят лямы, мами любят Тейпа, baby (йей)
Люблю маму, baby, и я люблю папу, baby (папу, baby)
Делай guap и делай fetty. P.S. С любовью, Тейпи (муа)
Раньше никто из них не верил, они гордятся Тейпом (о, да)
Миша старый, любит Camo, комод завален Bape'ом (старина)
Тупые суммы — это то, сколько я трачу в ЦУМе (дохуя)
Я проспал встречи, я звоню партнёрам в Zoom'е (Zoom)
Я пытался посчитать, сколько я заработал (эй)
Калькулятор выдал буквы, я ничё не понял (я ничё не понял)
Я люблю Настю, люблю, куплю ей скоро Birkin (Birkin)
Её так бесит, когда меня любят тупые тёлки (пум-пум)
Я чувствую себя как Санта, ведь мы курим ёлки (эй, эй, эй, эй)
Я чувствую себя как Санта, ведь мы курим ёлки (эй, эй, эй, эй)
Хо-хо-хо, jingle bells, bricks and bales (эй)
Арахис "Monkey Nuts", эти джанки Чип and Дейл
Бабушка гордится мной, ведь её внук — артист (её внук — артист)
Вся семья гордится мной, да, я протагонист (я протагонист)
Бриллиант, я дорогой камень, не аметист (да, я VV)
По приколу угнали — stolo Daewoo Matiz
Pull up, Escalade, но белый хочет себе Wraith
Я гоняю с налом, бро, и мне не нужен сейф
Удлинённый clip, Draco, baby K
Я не могу соврать: да, это был хороший день
Pull up, Escalade, но белый хочет себе Wraith
Я гоняю с налом, бро, и мне не нужен сейф
Удлинённый clip, Draco, baby K
Я не могу соврать: да, это был хороший день
Я хотел тебя набрать, но ты меня забыл
Когда я не имел ничё, скажи мне, где ты был? (Где же?)
Скажи, откуда они взялись, когда я сделал милы?
О да, я вижу их изнутри, не могу кататься с ними (у-у)
Я secur'ю этот bag, я беру на замок (на замок)
Widebody DemonHawk, мне не нужен сток
Я соскучился по маме, давно не видел блок (эй)
Да, это Aarne на бите, Тейпи накинул строк (бум)
Иногда я думаю, что я самый горячий в мире (самый)
Иногда я думаю, что я думаю лишь о сыре (cheese)
Нет, мы не похожи с ними, район меня обнимет (ай)
И я иду вперёд, мой белый, небо — это лимит (я знаю)
Я сру на индустрию, в туалете много платин
Не буду помогать им, факбой не мой приятель
Сейчас нам много платят, когда они нас видят
Раньше я носил камни, я превратил их в VV
Pull up, Escalade, но белый хочет себе Wraith
Я гоняю с налом, бро, и мне не нужен сейф
Удлинённый clip, Draco, baby K
Я не могу соврать: да, это был хороший день
Pull up, Escalade, но белый хочет себе Wraith
Я гоняю с налом, бро, и мне не нужен сейф
Удлинённый clip, Draco, baby K
Я не могу соврать: да, это был хороший день
Aarne'''

text = iter(song.split('\n'))


# замеряем размеры кнопки
# да, костыль
# но мне было похуй

start = xcor()
write(start_button, True, 'center', ('calibri', 50, 'bold'))
end = xcor()
delta = end - start


# рисуем кнопку

forward(delta * 0.25)
left(90)
forward(0.45 * delta)
left(90)

fillcolor(button_color)
begin_fill()
pd()
pensize(3)
for _ in range(2):
    forward(2.5 * delta)
    circle(0.1 * delta, 90)
    forward(0.3 * delta)
    circle(0.1 * delta, 90)
end_fill()
pu()


# текст кнопки, остальные элементы

goto(0, 0)
color('black')
write(start_button, True, 'center', ('calibri', 50, 'bold'))

goto(0.3 * side, -0.4 * side)
for letter in 'dalbaeb prodaction':
    color(choice(colors))
    write(letter, True, 'left', ('times new roman', 10, 'bold'))


# трекаем нажатие на кнопку
Screen().listen()
Screen().onclick(is_button)

done()
