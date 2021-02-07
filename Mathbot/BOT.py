import logging

import time

import opr

from aiogram import Bot, Dispatcher, executor, types

import random

import deffuncion

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from flask import make_response, Flask

token = "1318284914:AAFuzMDzTCWMiF24LXHfz-cHr8Y6RoUevVE"
bot = Bot(token=token)
app = Flask(__name__)
dp = Dispatcher(bot)
opr.timequestion = time.time()
test_input = KeyboardButton("ТЕСТ")
uchebnik = KeyboardButton("Учебник")
answer_a = KeyboardButton("А")
answer_b = KeyboardButton("Б")
answer_v = KeyboardButton("В")
obuchenie_var1 = KeyboardButton("Понял")
obuchenie_var2 = KeyboardButton("Закончить обучение")
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(test_input, uchebnik)
answer_variant = ReplyKeyboardMarkup(resize_keyboard=True).add(answer_a, answer_b, answer_v)
obuchenie_var = ReplyKeyboardMarkup(resize_keyboard=True).add(obuchenie_var1, obuchenie_var2)
logging.basicConfig(level=logging.INFO)


# Initialize bot and dispatcher


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    usrid =int(message.from_user.id)
    full_name = message.from_user.full_name
    print(deffuncion.SQgiving(usrid, full_name))
    if deffuncion.SQgiving(usrid, full_name) == []:
        await message.answer("Введи код который тебе дал классный руководитель:")
        deffuncion.SQsavereg(usrid, True)
    else:
        await message.reply(
            'Привет!\nЯ помогу тебе выучить математику!\n Что бы начать  отправь "учебник"\nЧто бы начать тестирование отправь "тест" ',
                reply_markup=greet_kb)
        deffuncion.SQsavevars(usrid, 1)
        deffuncion.SQsavewhatwelearn(usrid, 1)



