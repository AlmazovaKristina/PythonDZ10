
from bot_config import dp, bot
from aiogram import types
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
message2 = 0
message3 = 0
message4 = 0


@dp.message_handler(commands=['start'])
async def url_command(message: types.Message):

   markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
   btn1 = types.KeyboardButton('Хочу выбрать вещи')
   markup.add(btn1)
   await message.answer('Привет', reply_markup=markup)
   keyboard = InlineKeyboardMarkup()
   button = InlineKeyboardButton('Хочу посомтреть видео про моду', url='https://www.youtube.com/results?search_query=модные+вещи+2023')
   keyboard.add(button)
   await message.answer('Вы попали в мир моды! Выберите ниже, что вы хотите посмотреть.', reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def txt(message: types.Message):
   global message2
   global message3
   global message4
   global message5
   if (message.text == 'Хочу выбрать вещи'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn3 = types.KeyboardButton('Ж 👩‍🦰')
      btn4 = types.KeyboardButton('М 👨')
      markup.add(btn3, btn4)
      await bot.send_message(message.chat.id, text='Выберите пол:', reply_markup=markup)
   if (message.text == 'Ж 👩‍🦰'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      message2 = message.text
      message5 = message.text
      print(message2)
      print(message5)
      btn5 = types.KeyboardButton('Штаны 👖')
      btn6 = types.KeyboardButton('Кофта 👚')
      btn7 = types.KeyboardButton('Платье 👗')
      btn8 = types.KeyboardButton('Пальто 🧥')
      markup.add(btn5, btn6, btn7, btn8)
      await bot.send_message(message.chat.id, text='Выберите тип одежды:', reply_markup=markup)
   if (message.text == 'М 👨'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      message2 = message.text
      message5 = message.text
      print(message2)
      print(message5)
      btn9 = types.KeyboardButton('Штаны 👖')
      btn10 = types.KeyboardButton('Кофта 👕')
      btn11 = types.KeyboardButton('Рубашка 👔')
      btn12 = types.KeyboardButton('Пальто 🧥')
      markup.add(btn9,btn10,btn11, btn12)
      await bot.send_message(message.chat.id, text='Выберите тип одежды:', reply_markup=markup)
   if (message.text == 'Штаны 👖'):
      if message2 == 'Ж 👩‍🦰':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         message3 = message.text
         message5 = message.text
         print(message3)
         print(message5)
         btn13 = types.KeyboardButton('🔴')
         btn14 = types.KeyboardButton('🟠')
         btn19 = types.KeyboardButton('⚫️')
         markup.add(btn13, btn14,btn19)
      else:
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         message3 = message.text
         print(message3)
         btn13 = types.KeyboardButton('🔴')
         btn15 = types.KeyboardButton('⚫️')
         markup.add(btn13,btn15)
      await bot.send_message(message.chat.id, text='Выберите цвет:', reply_markup=markup)
   if (message.text == 'Кофта 👚'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      message3 = message.text
      message5 = message.text
      print(message3)
      btn22 = types.KeyboardButton('🔴')
      btn23 = types.KeyboardButton('🟠')
      btn28 = types.KeyboardButton('⚫️')
      markup.add(btn22, btn23,btn28)
      await bot.send_message(message.chat.id, text='Выберите цвет:', reply_markup=markup)
   if (message.text == 'Платье 👗'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      message3 = message.text
      print(message3)
      btn13 = types.KeyboardButton('🔴')
      btn14 = types.KeyboardButton('🟠')
      btn19 = types.KeyboardButton('⚫️')
      markup.add(btn13, btn14,btn19)
      await bot.send_message(message.chat.id, text='Выберите цвет:', reply_markup=markup)
   if (message.text == 'Пальто 🧥'):
      if message2 == 'Ж 👩‍🦰':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         message3 = message.text
         message5 = message.text
         print(message3)
         print(message5)
         btn13 = types.KeyboardButton('🔴')
         btn14 = types.KeyboardButton('🟠')
         btn19 = types.KeyboardButton('⚫️')
         markup.add(btn13, btn14, btn19)
      else:
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         message3 = message.text
         print(message3)
         btn13 = types.KeyboardButton('🔴')
         btn15 = types.KeyboardButton('⚫️')
         markup.add(btn13, btn15)
      await bot.send_message(message.chat.id, text='Выберите цвет:', reply_markup=markup)
   if (message.text == 'Кофта 👕'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      message3 = message.text
      print(message3)
      btn13 = types.KeyboardButton('🔴')
      btn15 = types.KeyboardButton('⚫️')
      markup.add(btn13, btn15)
      await bot.send_message(message.chat.id, text='Выберите цвет:', reply_markup=markup)
   if (message.text == 'Рубашка 👔'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      message3 = message.text
      print(message3)
      btn13 = types.KeyboardButton('🔴')
      btn15 = types.KeyboardButton('⚫️')
      markup.add(btn13, btn15)
      await bot.send_message(message.chat.id, text='Выберите цвет:', reply_markup=markup)
   if (message.text == '🔴'):
      if message2 == 'Ж 👩‍🦰' and message3 == 'Штаны 👖':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         message4 = message.text
         print(message4)
         await bot.send_message(message.chat.id,"[1](https://flakonn.com/wp-content/uploads/2017/07/krasnye-bryuki-zhenskie_-1.jpeg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://ae04.alicdn.com/kf/H987b628bcb614e87b24564cde108a324W/Dressmecb.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://ae04.alicdn.com/kf/S14225cc5b7304326b5d297f44f8a8a9dZ.jpg_350x350.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://www.lookbuck.com/system/products/items/images/019/561/547/small/image1xxl.jpg?1561579053)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message2 == 'М 👨' and message3 == 'Штаны 👖':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://smartcasuals.ru/wp-content/uploads/2021/07/2021-07-26-11-21-22-51.jpeg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://ae04.alicdn.com/kf/H51c07f2acc6c4966a2220b5ac98e4d86e/-.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://shopsycdn.com/i/p/69/0b/690bcb853a94afcb0dc72c2a6c5891b5_medium.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://maned.ru/upload/resize_cache/iblock/e5d/800_1200_173980c64749f168015761cd752caacb5/e5d89f456c6ee7c029c6790f0c314fca.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Кофта 👚':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://ae04.alicdn.com/kf/S2171834b1e7b4fe3abf727201fbc8a6fT.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://zapatos.ru/_sh/482/48259s_1.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://basket-04.wb.ru/vol446/part44690/44690383/images/big/2.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://cdn1.ozone.ru/s3/multimedia-3/c300/6155965719.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Платье 👗':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id, "[1](https://static2.issaplus.com/wa-data/public/shop/products/25/00/70025/images/160692/160692.600x900.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id, "[2](https://imgcdn.loverepublic.ru/upload/images/23593/thumb/375_9999/2359363515_70.jpg)", parse_mode='markdown')
         await bot.send_message(message.chat.id, "[3](https://cdnvitrina.ru/uploads/images/40/1959945127.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id, "[4](https://a.lmcdn.ru/img236x341/M/P/MP002XW0867X_14846111_1_v1_2x.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message2 == 'Ж 👩‍🦰' and message3 == 'Пальто 🧥':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://ekaterinasmolina.ru/media/list/krasnoe-na-krasnom.jpg.452x678_q85.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://i.pinimg.com/736x/77/b7/22/77b7227053a31ed055aff151d8b43c18.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://cdn.lookastic.ru/красное-пальто/warehouse-original-175074.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://trendy-lady.su/ext_images/763/img_3948e95746ac9ab7a201a13f96742a90)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message2 == 'М 👨' and message3 == 'Пальто 🧥':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://www.lookbuck.com/system/products/items/images/012/687/606/small/image1xxl.jpg?1508524027)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://www.mansfashion.ru/wp-content/uploads/2017/11/muzhskoe-krasnoe-palto.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://www.snik.co/system/products/items/images/033/562/204/small/palto-el-caballo-sevilla-1892?1644745518)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://smartcasuals.ru/wp-content/uploads/2020/10/hom5.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Кофта 👕':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://mrprintik.ru/wp-content/uploads/2018/10/muzhskaya-krasnaya-tolstovka.png)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://gd1.alicdn.com/imgextra/i1/902513423/TB2p4lggOMnBKNjSZFzXXc_qVXa_!!902513423.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://mayki.moscow/wp-content/uploads/2017/10/2-8-500x500.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://cdn.shopotam.com/huge/82/7d/827d3903992c8be0a40aafb5606eea12082a283c.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Рубашка 👔':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://www.aaa-gifts.ru/upload/iblock/335/3350ec253fed51172114d656d12ba3cb.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://themensclub.ru/components/com_virtuemart/shop_image/product/MS1201_13.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://www-s.mlo.me/upen/v/2017/201704/20170426/201704261452300257655.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://fashionapp.ru/wp-content/uploads/2016/04/modnye-muzhskie-rubashki-2016-9-803x1024.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
   if (message.text == '🟠'):
      if message3 == 'Штаны 👖':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         message4 = message.text
         message5 = message.text
         print(message4)
         print(message5)
         await bot.send_message(message.chat.id,"[1](https://a.lmcdn.ru/img236x341/M/P/MP002XW0CTXK_17026231_1_v1_2x.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://www.freak-butik.ru/products/23921.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://static.staff-clothes.com/uploads/media/image_product/0002/14/5b5b14f8ec054f6d827bdd396333b60c.jpeg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://ae04.alicdn.com/kf/He046703aaaed4692842639d0ba1214cdG/-.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Кофта 👚':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://cdn.yepme.ru/images/thumb/42071/kofta/17260705.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://www.vitoricci.ru/images/thumbs/132507540289725210.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://cdn1.ozone.ru/s3/multimedia-p/c300/6490023349.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://img2.cachan.ru/images/312x400x0x0x24x24/4/2c8d113565919409a551de0d0827d4c3.jpg?s=12)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Платье 👗':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id, "[1](https://a.lmcdn.ru/img236x341/M/P/MP002XW0BOY3_17110953_1_v1_2x.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id, "[2](https://ae04.alicdn.com/kf/Sa50c9c3b90bf4cdb951667d2b5172eb2U.jpg)", parse_mode='markdown')
         await bot.send_message(message.chat.id, "[3](https://ae04.alicdn.com/kf/Hf4b7b83ea40f46c1b4b5586c53bca0d7q/-.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id, "[4](https://a.lmcdn.ru/pi/img600x866/R/T/RTLABJ997701_16972582_1_v1.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Пальто 🧥':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://main-cdn.sbermegamarket.ru/big1/hlr-system/15099341127/100025747811b0.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://main-cdn.sbermegamarket.ru/big1/hlr-system/-4/46/91/68/05/11/10/100027563308b0.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://cdn1.ozone.ru/s3/multimedia-4/c300/6364783216.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://ae04.alicdn.com/kf/S9b55479de0b147d19e33382f7366fc03k/LANMREM.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
   if (message.text == '⚫️'):
      message4 = message.text
      print(message4)
      if message2 == 'Ж 👩‍🦰' and message3 == 'Штаны 👖':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://imgcdn.befree.ru/rest/V1/images/1024/product/images/1831291766/1831291766_50_2.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://ae01.alicdn.com/kf/H8fdcf822e9ed4c03b8f72a1f4563d545e.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](hhttps://img.joomcdn.net/842fdb51123f1ba5d9891af4e4f22d10f5233e58_original.jpeg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://ae04.alicdn.com/kf/S4f685546b6174171ba5d9682302059fds.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message2 == 'М 👨' and message3 == 'Штаны 👖':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://img.five-sport.ru/images/products/1/2234/304703674/1906492_999000_Craft_Glide_XC_лыжные_брюки_мужские_черные__1_.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://img.joomcdn.net/30d91929107c25b810e16db6cff85bdc66993273_original.jpeg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://ae04.alicdn.com/kf/HTB1s_lnQXXXXXb7XXXXq6xXFXXXG/-.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://ae04.alicdn.com/kf/H6a68e44f68ce44488c13e7b10317dd3az/-.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Кофта 👚':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://ae04.alicdn.com/kf/S00322579dc6e4c84aba3502f4784daf3x.jpg_350x350.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://spkubani.club/files/ca6/ca6da6b52a590d6ab7fcef56307f4140.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://basket-08.wb.ru/vol1124/part112448/112448073/images/c516x688/1.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://uhd.name/uploads/posts/2022-08/1660387411_1-uhd-name-p-kofta-chernaya-zhenskaya-devushka-krasivo-3.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Платье 👗':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id, "[1](https://ae04.alicdn.com/kf/Sb0cf51406a3140ebac2c859e82f7381be/-.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id, "[2](https://sc04.alicdn.com/kf/H00c83dc27be2429fb4cf3da88455a57eS.jpg)", parse_mode='markdown')
         await bot.send_message(message.chat.id, "[3](https://ae04.alicdn.com/kf/Sbc3f3253dc8447de991e0977e87a10c8Z.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id, "[4](https://ir.ozone.ru/s3/multimedia-j/c1000/6498453139.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message2 == 'Ж 👩‍🦰' and message3 == 'Пальто 🧥':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](hhttps://ae04.alicdn.com/kf/S482a111cf57f4604b7f7b771c17c6537E/-.jpg_640x640.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://paolomoretti.ru/images/2021/cashmere_donna/куртка-с-мехом-женская-зимняя.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://ekaterinasmolina.ru/media/list/dlinnoe-palto.jpg.452x678_q85.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://www.dhresource.com/0x0/f2/albu/g10/M01/9F/A1/rBVaVl1jqc6AN8x0AAO_ae8Re4g940.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message2 == 'М 👨' and message3 == 'Пальто 🧥':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://smartcasuals.ru/wp-content/uploads/2020/11/DSC_4633.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://fashionapp.ru/wp-content/uploads/2016/09/chernoe-muzhskoe-palto-20.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://ae04.alicdn.com/kf/Hfec36bb0aeec405b93ad7268e11d3870p/2020.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://www.lookbuck.com/system/products/items/images/041/220/238/small/24035672-1-black?1630411557)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Кофта 👕':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://ae04.alicdn.com/kf/S75193a331107455788933b31234dddafw/-.jpg_640x640.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://ae04.alicdn.com/kf/H2952bb4b8b13499cb7483bf13d4ee21ce/-.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://ae01.alicdn.com/kf/Sdd3ed5c950f541529e331268ffc1794dN.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://ae04.alicdn.com/kf/Ha197d660bf0e49a2af3303737ad31932x.jpg_350x350.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
      elif message3 == 'Рубашка 👔':
         markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
         await bot.send_message(message.chat.id,"[1](https://henderson.ru/uimages/catalog/product/SHL-1469-N/SHL-1469-N-BLACK-6-7.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[2](https://ae04.alicdn.com/kf/Se4dea251111d436fad63c9f50c505a74G.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[3](https://ae04.alicdn.com/kf/HTB1FcbAlL1TBuNjy0Fjq6yjyXXa2/2018.jpg)",parse_mode='markdown')
         await bot.send_message(message.chat.id,"[4](https://ae04.alicdn.com/kf/S910a51fb08944f019c5e8dae9bdcc67aQ.jpg)",parse_mode='markdown')
         btn13 = types.KeyboardButton('1 вариант')
         btn14 = types.KeyboardButton('2 вариант')
         btn15 = types.KeyboardButton('3 вариант')
         btn16 = types.KeyboardButton('4 вариант')
         markup.add(btn13, btn14, btn15, btn16)
         await bot.send_message(message.chat.id, text='Выберите какой вариант вам нравится:', reply_markup=markup)
   if (message.text == '1 вариант' or message.text == '2 вариант' or message.text == '3 вариант' or message.text == '4 вариант'):
      markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
      btn13 = types.KeyboardButton('Да')
      btn14 = types.KeyboardButton('Нет')
      markup.add(btn13, btn14)
      await bot.send_message(message.chat.id, text='Вы дейстивтельно хотите заказать товар: ', reply_markup=markup)
   if (message.text == 'Да'):
      await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, заказ оформлен')
   elif (message.text == 'Нет'):
      await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, очень жаль, приходите к нам ещё')


















