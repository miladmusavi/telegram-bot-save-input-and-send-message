import datetime
import functools
import typing

from ast import Call
from cgitb import text
from distutils.cmd import Command
from email import message
from email.headerregistry import MessageIDHeader
from http import client
from imaplib import Commands
from importlib.resources import contents
from re import X
from subprocess import call
from telnetlib import theNULL
from typing import ContextManager
from unittest import expectedFailure
import requests

from aiogram import Bot, Dispatcher, executor, types
#from aiogram import base, fields
#from aiogram import Chat, ChatType

from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.message import ContentTypes
from aiogram.bot.api import TelegramAPIServer
from aiogram.types import ContentType

import asyncio
import logging
import json

from telegram.ext import (Updater, CommandHandler, CallbackQueryHandler)
import pytz




#bot2 = Bot(token='5448480357:AAHdBnqHbP-fY4WglCAf919pxKHCRE_Yf7A', parse_mode=markdown)










bot = Bot(token='5448480357:AAHdBnqHbP-fY4WglCAf919pxKHCRE_Yf7A')
chat_id = "Ecbatanamoney"
PAYMENTS_PROVIDER_TOKEN = '123456789:TEST:1422'
dp = Dispatcher(bot)

dispatcher = dp

#bot = Client('5448480357:AAHdBnqHbP-fY4WglCAf919pxKHCRE_Yf7A')

#chat: Chat = fields.Field(dp=Chat)


logging.basicConfig(level=logging.INFO)


#echo_handler = MessageHanler(Filters.text, echo)    


telegram_auth_token= "5448480357:AAHdBnqHbP-fY4WglCAf919pxKHCRE_Yf7A"
telegram_group_id= "@Ecbatanamoney"


#keyboard1
#nemoone
button1 = InlineKeyboardButton(text="👋 euro", callback_data="euro")
button2 = InlineKeyboardButton(text="💋 button2", callback_data="randomvalue_of100")

keyboard_inline = InlineKeyboardMarkup().add(button1, button2)
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("فروش", "خرید")


#keyboard3
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("تایید", "بازگشت")
keyboard6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("تایید", "بازگشت")
keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("تایید درخواست", "بازگشت")
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("ثبت آگهی", "بازگشت",\
    "از اکباتانا")

#-------------------------------------------------------------------------------------
#nemoone dokme ha
button3 = InlineKeyboardButton(text=" button3", callback_data="تایید")
button4 = InlineKeyboardButton(text=" button4", callback_data="randomvalue_of100")

#inline keyboard2
keyboard_inlinex = InlineKeyboardMarkup().add(button1, button2)

#keyboard2
#keyboardx = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("👋 Hi!", "💋 YT")
#---------------------------------------------------------------------------------------


#keyboard5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("تماس یا ما", "بازگشت")










