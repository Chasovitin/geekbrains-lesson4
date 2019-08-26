# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и
# фамилия должны иметь заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

# a = input(" введите имя ")
# b = input ("введите фамилию")
# с = input ("введите  email")

import re


print('начало регистрации')/n ("1)Имя и Фамимилия должны начинаться с заглавной буквы/п')")/n

user_name = input(" введите имя ")
user_sname = input('Ваша Фамилия?: ')
user_email = input('Введите ваш адрес email: ')
if re.match('^[А-Я]{1,1}',user_name) is not  None:
    if re.match('^[А-Я]{1,1}', user_sname) is not None:
        if re.findall('[a-z, 0-9]+@+[a-z 0-9]+\.(ru|com|org)', user_name) is not None:
            print('Добро пожаловать, {} {}! Ваш почтовый адрес: {}'.format(user_name, user_sname, user_email))
else:
    print('Вы ввели неверные данные')



# # Задача - 2:
# # Вам дан текст:
#



some_str = '''
Мороз и солнце; день чудесный!
Еще ты дремлешь, друг прелестный —
Пора, красавица, проснись:
Открой сомкнуты негой взоры
Навстречу северной Авроры,
Звездою севера явись!
Вечор, ты помнишь, вьюга злилась,
На мутном небе мгла носилась;
Луна, как бледное пятно,
Сквозь тучи мрачные желтела,
И ты печальная сидела —
А нынче... погляди в окно:
Под голубыми небесами
Великолепными коврами,
Блестя на солнце, снег лежит;
Прозрачный лес один чернеет,
И ель сквозь иней зеленеет,
И речка подо льдом блестит.
Вся комната янтарным блеском
Озарена. Веселым треском
Трещит затопленная печь.
Приятно думать у лежанки.
Но знаешь: не велеть ли в санки
Кобылку бурую запречь?
Скользя по утреннему снегу,
Друг милый, предадимся бегу
Нетерпеливого коня
И навестим поля пустые,
Леса, недавно столь густые,
И берег, милый для меня.'''

findintext = r"\.\."

allresults = re.findall(findintext, some_str)

print (allresults)



# Необходимо с помощью регулярных выражений определить есть ли в тексте подряд
# # более одной точки, при любом исходе сообщите результат пользователю!