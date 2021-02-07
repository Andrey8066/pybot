import sqlite3

import opr

import logging

import time

from aiogram import Bot, Dispatcher, executor, types

import random

import deffuncion

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

conn = sqlite3.connect("./database/userdatabase.db")
cursor = conn.cursor()

def SQdoing(class_id, user_id, full_name, resoftest , whatwelearntest, whatwelearntest1, whatwelearntest2, whatwelearntest3,  whatwelearn, vars, reg):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      albums = (class_id, user_id, full_name, resoftest , whatwelearntest, whatwelearntest1, whatwelearntest2, whatwelearntest3, whatwelearn, vars, reg)
      cursor.execute("INSERT INTO userdata VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 0)", albums)
      conn.commit()
def fSQsavewhatwelearntest(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET whatwelearntest =? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def fSQsavewhatwelearntest1(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET whatwelearntest1 =? WHERE user_id = ?", [smt, user_id])
      conn.commit()

def fSQsavewhatwelearntest2(user_id, smt):
            conn = sqlite3.connect("./database/userdatabase.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE userdata SET whatwelearntest2 =? WHERE user_id = ?", [smt, user_id])
            conn.commit()
def fSQsavewhatwelearntest3(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET whatwelearntest3 =? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def SQsaveresoftest(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET resoftest = ? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def SQsaveresoftest(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET variant = ? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def SQsavewhatwelearn(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET whatwelearn =? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def SQsavevars(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET vars = ? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def SQsavereg(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET reg = ? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def SQsavevariant(user_id, smt):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("UPDATE userdata SET latest = ? WHERE user_id = ?", [smt, user_id])
      conn.commit()
def SQgiving(user_id, full_name):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ? and full_name = ?", [user_id, full_name])
      all_results = (cursor.fetchall())
      return all_results
def SQgivingstandart(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      standart = []
      for i in range(0, 3):
            idontknowname = int(8 + i)
            standart.append(voc[idontknowname])
      print(standart)
      return standart
def SQgivingwhatwelearn(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      whatwelearn = voc[8]
      return whatwelearn
def SQgivingwhatwelearntest(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      whatwelearntest = voc[4]
      return whatwelearntest
def SQgivingwhatwelearntest1(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      whatwelearntest = voc[5]
      return whatwelearntest
def SQgivingwhatwelearntest2(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      whatwelearntest = voc[6]
      return whatwelearntest
def SQgivingwhatwelearntest3(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      whatwelearntest = voc[7]
      return whatwelearntest
def SQgivingvars(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      vars = voc[9]
      return vars
def SQgivingreg(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      try:
            voc = all_results[0]
            reg = voc[10]
      except IndexError:
            reg = True
      return reg
def SQgivingresoftest(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      resoftest = voc[3]
      return resoftest
def SQgivingvariant(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      resoftest = voc[11]
      return resoftest
def SQgivingclass_id(user_id):
      conn = sqlite3.connect("./database/userdatabase.db")
      cursor = conn.cursor()
      cursor.execute("SELECT * FROM userdata  WHERE user_id = ?", [user_id])
      all_results = cursor.fetchall()
      opr.ressql = all_results
      voc = all_results[0]
      class_id = voc[0]
      return class_id


def test_variant(usrid, opr, nextstep, topic, question):
      testvariant = random.randint(0, 5)
      while testvariant ==deffuncion.SQgivingvariant(usrid):
            testvariant = random.randint(0, 5)
      testcard = opr.TEST.get(topic)
      testquestion = testcard.get(question)
      deffuncion.SQsavewhatwelearn(usrid, nextstep)
      deffuncion.SQsavevariant(usrid, testvariant)

      return str(testquestion[testvariant])

def test_variantvars(usrid, opr, nextstep, topic, question):
      testvariant = random.randint(0, 5)
      while testvariant ==deffuncion.SQgivingvariant(usrid):
            testvariant = random.randint(0, 5)
      testcard = opr.TEST.get(topic)
      testquestion = testcard.get(question)
      deffuncion.SQsavevars(usrid, nextstep)
      deffuncion.SQsavevariant(usrid, testvariant)

      return str(testquestion[testvariant])

def test_check(usrid, al, opr, topic, question):
      testcard = opr.TEST_ANSWERS.get(topic)
      testquestion = testcard.get(question)
      print("Время запроса: {}.\nПользователь {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(),usrid,topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
      with open("testlog.txt", "a") as log:
            log.write("Время запроса: {}.\nПользователя {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(),usrid,topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
            log.close()
      if al == testquestion[deffuncion.SQgivingvariant(usrid)]:
            print(deffuncion.SQgivingwhatwelearntest(usrid))
            deffuncion.fSQsavewhatwelearntest(usrid, (int(deffuncion.SQgivingwhatwelearntest(usrid)) + 1))
            return True
      else:
            return False

def test_check1(usrid, al, opr, topic, question):
      testcard = opr.TEST_ANSWERS.get(topic)
      testquestion = testcard.get(question)
      print("Время запроса: {}.\nПользователь {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(),usrid,topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
      with open("testlog.txt", "a") as log:
            log.write("Время запроса: {}.\nПользователь {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(), usrid, topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
            log.close()
      if al == testquestion[deffuncion.SQgivingvariant(usrid)]:
            print(deffuncion.SQgivingwhatwelearntest1(usrid))
            deffuncion.fSQsavewhatwelearntest1(usrid, (int(deffuncion.SQgivingwhatwelearntest1(usrid)) + 1))
            return True
      else:
            return False

def test_check2(usrid, al, opr, topic, question):
      testcard = opr.TEST_ANSWERS.get(topic)
      testquestion = testcard.get(question)
      print("Время запроса: {}.\nПользователь {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(),usrid,topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
      with open("testlog.txt", "a") as log:
            log.write("Время запроса: {}.\nПользователь {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(), usrid, topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
            log.close()
      if al == testquestion[deffuncion.SQgivingvariant(usrid)]:
            print(deffuncion.SQgivingwhatwelearntest2(usrid))
            deffuncion.fSQsavewhatwelearntest2(usrid, (int(deffuncion.SQgivingwhatwelearntest2(usrid)) + 1))
            return True
      else:
            return False

def test_check3(usrid, al, opr, topic, question):
      testcard = opr.TEST_ANSWERS.get(topic)
      testquestion = testcard.get(question)
      print("Время запроса: {}.\nПользователь {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(),usrid,topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
      with open("testlog.txt", "a") as log:
            log.write("Время запроса: {}.\nПользователь {}.\nТест {}.\nВопрос {}.\nОтвет {}, правильный ответ {}\n".format(time.ctime(),usrid, topic, question, al, testquestion[deffuncion.SQgivingvariant(usrid)]))
            log.close()
      if al == testquestion[deffuncion.SQgivingvariant(usrid)]:
            print(deffuncion.SQgivingwhatwelearntest3(usrid))
            deffuncion.fSQsavewhatwelearntest3(usrid, (int(deffuncion.SQgivingwhatwelearntest3(usrid)) + 1))

            return True
      else:
            return False