def ex_id (id):
    result = False
    file = open ("users.text", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result



#@bot.message_handler(commmands=['start'])
def send (message):
    if message.chat.type == 'private':
        idu = message.from_user.id
        f = open("users.txt", 'a')
        if(not ex_id(str(idu))):
            f.write("{}\n".format(idu))
            f.close()
            bot.send_message(message.chat.id, "what you need")



# farman ha



msg= f"bot online shod "



def send_msg_on_telegram(message):
    #telegram_api_url= f"wwww{telegram_auth_token}/send@{telegram_group_id}&text={message}"

    telegram_api_url= f"https://api.telegram.org/bot{telegram_auth_token}/sendMessage?chat_id={telegram_group_id}&text={message}"
    tele_res = requests.get(telegram_api_url)

    if tele_res.status_code == 200:
        print("info: notfication he has send on telegram")

    else:
        print("erro: nemitone befreste")

send_msg_on_telegram(msg)



def send (message):
    if message.chat.type == 'private':
        idu = message.from_user.id
        f = open("users.txt", 'a')
        if(not ex_id(str(idu))):
            f.write("{}\n".format(idu))
            f.close()
            bot.send_message(message.chat.id, "what you need")
        else:
            bot.send_message(message.chat.id, "Command here!")


#@dp.message_handler()
@dp.message_handler(commands=['start'])
async def welcome(message):
    khoshamdin = await message.answer("سلام من روبات اکباتانا هستم و میخواهم به شما کمک کنم تا به سرویس خود دسترسی داشته باشین:", reply_markup = keyboard3)
    print ("Client Entered: Start")





@dp.message_handler()
async def kb_answer(message: types.Message):
    #me = await bot.get_users("me")
    #status = me.status
    #khoshamdin = await message.reply("سلام من روبات اکباتانا هستم و میخواهم به شما کمک کنم تا به سرویس خود دسترسی داشته باشین:", reply_markup=keyboard3)
    print("**************** START Again ***************")





    print ("Client Entered avale barname:")



    #await message.answer("start", reply_markup=keyboard3)
    #if message.text >= 0:
        #print("hal shod")
    #else:
        #print("ridi")


    
    if message.text == 'از اکباتانا':
        #await message.reply("با ادمین تماس بگیرین", reply_markup=keyboard4)
        await message.answer("با ادمین تماس بگیرین:\n" + "شماره تماس:\n" + "+176123456", reply_markup=keyboard3)
        #print (message.answer)




    elif message.text ==  "ثبت آگهی":
        esmeid = (message.from_user.username)
        
        esm = (message.chat.first_name)
        famil = (message.chat.last_name)
        shenase = (message.chat.id)


        print ('{},{},{},{}'.format(esm,famil,shenase,esmeid), "<-----------------moshakhasaate Client")
        agahi = await message.answer("لطفا یک گزینه را انتخاب کنید", reply_markup=keyboard1)


    elif message.text ==  'خرید':

        a = await message.answer("مقدار یورو مورد نظر را به لاتین وارد کنید", reply_markup=keyboard2)


        #a = message.text
        #if a == int(a):
            #print(a.numerator)

        #meghdar2 = int(await message.answer("مقدار یورو مورد نظر را به لاتین وارد کنید 2", reply_markup=keyboard4))
        #meghdar1 = 0
        #meghdar2 = 0

            #print(number_1 + number_2)
        #print('{} + {} = '.format(meghdar1, meghdar2))
        #print (message.answer("meghdar1", meghdar1))

        #print(meghdar2+meghdar1)

 


    elif message.text ==  'فروش':
        a = await message.answer("مقدار یورو مورد نظر را به لاتین وارد کنید و دکمه ی تایید را بزنید", reply_markup=keyboard2)

        



    #elif message.text ==  'paypal':

        #await message.text (f"https://api.telegram.org/bot5448480357:AAHdBnqHbP-fY4WglCAf919pxKHCRE_Yf7A/sendMessage?chat_id=@{chat_id}&text=paym")
       # print (await message.answer(f"paypal sabt shod", reply_markup=keyboard4))
        #print (message.answer)
        #return ecbatana
    #elif message.text ==  'ok':
        #await message.answer("مقدار یورو مورد نظر را به لاتین وارد کنید", reply_markup=keyboard4)
    


    elif message.text ==  'تایید':

        #print (message.answer)
        #if a >= 0:
            payam = message.text
            b = await message.answer("لطفا ارزش پول خود را بنویسید و پس از ارسال, روی دکمه ی تایید درخواست کلیک کنید", reply_markup=keyboard4)



            #if ok1 

            #a = await message.answer(f"به چه ارزشی؟ ")

            print ("meghdare 1 taid shod************************")
            print ("darkhaste 1 hast:--------->", {message.text})




    elif message.text ==  'تایید درخواست':
        #print(me)
        #print (message.answer)
            #if b >= 0:
        #try:
        print("taiide darkhast")
        #except taiiderror: # esme error del be khahi
        print("Something went wrong", message.text)
        c = await message.answer("ممنون چک میشه", reply_markup=keyboard3)
        #else:
        print("Nothing went wrong", message.text)
        print ("meghdare 2 taid shod*************************")
        print()



        esmeid = (message.from_user.username)
        
        esm = (message.chat.first_name)
        famil = (message.chat.last_name)
        shenase = (message.chat.id)


        print ('{},{},{},{}'.format(esm,famil,shenase,esmeid), "moshakhasaate Client")



    elif message.text ==  'بازگشت':
        await message.answer("ممنون", reply_markup=keyboard3)
        #print (message.answer)
    



    #CLI
        print("-------------------LOG 1------------------------")

    print ("Client Entered akhare barname:---------->")
 

    print("-------------------LOG 2------------------------")    
    print(message.text)

    print ("message id:", message.message_id)


if __name__ == '__main__':

    print("******************STARTING**********************")


    print ('status')
executor.start_polling(dp, skip_updates=True)





#برای دریافت پیام ها
#https://api.telegram.org/bot<token>/sendMessage?chat_id=<group chat id >&text=<our text>


#ارسال پیام
#https://api.telegram.org/bot5448480357:AAHdBnqHbP-fY4WglCAf919pxKHCRE_Yf7A/sendMessage?chat_id=@ecbatanamoney&text=paym