@dp.message_handler()
async def echo(message):
    a = str(message.text)
    al = a.lower()
    ag = (opr.opr).get(al)
    logs = open('log.txt', 'a')
    standart = (1, 1, 0)
    timenow = time.ctime()
    usrid = int(message.from_user.id)
    print(al)
    print(ag)
    logs.write('Время запроса: {}\n'.format(timenow))
    logs.write('Текст запроса: "{}"\n'.format(al))

    if deffuncion.SQgivingreg(usrid) is True:
        deffuncion.SQdoing(int(message.text), usrid, message.from_user.full_name, 0, 0, 0, 0, 0,  1, 1, False)
        deffuncion.SQsavereg(usrid, False)
        print("Пользователь зарегистрирован:{}".format(deffuncion.SQgiving(usrid, message.from_user.full_name)))
        await message.answer(
            'Привет!\nЯ помогу тебе выучить математику!\n Что бы начать  отправь "учебник"\nЧто бы начать тестирование отправь "тест" ',
            reply_markup=greet_kb)

    else:
        pass

    if deffuncion.SQgivingvars(usrid) == 1:

            if ag == None and deffuncion.SQgivingstandart(usrid) == standart:
                    i = random.randint(0, 3)
                    if i == 0:
                            await message.answer('Ты о чем?')
                            await message.answer(
                                'Привет!\nЯ помогу тебе выучить математику!\n Что бы начать  отправь "учебник"\nЧто бы начать тестирование отправь "тест" ',
                                reply_markup=greet_kb)

                    elif i == 1:
                            await message.answer('Что ты имел в виду?')
                            await message.answer(
                                'Привет!\nЯ помогу тебе выучить математику!\n Что бы начать  отправь "учебник"\nЧто бы начать тестирование отправь "тест" ',
                                reply_markup=greet_kb)

                    elif i == 2:
                            await message.answer('Обьясни по лучше?')
                            await message.answer(
                                'Привет!\nЯ помогу тебе выучить математику!\n Что бы начать  отправь "учебник"\nЧто бы начать тестирование отправь "тест" ',
                                reply_markup=greet_kb)
                    else:
                            await message.answer('Я тебя не совсем понял')
                            await message.answer(
                                'Привет!\nЯ помогу тебе выучить математику!\n Что бы начать  отправь "учебник"\nЧто бы начать тестирование отправь "тест" ',
                                reply_markup=greet_kb)
            if al == 'тест':
                if deffuncion.SQgivingvars(usrid) == 1 and deffuncion.SQgivingreg(usrid) == 0 and deffuncion.SQgivingwhatwelearntest(usrid) + deffuncion.SQgivingwhatwelearntest1(usrid) + deffuncion.SQgivingwhatwelearntest2(usrid) + deffuncion.SQgivingwhatwelearntest3(usrid) == 0:
                    await message.answer("Ты уже проходил в школе тему 'дроби'?", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
                else:
                    deffuncion.SQgivingwhatwelearntest(usrid, 0)
                    deffuncion.SQgivingwhatwelearntest1(usrid, 0)
                    deffuncion.SQgivingwhatwelearntest2(usrid, 0)
                    deffuncion.SQgivingwhatwelearntest3(usrid, 0)
                    await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 1.5, "СЛОЖЕНИЕ", "а"))
            elif (al == "да" or al == "нет") and deffuncion.SQgivingvars(usrid) == 1 and deffuncion.SQgivingreg(usrid) == 0 and deffuncion.SQgivingwhatwelearntest(usrid) + deffuncion.SQgivingwhatwelearntest1(usrid) + deffuncion.SQgivingwhatwelearntest2(usrid) + deffuncion.SQgivingwhatwelearntest3(usrid) == 0:
                        if al == "да":
                            await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 1.5, "СЛОЖЕНИЕ", "а"))
                        elif al == "нет":
                            print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                            logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                            await message.answer("Хорошо, тогда начнем с самого простого, а именно с дробей",reply_markup=types.ReplyKeyboardRemove())
                            time.sleep(3)
                            await message.answer('Предположим, что у нас есть некоторый предмет, составленный из нескольких абсолютно одинаковых (то есть, равных) частей.')
                            time.sleep(5)
                            await message.answer('Для наглядности можно представить, например, апельсин,разрезанный на несколько равных частей. Каждую из этих равных частей, составляющих целый предмет, называют долей целого или просто долей.')
                            time.sleep(7)
                            await message.answer('Каждую из этих равных частей, составляющих целый предмет, называют долей целого или просто долей.')
                            time.sleep(4)
                            await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXmV-Tz__5Y1hyoyLQpnrtIeXSuWenAAKxsTEbG6WYSNoHGx5yrg76l-EUmC4AAwEAAwIAA20AA7gpAgABGwQ")
                            time.sleep(3)
                            await message.answer('В зависимости от количества долей, составляющих целый предмет, эти доли имеют свои названия.')
                            time.sleep(4)
                            await message.answer('Разберем названия долей.')
                            time.sleep(2)
                            await message.answer('Если предмет составляют две доли, любая из них называется одна вторая доля или половина целого предмета; ')
                            time.sleep(4)
                            await message.answer('Если предмет составляют три доли, то любая из них называется одна третья доля или треть.')
                            time.sleep(4)
                            await message.answer('Если предмет составляют четыре доли, то любая из них называется одна четвертая доля или четверть, и так далее.')
                            time.sleep(4)
                            await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXm1-T0Am3-NX_TKzYGF0OktXH3DHKAAKysTEbG6WYSJdN6H41AAFqzQSS5ZcuAAMBAAMCAANtAAPsMgIAARsE")
                            time.sleep(6)
                            await  message.answer('Для описания количества долей используются обыкновенные дроби. Приведем пример, который позволит нам подойти к определению обыкновенных дробей.')
                            time.sleep(6)
                            await message.answer('Пусть апельсин состоит из 12 долей. Каждая доля в этом случае представляет одну двенадцатую долю целого апельсина, то есть, 1/12. Две доли обозначим как 2/12, три доли – как 3/12, и так далее, 12 долей обозначим как 12/12. Каждую из приведенных записей называют обыкновенной дробью.')
                            time.sleep(15)
                            await message.answer('Теперь дадим общее определение обыкновенных дробей.')
                            time.sleep(3)
                            await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXnV-T0BAYVWgUSmtj2HQCFtT4pt1PAAKzsTEbG6WYSHauR26x2QZR4vHAly4AAwEAAwIAA20AA5H_AQABGwQ")
                            time.sleep(10)
                            await message.answer("Натуральные числа-числа, которые используют для счета; например 1, 2 или 3")
                            time.sleep(4)
                            await message.answer('Осталось обговорить смысл, заключенный в числителе и знаменателе обыкновенной дроби.')
                            time.sleep(4)
                            await message.answer('Знаменатель дроби показывает, из скольких долей состоит один предмет, числитель в свою очередь указывает количество таких долей. Например, знаменатель 5 дроби 12/5 означает, что один предмет состоит из пяти долей, а числитель 12 означает, что взято 12 таких долей.')
                            time.sleep(12)
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUO1-NpNSDCSyZBtTL4pSqceLK7egfAAJjCQACk3BxSB1k6PR5l8pAGwQ")
                            time.sleep(15)
                            await message.answer("Если ты понял тему", reply_markup=obuchenie_var)
                            deffuncion.SQsavewhatwelearn(usrid, 2)
                        else:
                            await message.answer('Я тебя не совсем понял')

            elif al == 'учебник' or deffuncion.SQgivingwhatwelearn(usrid) >= 1:
                    if al == 'учебник':
                        if deffuncion.SQgivingvars(usrid) == 1 and deffuncion.SQgivingreg(usrid) == 0 and deffuncion.SQgivingwhatwelearntest(usrid) + deffuncion.SQgivingwhatwelearntest1(usrid) + deffuncion.SQgivingwhatwelearntest2(usrid) + deffuncion.SQgivingwhatwelearntest3(usrid) == 0:
                            await message.answer("Ты уже проходил в школе тему 'дроби'?", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add("Да", "Нет"))
                        elif deffuncion.SQgivingvars(usrid) == 1 and deffuncion.SQgivingreg(usrid) == 0 and deffuncion.SQgivingwhatwelearntest(usrid) + deffuncion.SQgivingwhatwelearntest1(usrid) + deffuncion.SQgivingwhatwelearntest2(usrid) + deffuncion.SQgivingwhatwelearntest3(usrid) != 0:
                            print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                            logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                            await message.answer("Хорошо, тогда начнем с самого простого, а именно с дробей", reply_markup=types.ReplyKeyboardRemove())
                            time.sleep(3)
                            await message.answer('Предположим, что у нас есть некоторый предмет, составленный из нескольких абсолютно одинаковых (то есть, равных) частей.')
                            time.sleep(5)
                            await message.answer('Для наглядности можно представить, например, апельсин,разрезанный на несколько равных частей. Каждую из этих равных частей, составляющих целый предмет, называют долей целого или просто долей.')
                            time.sleep(7)
                            await message.answer('Каждую из этих равных частей, составляющих целый предмет, называют долей целого или просто долей.')
                            time.sleep(4)
                            await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXmV-Tz__5Y1hyoyLQpnrtIeXSuWenAAKxsTEbG6WYSNoHGx5yrg76l-EUmC4AAwEAAwIAA20AA7gpAgABGwQ")
                            time.sleep(3)
                            await message.answer('В зависимости от количества долей, составляющих целый предмет, эти доли имеют свои названия.')
                            time.sleep(4)
                            await message.answer('Разберем названия долей.')
                            time.sleep(2)
                            await message.answer('Если предмет составляют две доли, любая из них называется одна вторая доля или половина целого предмета; ')
                            time.sleep(4)
                            await message.answer('Если предмет составляют три доли, то любая из них называется одна третья доля или треть.')
                            time.sleep(4)
                            await message.answer('Если предмет составляют четыре доли, то любая из них называется одна четвертая доля или четверть, и так далее.')
                            time.sleep(4)
                            await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXm1-T0Am3-NX_TKzYGF0OktXH3DHKAAKysTEbG6WYSJdN6H41AAFqzQSS5ZcuAAMBAAMCAANtAAPsMgIAARsE")
                            time.sleep(6)
                            await  message.answer('Для описания количества долей используются обыкновенные дроби. Приведем пример, который позволит нам подойти к определению обыкновенных дробей.')
                            time.sleep(6)
                            await message.answer('Пусть апельсин состоит из 12 долей. Каждая доля в этом случае представляет одну двенадцатую долю целого апельсина, то есть, 1/12. Две доли обозначим как 2/12, три доли – как 3/12, и так далее, 12 долей обозначим как 12/12. Каждую из приведенных записей называют обыкновенной дробью.')
                            time.sleep(15)
                            await message.answer('Теперь дадим общее определение обыкновенных дробей.')
                            time.sleep(3)
                            await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXnV-T0BAYVWgUSmtj2HQCFtT4pt1PAAKzsTEbG6WYSHauR26x2QZR4vHAly4AAwEAAwIAA20AA5H_AQABGwQ")
                            time.sleep(10)
                            await message.answer("Натуральные числа-числа, которые используют для счета; например 1, 2 или 3")
                            time.sleep(4)
                            await message.answer('Осталось обговорить смысл, заключенный в числителе и знаменателе обыкновенной дроби.')
                            time.sleep(4)
                            await message.answer('Знаменатель дроби показывает, из скольких долей состоит один предмет, числитель в свою очередь указывает количество таких долей. Например, знаменатель 5 дроби 12/5 означает, что один предмет состоит из пяти долей, а числитель 12 означает, что взято 12 таких долей.')
                            time.sleep(12)
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUO1-NpNSDCSyZBtTL4pSqceLK7egfAAJjCQACk3BxSB1k6PR5l8pAGwQ")
                            time.sleep(15)
                            await message.answer("Если ты понял тему", reply_markup=obuchenie_var)
                            deffuncion.SQsavewhatwelearn(usrid, 2)
                        else:
                            await message.answer("Ты о чём?")
                    elif (al == "да" or al == "нет") and deffuncion.SQgivingvars(usrid) == 1 and deffuncion.SQgivingreg(usrid) == 0  and deffuncion.SQgivingwhatwelearntest(usrid) + deffuncion.SQgivingwhatwelearntest1(usrid) + deffuncion.SQgivingwhatwelearntest2(usrid) + deffuncion.SQgivingwhatwelearntest3(usrid) == 0:
                        if al == "да":
                            await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 2, "СЛОЖЕНИЕ", "а"))
                        elif al == "нет":
                            print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                            logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                            await message.answer("Хорошо, тогда начнем с самого простого, а именно с дробей", reply_markup=types.ReplyKeyboardRemove())
                            time.sleep(3)
                            await message.answer('Предположим, что у нас есть некоторый предмет, составленный из нескольких абсолютно одинаковых (то есть, равных) частей.')
                            time.sleep(5)
                            await message.answer('Для наглядности можно представить, например, апельсин,разрезанный на несколько равных частей. Каждую из этих равных частей, составляющих целый предмет, называют долей целого или просто долей.')
                            time.sleep(7)
                            await message.answer('Каждую из этих равных частей, составляющих целый предмет, называют долей целого или просто долей.')
                            time.sleep(4)
                            await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXmV-Tz__5Y1hyoyLQpnrtIeXSuWenAAKxsTEbG6WYSNoHGx5yrg76l-EUmC4AAwEAAwIAA20AA7gpAgABGwQ")
                            time.sleep(3)
                            await message.answer('В зависимости от количества долей, составляющих целый предмет, эти доли имеют свои названия.')
                            time.sleep(4)
                            await message.answer('Разберем названия долей.')
                            time.sleep(2)
                            await message.answer('Если предмет составляют две доли, любая из них называется одна вторая доля или половина целого предмета; ')
                            time.sleep(4)
                            await message.answer('Если предмет составляют три доли, то любая из них называется одна третья доля или треть.')
                            time.sleep(4)
                            await message.answer('Если предмет составляют четыре доли, то любая из них называется одна четвертая доля или четверть, и так далее.')
                            time.sleep(4)
                            await bot.send_photo(message.from_user.id,photo="AgACAgIAAxkBAAIXm1-T0Am3-NX_TKzYGF0OktXH3DHKAAKysTEbG6WYSJdN6H41AAFqzQSS5ZcuAAMBAAMCAANtAAPsMgIAARsE")
                            time.sleep(6)
                            await  message.answer('Для описания количества долей используются обыкновенные дроби. Приведем пример, который позволит нам подойти к определению обыкновенных дробей.')
                            time.sleep(6)
                            await message.answer('Пусть апельсин состоит из 12 долей. Каждая доля в этом случае представляет одну двенадцатую долю целого апельсина, то есть, 1/12. Две доли обозначим как 2/12, три доли – как 3/12, и так далее, 12 долей обозначим как 12/12. Каждую из приведенных записей называют обыкновенной дробью.')
                            time.sleep(15)
                            await message.answer('Теперь дадим общее определение обыкновенных дробей.')
                            time.sleep(3)
                            await bot.send_photo(message.from_user.id,photo="AgACAgIAAxkBAAIXnV-T0BAYVWgUSmtj2HQCFtT4pt1PAAKzsTEbG6WYSHauR26x2QZR4vHAly4AAwEAAwIAA20AA5H_AQABGwQ")
                            time.sleep(10)
                            await message.answer("Натуральные числа-числа, которые используют для счета; например 1, 2 или 3")
                            time.sleep(4)
                            await message.answer('Осталось обговорить смысл, заключенный в числителе и знаменателе обыкновенной дроби.')
                            time.sleep(4)
                            await message.answer('Знаменатель дроби показывает, из скольких долей состоит один предмет, числитель в свою очередь указывает количество таких долей. Например, знаменатель 5 дроби 12/5 означает, что один предмет состоит из пяти долей, а числитель 12 означает, что взято 12 таких долей.')
                            time.sleep(12)
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUO1-NpNSDCSyZBtTL4pSqceLK7egfAAJjCQACk3BxSB1k6PR5l8pAGwQ")
                            time.sleep(15)
                            await message.answer("Если ты понял тему", reply_markup=obuchenie_var)
                            deffuncion.SQsavewhatwelearn(usrid, 2)
                    elif deffuncion.SQgivingwhatwelearn(usrid) == 2 and al == 'понял':        #Обучение дробям
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        await message.answer('Дроби делятся на три типа, в данном случае рассмотрим обыкновенные', reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(7)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXn1-T0B_7fW91PPsS6lw6KCbaZ2OVAAK0sTEbG6WYSIrGwZizFBG6PQXZli4AAwEAAwIAA20AA-XSAgABGwQ")
                        time.sleep(8)
                        await message.answer('Итак, любое натуральное число m можно представить в виде обыкновенной дроби со знаменателем 1 как m/1, а любую обыкновенную дробь вида m/1 можно заменить натуральным числом m.')
                        time.sleep(6)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXoV-T0CWVHeDIY8_erRbXwrg6ZYy3AAK1sTEbG6WYSLCma_bgh24p1Zxxly4AAwEAAwIAA20AAzE7AgABGwQ")
                        time.sleep(5)
                        await  message.answer('Очень важная вещь в дробях-дробная черта, стоит запомнить, что дробная черта обозначает деление')
                        time.sleep(3)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXo1-T0C3nwaoULRE1gYFVBxPQO3CKAAK2sTEbG6WYSMz66bYnIiCO08BImC4AAwEAAwIAA20AA-olAgABGwQ")
                        time.sleep(4)
                        await  message.answer('Чтобы сравнить дроби нужно: произведение числителя 1 дроби и знаменателя второй, сравнить с произведением знаменателятя 1 дроби на числитель воторой, и знак полученный в результате сравнения написать в сравнение дробей')
                        time.sleep(9)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXpV-T0DigW7LlauuT7FE2k1YKBcnMAAK3sTEbG6WYSJcpdBpCURVd808SlS4AAwEAAwIAA20AA--yBQABGwQ")
                        time.sleep(10)
                        await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUPV-NpShCsrPgwFmU00Mvv76B8DVFAAJkCQACk3BxSK1Abj7nyY_LGwQ")
                        time.sleep(15)
                        await message.answer('Дробь называется правильной если числитель больше знаменателя, в иных случаях дробь называется неправильной')
                        time.sleep(5)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIXp1-T0EUeD8pSyVU2eIVK458Z94uIAAK4sTEbG6WYSJ4WajMI-Z3Tx-0XmC4AAwEAAwIAA20AAwIqAgABGwQ")
                        time.sleep(6)
                        await message.answer("Если тебе трудно запомнить где числитель, а где знаменатель; то можешь использовать анологию: Человек на Земле")
                        time.sleep(7)
                        await message.answer("Человек это Числитель, а Земля Знаменатель, то есть просто по первым буквам")
                        time.sleep(8)
                        await message.answer("Если ты понял тему", reply_markup=obuchenie_var)
                        deffuncion.SQsavewhatwelearn(usrid, 3)


                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3  and al == 'понял':        #Обучение сложению и вычитанию дробей дробей
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        await message.answer("Существует 4 основных действий с дробями: сложение, вычитание, деление, умножение.", reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(3)
                        await message.answer("Для начала рассмотрим сложение:")
                        time.sleep(2)
                        await message.answer("Сложение делится на два подпункта: с одинаковым знаменателем и с различным.")
                        time.sleep(3)
                        await message.answer("Для начала рассмотрим сложение дробей с одинаковым знаменателем:")
                        time.sleep(3)
                        await message.answer("Для сложение дробей с одинаковым знаменателем нужно: сложить числитель первой и второй дроби, а знаменатель оставить прежним")
                        time.sleep(5)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIYD1-T0muH4u1BJWkf_9xvqiXfJBYeAAKwrjEbf6GgSAjn4Bv040Ip--sXmC4AAwEAAwIAA20AA6YsAgABGwQ")
                        time.sleep(5)
                        await message.answer("Теперь рассмотрим сложение дробей с разным знаменателем.")
                        time.sleep(3)
                        await message.answer("Для этого нужно:")
                        time.sleep(2)
                        await message.answer("1) привести дроби к наименьшему общему знаменателю;")
                        time.sleep(3)
                        await message.answer("2) выполнить сложение;")
                        time.sleep(2)
                        await bot.send_video(chat_id=message.from_user.id, video="BAACAgIAAxkBAAIoN1_AGaPw5Bh7n3R0vXrFgWNBh38zAAJuCAACMgEBSgxYUcQcVS_JHgQ", caption="Для лучшего понимания мы рекомендуем ознакомиться с данным видео.")
                        time.sleep(15)
                        await message.answer('А теперь пройди тестирование: ')
                        time.sleep(3)
                        testvariant = random.randint(0, 2)
                        await bot.send_photo(chat_id=message.from_user.id, photo=((opr.TEST.get("СЛОЖЕНИЕ")).get("тст")[testvariant]))
                        await message.answer("Варианты ответа", reply_markup=answer_variant)
                        deffuncion.SQsavevariant(usrid, testvariant)
                        deffuncion.SQsavewhatwelearn(usrid, 3.05)
                        deffuncion.fSQsavewhatwelearntest(usrid, 0)

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.05:
                        if al == "а":
                            deffuncion.fSQsavewhatwelearntest(usrid, (int(deffuncion.SQgivingwhatwelearntest(usrid)) + 1))
                        else:
                            pass
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 3.07, "СЛОЖЕНИЕ", "а"), reply_markup=types.ReplyKeyboardRemove())

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.07:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 3.1, "СЛОЖЕНИЕ", "а"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.1:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 3.12, "СЛОЖЕНИЕ", "б"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.12:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "б")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 3.15, "СЛОЖЕНИЕ", "б"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.15:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "б")
                        await bot.send_photo(chat_id=message.from_user.id,photo=deffuncion.test_variant(usrid, opr, 3.17, "СЛОЖЕНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.17:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 3.2, "СЛОЖЕНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.2:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 3.22, "СЛОЖЕНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.22:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "г")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 3.25, "СЛОЖЕНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 3.25:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "г")
                        await message.answer("Результат теста:{} из 9".format(deffuncion.SQgivingwhatwelearntest(usrid)))
                        if deffuncion.SQgivingwhatwelearntest(usrid) <= 4:
                            await message.answer("Так как ты написал тест на неудовлетворительный бал, посмотри теорию и  видео-обьяснение, и попробуй еще раз.")
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUP1-NpW-RN6j2WVkAATu907IQfPCIEwACZQkAApNwcUg_rXlog484bhsE")
                            time.sleep(15)
                            deffuncion.SQsavewhatwelearn(usrid, 3)
                        elif deffuncion.SQgivingwhatwelearntest(usrid) > 4 and deffuncion.SQgivingwhatwelearntest(usrid) < 8:
                            await message.answer("Ты написал тест на удовлетворительный бал, посмотри видео-обьяснение, и попробуй еще раз.")
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUP1-NpW-RN6j2WVkAATu907IQfPCIEwACZQkAApNwcUg_rXlog484bhsE")
                            await message.answer('А теперь пройди тестирование.')
                            testvariant = random.randint(0, 2)
                            await bot.send_photo(chat_id=message.from_user.id, photo=((opr.TEST.get("СЛОЖЕНИЕ")).get("тст")[testvariant]))
                            await message.answer("Варианты ответа", reply_markup=answer_variant)
                            deffuncion.SQsavevariant(usrid, testvariant)
                            deffuncion.SQsavewhatwelearn(usrid, 3.05)
                            deffuncion.fSQsavewhatwelearntest(usrid, 0)
                        else:
                            if deffuncion.SQgivingwhatwelearntest1(usrid) < 6:
                                deffuncion.SQsavewhatwelearn(usrid, 4)
                            else:
                                if deffuncion.SQgivingwhatwelearntest2(usrid) < 6:
                                    deffuncion.SQsavewhatwelearn(usrid, 5)
                                else:
                                    if deffuncion.SQgivingwhatwelearntest3(usrid) < 6:
                                        deffuncion.SQsavewhatwelearn(usrid, 6)
                                    else:
                                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 1.5, "СЛОЖЕНИЕ", "а"))
                            await message.answer("Если ты понял тему", reply_markup=obuchenie_var)
                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4 and al == 'понял':        #Обучение сложению и вычитанию дробей дробей
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        await message.answer("Рассмотрим вычитание.", reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(2)
                        await message.answer("Вычитание как и сложение бывает с одинаковыми знаменателеми и с разными.")
                        time.sleep(3)
                        await message.answer("Для вычитания дробей с одинаковым знаменателем нужно из числителя первой дроби вычесть числитель второй дроби, а знаменатель оставить прежним")
                        time.sleep(6)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIn11_AFS5eKuqYRiUS4dE4qTTFXFJXAALerzEbMgEBSqVwg89x4EIkfM5emi4AAwEAAwIAA20AA8RbAQABHgQ")
                        time.sleep(5)
                        await message.answer("Теперь рассмотрим вычитание дробей с разными знаменателями.")
                        time.sleep(3)
                        await message.answer("Для этого нужно:")
                        time.sleep(2)
                        await message.answer("1) привести дроби к наименьшему общему знаменателю;")
                        time.sleep(3)
                        await message.answer("2) выполнить вычитание")
                        time.sleep(2)
                        await bot.send_video(chat_id=message.from_user.id, video="BAACAgIAAxkBAAIoOl_AGhUEkI6MSpIFVRtemk06YIX9AAJvCAACMgEBSmm1eQJqEHIIHgQ", caption="Для лучшего понимания мы рекомендуем ознакомится с данным видео.")
                        time.sleep(10)
                        await message.answer('А теперь пройди тестирование.')
                        time.sleep(2)
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.05, "ВЫЧИТАНИЕ", "а"))

                        deffuncion.SQsavewhatwelearn(usrid, 4.05)
                        deffuncion.fSQsavewhatwelearntest1(usrid, 0)

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.05:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.07, "ВЫЧИТАНИЕ", "а"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.07:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.1, "ВЫЧИТАНИЕ", "б"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.1:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "б")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.12, "ВЫЧИТАНИЕ", "б"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.12:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "б")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.15, "ВЫЧИТАНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.15:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id,photo=deffuncion.test_variant(usrid, opr, 4.17, "ВЫЧИТАНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.17:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.2, "ВЫЧИТАНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.2:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "г")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.25, "ВЫЧИТАНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 4.25:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "г")
                        await message.answer("Результат теста:{} из 8".format(deffuncion.SQgivingwhatwelearntest1(usrid)))
                        if deffuncion.SQgivingwhatwelearntest1(usrid) <= 4:
                            await message.answer("Так как ты написал тест на неудовлетворительный бал, посмотри теорию и  видео-обьяснение, и попробуй еще раз.")
                            time.sleep(5)
                            deffuncion.SQsavewhatwelearn(usrid, 4)
                        elif deffuncion.SQgivingwhatwelearntest1(usrid) > 4 and deffuncion.SQgivingwhatwelearntest1(usrid) < 7:
                            await message.answer("Ты написал тест на удовлетворительный бал, посмотри видео-обьяснение, и попробуй еще раз.")
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIoOl_AGhUEkI6MSpIFVRtemk06YIX9AAJvCAACMgEBSmm1eQJqEHIIHgQ")
                            await message.answer('А теперь пройди тестирование.')
                            await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 4.05, "ВЫЧИТАНИЕ", "а"))
                            deffuncion.fSQsavewhatwelearntest1(usrid, 0)
                        else:
                            if deffuncion.SQgivingwhatwelearntest2(usrid) < 6:
                                deffuncion.SQsavewhatwelearn(usrid, 5)
                            else:
                                if deffuncion.SQgivingwhatwelearntest3(usrid) < 6:
                                    deffuncion.SQsavewhatwelearn(usrid, 6)
                                else:
                                    await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 1.5, "СЛОЖЕНИЕ", "а"))
                            await message.answer("Если ты понял тему", reply_markup=obuchenie_var)
                        await message.answer("Если ты понял тему", reply_markup=obuchenie_var)
                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5 and al == 'понял':  #Обучение умножению дробей
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        await message.answer("Теперь рассмотрим одно из самых простых действий - умноженение:", reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(3)
                        await message.answer("Чтобы умножить дробь на дробь, надо:")
                        time.sleep(2)
                        await message.answer("Числитель первой дроби умножить на числитель второй дроби и их произведение записать в числитель новой дроби.")
                        time.sleep(6)
                        await message.answer("Знаменатель первой дроби умножить на знаменатель второй дроби и их произведение записать в знаменатель новой дроби.")
                        time.sleep(5)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAInal-9OJUNo_Ot6rgGv1C_hkg9NYlCAAIssTEbX7ToSRTh7CxRkYrlZySlli4AAwEAAwIAA20AA2hYBAABHgQ")
                        time.sleep(5)
                        await message.answer("Если требуется умножить дробь на целое число, нужно: ")
                        time.sleep(4)
                        await message.answer("1)Число умножить на числитель дроби и записать полученное число в числитель новой дроби.")
                        time.sleep(4)
                        await message.answer("2)Знаменатель оставить от старой дроби.")
                        time.sleep(3)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIn0V--K841BFdHMJmBzcmLN5ihNUPVAAJerzEbj_vwSXYOEdr9LF5RgN1hmi4AAwEAAwIAA20AA-xKAQABHgQ")
                        time.sleep(5)
                        await message.answer('А теперь пройди тестирование.')
                        time.sleep(3)
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.05, "УМНОЖЕНИЕ", "а"))
                        deffuncion.fSQsavewhatwelearntest2(usrid, 0)

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.05:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.07, "УМНОЖЕНИЕ", "а"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.07:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.1, "УМНОЖЕНИЕ", "б"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.1:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "б")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.12, "УМНОЖЕНИЕ", "б"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.12:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "б")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.15, "УМНОЖЕНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.15:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.17, "УМНОЖЕНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.17:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.20, "УМНОЖЕНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.2:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "г")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.25, "УМНОЖЕНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 5.25:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "г")
                        await message.answer(
                            "Результат теста:{} из 8".format(deffuncion.SQgivingwhatwelearntest2(usrid)))
                        if deffuncion.SQgivingwhatwelearntest2(usrid) <= 4:
                            await message.answer(
                                "Так как ты написал тест на неудовлетворительный бал, посмотри теорию и  видео-обьяснение, и попробуй еще раз.")
                            await bot.send_video(message.from_user.id,
                                                 video="BAACAgIAAxkBAAIUP1-NpW-RN6j2WVkAATu907IQfPCIEwACZQkAApNwcUg_rXlog484bhsE")
                            time.sleep(5)
                            deffuncion.SQsavewhatwelearn(usrid, 5)
                        elif deffuncion.SQgivingwhatwelearntest2(usrid) > 4 and deffuncion.SQgivingwhatwelearntest2(usrid) < 7:
                            await message.answer("Ты написал тест на удовлетворительный бал, посмотри видео-обьяснение, и попробуй еще раз.")
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUP1-NpW-RN6j2WVkAATu907IQfPCIEwACZQkAApNwcUg_rXlog484bhsE")
                            await message.answer('А теперь пройди тестирование.')
                            await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 5.05, "УМНОЖЕНИЕ", "а"))
                            deffuncion.fSQsavewhatwelearntest2(usrid, 0)
                        else:
                            if deffuncion.SQgivingwhatwelearntest3(usrid) < 6:
                                deffuncion.SQsavewhatwelearn(usrid, 6)
                            else:
                                await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 1.5, "СЛОЖЕНИЕ", "а"))
                            deffuncion.SQsavewhatwelearn(usrid, 6)
                        await message.reply("Если ты понял тему", reply_markup=obuchenie_var)
                    elif deffuncion.SQgivingwhatwelearn(usrid) == 6 and al == 'понял':  #Обучение делению дробей
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        await message.answer("И последнее действее с дробями - деление", reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(3)
                        await message.answer("Дабы выполнить деление дроби на дробь нужно:")
                        time.sleep(4)
                        await message.answer("Числитель первой дроби умножить на знаменатель второй дроби и записать произведение в числитель новой дроби.")
                        time.sleep(7)
                        await message.answer("Знаменатель первой дроби умножить на числитель второй дроби и записать произведение в знаменатель новой дроби.")
                        time.sleep(7)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAInUl-9F7Hon7prs49v0tLHMlG24IzKAAIgtDEbj_voSaTNCIPiN0_MfwNFli4AAwEAAwIAA20AA6zHBAABHgQ")
                        time.sleep(7)
                        await message.answer("Если требуется разделить число на дробь или наоборот то прежде чем умножить нужно число предствить в виде дроби.")
                        time.sleep(7)
                        await message.answer("А после выполнять действия по выше описанному алгоритму.")
                        time.sleep(4)
                        await message.answer("Знаменатель оставить от старой дроби.")
                        time.sleep(3)
                        await bot.send_photo(message.from_user.id, photo="AgACAgIAAxkBAAIn1F--OR-CjIX5r4cYjt0gTUJtnGczAAJurzEbj_vwSUpsnigw27ZJJrJFmC4AAwEAAwIAA20AA9x9AwABHgQ")
                        deffuncion.SQsavewhatwelearn(usrid, 6.05)
                        time.sleep(7)
                        await message.answer('А теперь пройди тестирование.')
                        time.sleep(3)
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 6.05, "ДЕЛЕНИЕ", "а"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 6.05:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 6.07, "ДЕЛЕНИЕ", "а"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 6.07:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "а")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 6.15, "ДЕЛЕНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 6.15:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 6.17, "ДЕЛЕНИЕ", "в"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 6.17:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "в")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 6.2, "ДЕЛЕНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 6.2:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "г")
                        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 6.25, "ДЕЛЕНИЕ", "г"))

                    elif deffuncion.SQgivingwhatwelearn(usrid) == 6.25:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "г")
                        await message.answer("Результат теста:{} из 8".format(deffuncion.SQgivingwhatwelearntest3(usrid)))
                        if deffuncion.SQgivingwhatwelearntest3(usrid) <= 4:
                            await message.answer("Так как ты написал тест на неудовлетворительный бал, посмотри теорию и попробуй еще раз.")
                            deffuncion.SQsavewhatwelearn(usrid, 6)
                            await message.reply("Если ты понял тему", reply_markup=obuchenie_var)
                        elif deffuncion.SQgivingwhatwelearntest3(usrid) > 4 and deffuncion.SQgivingwhatwelearntest3(usrid) < 7:
                            await message.answer("Ты написал тест на удовлетворительный бал, посмотри видео-обьяснение, и попробуй еще раз.")
                            await bot.send_video(message.from_user.id, video="BAACAgIAAxkBAAIUP1-NpW-RN6j2WVkAATu907IQfPCIEwACZQkAApNwcUg_rXlog484bhsE")
                            time.sleep(10)
                            await message.answer('А теперь пройди тестирование.')
                            await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variant(usrid, opr, 6.05, "ДЕЛЕНИЕ", "а"))
                            deffuncion.fSQsavewhatwelearntest3(usrid, 0)
                        else:
                            await message.answer("Ты даун")
                            deffuncion.SQsavewhatwelearn(usrid, 1)
                            await message.answer(chat_id=message.from_user.id, photo=(deffuncion.test_variantvars(usrid, opr, 1.5, "СЛОЖЕНИЕ", "а")))

                    elif al == 'закончить обучение' and deffuncion.SQgivingwhatwelearn(usrid) > 1:
                        await message.reply('Привет!\nЯ помогу тебе выучить математику!\n Что бы начать  отправь "учебник"\nЧто бы начать тестирование отправь "тест"', reply_markup=greet_kb)
                        deffuncion.SQsavewhatwelearn(usrid, 1)

                    else:
                        pass

    elif deffuncion.SQgivingvars(usrid) == 1.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 2, "СЛОЖЕНИЕ", "а"))
    elif deffuncion.SQgivingvars(usrid) == 2:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 2.5, "СЛОЖЕНИЕ", "б"))
    elif deffuncion.SQgivingvars(usrid) == 2.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "б")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 3, "СЛОЖЕНИЕ", "б"))
    elif deffuncion.SQgivingvars(usrid) == 3:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "б")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 3.5, "СЛОЖЕНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 3.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 4, "СЛОЖЕНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 4:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 4.5, "СЛОЖЕНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 4.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "г")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 5, "СЛОЖЕНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check(usrid, al, opr, "СЛОЖЕНИЕ", "г")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 5.5, "ВЫЧИТАНИЕ", "а"))
    elif deffuncion.SQgivingvars(usrid) == 5.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 6, "ВЫЧИТАНИЕ", "а"))
    elif deffuncion.SQgivingvars(usrid) == 6:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 6.5, "ВЫЧИТАНИЕ", "б"))
    elif deffuncion.SQgivingvars(usrid) == 6.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "б")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 7, "ВЫЧИТАНИЕ", "б"))
    elif deffuncion.SQgivingvars(usrid) == 7:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "б")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 7.5, "ВЫЧИТАНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 7.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 8, "ВЫЧИТАНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 8:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 8.5, "ВЫЧИТАНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 8.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "г")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 9, "ВЫЧИТАНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 9:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check1(usrid, al, opr, "ВЫЧИТАНИЕ", "г")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 9.5, "УМНОЖЕНИЕ", "а"))
    elif deffuncion.SQgivingvars(usrid) == 9.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 10, "УМНОЖЕНИЕ", "а"))
    elif deffuncion.SQgivingvars(usrid) == 10:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 10.5, "УМНОЖЕНИЕ", "б"))
    elif deffuncion.SQgivingvars(usrid) == 10.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "б")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 11, "УМНОЖЕНИЕ", "б"))
    elif deffuncion.SQgivingvars(usrid) == 11:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "б")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 11.5, "УМНОЖЕНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 11.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 12, "УМНОЖЕНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 12:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 12.5, "УМНОЖЕНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 12.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "г")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 13, "УМНОЖЕНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 13:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check2(usrid, al, opr, "УМНОЖЕНИЕ", "г")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 13.5, "ДЕЛЕНИЕ", "а"))
    elif deffuncion.SQgivingvars(usrid) == 13.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 14, "ДЕЛЕНИЕ", "а"))
    elif deffuncion.SQgivingvars(usrid) == 14:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "а")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 14.5, "ДЕЛЕНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 14.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id,photo=deffuncion.test_variantvars(usrid, opr, 15, "ДЕЛЕНИЕ", "в"))
    elif deffuncion.SQgivingvars(usrid) == 15:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "в")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 15.5, "ДЕЛЕНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 15.5:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "г")
        await bot.send_photo(chat_id=message.from_user.id, photo=deffuncion.test_variantvars(usrid, opr, 16, "ДЕЛЕНИЕ", "г"))
    elif deffuncion.SQgivingvars(usrid) == 16:
        print("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        logs.write("Тест, пункт {}".format(deffuncion.SQgivingvars(usrid)))
        deffuncion.test_check3(usrid, al, opr, "ДЕЛЕНИЕ", "г")
        await message.answer("Результат теста:{} из 30".format(deffuncion.SQgivingwhatwelearntest(usrid)+deffuncion.SQgivingwhatwelearntest1(usrid)+deffuncion.SQgivingwhatwelearntest2(usrid)+deffuncion.SQgivingwhatwelearntest3(usrid)))
        print("Результат теста:{} из 30".format(deffuncion.SQgivingwhatwelearntest(usrid)+deffuncion.SQgivingwhatwelearntest1(usrid)+deffuncion.SQgivingwhatwelearntest2(usrid)+deffuncion.SQgivingwhatwelearntest3(usrid)))
        logs.write("Результат теста:{} из 30".format(deffuncion.SQgivingwhatwelearntest(usrid)+deffuncion.SQgivingwhatwelearntest1(usrid)+deffuncion.SQgivingwhatwelearntest2(usrid)+deffuncion.SQgivingwhatwelearntest3(usrid)))
        deffuncion.SQsavevars(usrid, 1)
        if deffuncion.SQgivingwhatwelearntest(usrid)+deffuncion.SQgivingwhatwelearntest1(usrid)+deffuncion.SQgivingwhatwelearntest2(usrid)+deffuncion.SQgivingwhatwelearntest3(usrid) >= 0.85 * 30:
            await message.answer("Поздравляю ")
        elif deffuncion.SQgivingwhatwelearntest(usrid)+deffuncion.SQgivingwhatwelearntest1(usrid)+deffuncion.SQgivingwhatwelearntest2(usrid)+deffuncion.SQgivingwhatwelearntest3(usrid) >= 0.5 * 30 and deffuncion.SQgivingwhatwelearntest(usrid)+deffuncion.SQgivingwhatwelearntest1(usrid)+deffuncion.SQgivingwhatwelearntest2(usrid)+deffuncion.SQgivingwhatwelearntest3(usrid) < 0.85 * 30:
            if deffuncion.SQgivingwhatwelearntest(usrid) >= 6:
               if deffuncion.SQgivingwhatwelearntest1(usrid) >= 6:
                    if deffuncion.SQgivingwhatwelearntest2(usrid) < 6:
                        if deffuncion.SQgivingwhatwelearntest3(usrid) < 6:
                            pass
                        else:
                            print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn))
                            logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn))
                            await message.answer("И последнее действее с дробями - деление",
                                                 reply_markup=types.ReplyKeyboardRemove())
                            time.sleep(3)
                            await message.answer("Дабы выполнить деление дроби на дробь нужно:")
                            time.sleep(4)
                            await message.answer(
                                "Числитель первой дроби умножить на знаменатель второй дроби и записать произведение в числитель новой дроби.")
                            time.sleep(7)
                            await message.answer(
                                "Знаменатель первой дроби умножить на числитель второй дроби и записать произведение в знаменатель новой дроби.")
                            time.sleep(7)
                            await bot.send_photo(message.from_user.id,
                                                 photo="AgACAgIAAxkBAAInUl-9F7Hon7prs49v0tLHMlG24IzKAAIgtDEbj_voSaTNCIPiN0_MfwNFli4AAwEAAwIAA20AA6zHBAABHgQ")
                            time.sleep(7)
                            await message.answer(
                                "Если требуется разделить число на дробь или наоборот то прежде чем умножить нужно число предствить в виде дроби.")
                            time.sleep(7)
                            await message.answer("А после выполнять действия по выше описанному алгоритму.")
                            time.sleep(4)
                            await message.answer("Знаменатель оставить от старой дроби.")
                            time.sleep(3)
                            await bot.send_photo(message.from_user.id,
                                                 photo="AgACAgIAAxkBAAIn1F--OR-CjIX5r4cYjt0gTUJtnGczAAJurzEbj_vwSUpsnigw27ZJJrJFmC4AAwEAAwIAA20AA9x9AwABHgQ")
                            deffuncion.SQsavewhatwelearn(usrid, 6.05)
                            time.sleep(7)
                            await message.answer('А теперь пройди тестирование.')
                            time.sleep(3)
                            await bot.send_photo(chat_id=message.from_user.id,
                                                 photo=deffuncion.test_variant(usrid, opr, 6.05, "ДЕЛЕНИЕ", "а"))

                    else:
                        print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                        await message.answer("Теперь рассмотрим одно из самых простых действий - умноженение:",
                                             reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(3)
                        await message.answer("Чтобы умножить дробь на дробь, надо:")
                        time.sleep(2)
                        await message.answer(
                            "Числитель первой дроби умножить на числитель второй дроби и их произведение записать в числитель новой дроби.")
                        time.sleep(6)
                        await message.answer(
                            "Знаменатель первой дроби умножить на знаменатель второй дроби и их произведение записать в знаменатель новой дроби.")
                        time.sleep(5)
                        await bot.send_photo(message.from_user.id,
                                             photo="AgACAgIAAxkBAAInal-9OJUNo_Ot6rgGv1C_hkg9NYlCAAIssTEbX7ToSRTh7CxRkYrlZySlli4AAwEAAwIAA20AA2hYBAABHgQ")
                        time.sleep(5)
                        await message.answer("Если требуется умножить дробь на целое число, нужно: ")
                        time.sleep(4)
                        await message.answer(
                            "1)Число умножить на числитель дроби и записать полученное число в числитель новой дроби.")
                        time.sleep(4)
                        await message.answer("2)Знаменатель оставить от старой дроби.")
                        time.sleep(3)
                        await bot.send_photo(message.from_user.id,
                                             photo="AgACAgIAAxkBAAIn0V--K841BFdHMJmBzcmLN5ihNUPVAAJerzEbj_vwSXYOEdr9LF5RgN1hmi4AAwEAAwIAA20AA-xKAQABHgQ")
                        time.sleep(5)
                        await message.answer('А теперь пройди тестирование.')
                        time.sleep(3)
                        await bot.send_photo(chat_id=message.from_user.id,
                                             photo=deffuncion.test_variant(usrid, opr, 5.05, "УМНОЖЕНИЕ", "а"))
                        deffuncion.fSQsavewhatwelearntest2(usrid, 0)

               else:
                   print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                   logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                   await message.answer("Рассмотрим вычитание.", reply_markup=types.ReplyKeyboardRemove())
                   time.sleep(2)
                   await message.answer("Вычитание как и сложение бывает с одинаковыми знаменателеми и с разными.")
                   time.sleep(3)
                   await message.answer(
                       "Для вычитания дробей с одинаковым знаменателем нужно из числителя первой дроби вычесть числитель второй дроби, а знаменатель оставить прежним")
                   time.sleep(6)
                   await bot.send_photo(message.from_user.id,
                                        photo="AgACAgIAAxkBAAIn11_AFS5eKuqYRiUS4dE4qTTFXFJXAALerzEbMgEBSqVwg89x4EIkfM5emi4AAwEAAwIAA20AA8RbAQABHgQ")
                   time.sleep(5)
                   await message.answer("Теперь рассмотрим вычитание дробей с разными знаменателями.")
                   time.sleep(3)
                   await message.answer("Для этого нужно:")
                   time.sleep(2)
                   await message.answer("1) привести дроби к наименьшему общему знаменателю;")
                   time.sleep(3)
                   await message.answer("2) выполнить вычитание")
                   time.sleep(2)
                   await bot.send_video(chat_id=message.from_user.id,
                                        video="BAACAgIAAxkBAAIoOl_AGhUEkI6MSpIFVRtemk06YIX9AAJvCAACMgEBSmm1eQJqEHIIHgQ",
                                        caption="Для лучшего понимания мы рекомендуем ознакомится с данным видео.")
                   time.sleep(10)
                   await message.answer('А теперь пройди тестирование.')
                   time.sleep(2)
                   await bot.send_photo(chat_id=message.from_user.id,
                                        photo=deffuncion.test_variant(usrid, opr, 4.05, "ВЫЧИТАНИЕ", "а"))

                   deffuncion.SQsavewhatwelearn(usrid, 4.05)
                   deffuncion.fSQsavewhatwelearntest1(usrid, 0)

            else:
                print("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                logs.write("Учебник, пункт {}".format(deffuncion.SQgivingwhatwelearn(usrid)))
                await message.answer(
                    "Существует 4 основных действий с дробями: сложение, вычитание, деление, умножение.",
                    reply_markup=types.ReplyKeyboardRemove())
                time.sleep(3)
                await message.answer("Для начала рассмотрим сложение:")
                time.sleep(2)
                await message.answer("Сложение делится на два подпункта: с одинаковым знаменателем и с различным.")
                time.sleep(3)
                await message.answer("Для начала рассмотрим сложение дробей с одинаковым знаменателем:")
                time.sleep(3)
                await message.answer(
                    "Для сложение дробей с одинаковым знаменателем нужно: сложить числитель первой и второй дроби, а знаменатель оставить прежним")
                time.sleep(5)
                await bot.send_photo(message.from_user.id,
                                     photo="AgACAgIAAxkBAAIYD1-T0muH4u1BJWkf_9xvqiXfJBYeAAKwrjEbf6GgSAjn4Bv040Ip--sXmC4AAwEAAwIAA20AA6YsAgABGwQ")
                time.sleep(5)
                await message.answer("Теперь рассмотрим сложение дробей с разным знаменателем.")
                time.sleep(3)
                await message.answer("Для этого нужно:")
                time.sleep(2)
                await message.answer("1) привести дроби к наименьшему общему знаменателю;")
                time.sleep(3)
                await message.answer("2) выполнить сложение;")
                time.sleep(2)
                await bot.send_video(chat_id=message.from_user.id,
                                     video="BAACAgIAAxkBAAIoN1_AGaPw5Bh7n3R0vXrFgWNBh38zAAJuCAACMgEBSgxYUcQcVS_JHgQ",
                                     caption="Для лучшего понимания мы рекомендуем ознакомиться с данным видео.")
                time.sleep(15)
                await message.answer('А теперь пройди тестирование: ')
                time.sleep(3)
                testvariant = random.randint(0, 2)
                await bot.send_photo(chat_id=message.from_user.id,
                                     photo=((opr.TEST.get("СЛОЖЕНИЕ")).get("тст")[testvariant]))
                await message.answer("Варианты ответа", reply_markup=answer_variant)
                deffuncion.SQsavevariant(usrid, testvariant)
                deffuncion.SQsavewhatwelearn(usrid, 3.05)
                deffuncion.fSQsavewhatwelearntest(usrid, 0)

        else:
            pass


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(echo(message))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
