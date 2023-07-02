import requests,re
from telegram import InputMediaPhoto
try:
	 import telebot
except:
	 import os
	 os.system("pip install pyTelegramBotAPI")
from telebot import *
from gate import Tele 
from gate import Tel
from gate import star
from colorama import Fore
from telebot import types
token = "6205240657:AAEQJw40RKu7noLkNX52DsinpAnsUXYfOMo" #توكنك
id =5389729648  #ايديك
bot=telebot.TeleBot(token,parse_mode="HTML")

@bot.message_handler(commands=["start"])
def start(message):
	user_first_name = message.from_user.first_name
	    
	english_texts = {
		'start': f'''
	Welcome {user_first_name} To The Best Bot That Provides Spam Services 
	Portals Are Now Available 👇 
	/chk ➜ stripe 
	/cc ➜ braintree
	/gen Then put your bin ➜ to generate cards
	/scr Then put the link and the number''',
	}
	
	arabic_texts = {
		'start': f'''مرحبًا {user_first_name} بك في أفضل روبوت يوفر  خدمات الspammer  الاوامر المتاحة الآن  /chk ➜ stripe /cc ➜ braintree /gen Bin here  ➜ لإنشاء بطاقات /scr ثم ضع رابط الجروب او القناه وعدد البطاقات'''
	}
	user_id = message.from_user.id
	numbers = re.findall(r'\d+', message.text)
	for number in numbers:
		if len(number) == 10:
			with open("all id.txt", "r+") as file:
				lines = file.readlines()
				file.seek(0)
				for line in lines:
					if number in line.strip():
						parts = line.strip().split('|')
						num = int(parts[1])
						num += 10
						new_line = f"{parts[0]}|{num}\n"
						print(new_line)
						file.write(new_line)
					else:
						file.write(line)
				file.truncate()

		

		else:
			print("لا توجد 10 أرقام في الرسالة.")
	print(message.text)
	user_id = message.from_user.id
	found = 'yy'
	with open("id.txt", "r") as file:
		for line in file:
			if str(user_id) in line.strip():
				if "ar" in line.strip():
					found='ar'
				else:
					found='en'
	if "ar" in found:
		photo_url = 'https://t.me/gutxw/2'
		caption = arabic_texts['start']
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=caption)
	elif "en" in found:
		photo_url = 'https://t.me/gutxw/2'
		caption = english_texts['start']
		bot.send_photo(chat_id=message.chat.id, photo=photo_url, caption=caption)
	else:
			markup = types.InlineKeyboardMarkup(row_width=2)
			lucifer1 = types.InlineKeyboardButton("Arab 🇸🇦", callback_data='u8')
			lucifer2 = types.InlineKeyboardButton("English 🇺🇸", callback_data='u2')
			markup.add(lucifer1, lucifer2)
			
			# إرسال رسالة الرد مع اللوحة
			
			bot.send_message(chat_id=message.chat.id, text="ما هي لغتك\n What is your language ", reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
	user_first_name = call.from_user.first_name
	    
	english_texts = {
		'start': f'''
	Welcome {user_first_name} To The Best Bot That Provides Spam Services 
	Portals Are Now Available 👇 
	/chk ➜ stripe 
	/cc ➜ braintree
	/gen Then put your bin ➜ to generate cards
	/scr Then put the link and the number''',
	}
	
	arabic_texts = {
		'start': f'''مرحبًا {user_first_name} بك في أفضل روبوت يوفر  خدمات الspammer  الاوامر المتاحة الآن  /chk ➜ stripe /cc ➜ braintree /gen Bin here  ➜ لإنشاء بطاقات /scr ثم ضع رابط الجروب او القناه وعدد البطاقات'''
	}
	if call.data == 'u8':
		photo_url = 'https://t.me/gutxw/2'
		caption = arabic_texts['start']
		bot.send_photo(chat_id=call.from_user.id, photo=photo_url, caption=caption)
		with open('id.txt', 'a+') as f:
			f.writelines(str(call.from_user.id)+'|'+'ar\n')
		
	else:
		photo_url = 'https://t.me/gutxw/2'
		caption = english_texts['start']
		bot.send_photo(chat_id=call.from_user.id, photo=photo_url, caption=caption)
		with open('id.txt', 'a+') as f:
			f.writelines(str(call.from_user.id)+'|'+'en\n')
@bot.message_handler(content_types=["document"])
def main(message):
	bad = 0
	nok = 0
	ok = 0
	ko = (bot.reply_to(message, "Please Wait...⏳").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	
	if message.chat.id == id:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('unknown ⚠️')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('unknown ⚠️')
				try:
					cn=(data['country']['name'])
				except:
					cn=('unknown ⚠️')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('unknown ⚠️')
				try:
					typ=(data['type'])
				except:
					typ=('unknown ⚠️')
				try:
					url=(data['bank']['url'])
				except:
					url=('unknown ⚠️')
				else:
					break
				mes = types.InlineKeyboardMarkup(row_width=1)
				lucifer1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				lucifer2 = types.InlineKeyboardButton(f"• CHARGED ✅: [ {ok} ] •", callback_data='u2')
				lucifer3 = types.InlineKeyboardButton(f"• Live ✅ : [ {nok} ] •", callback_data='u2')
				lucifer4 = types.InlineKeyboardButton(f"• DEAD ❌ : [ {bad} ] •", callback_data='u1')
				lucifer5 = types.InlineKeyboardButton(f"• TOTAL 👻 : [ {total} ] •", callback_data='u1')
				mes.add(lucifer1, lucifer2, lucifer3, lucifer4, lucifer5)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @THE_S9 ''', reply_markup=mes)
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					try:
						last = str(Tele(cc))
					except Exception as e:
						print(e)
						bot.reply_to(message, f"حدث خطأ أثناء فحص هذه البطاقة وتم تخطيها \nAn error occurred while checking this card and it has been skipped \n {cc}")
						last = "Your card was declined."
					print(last)
					msg1 = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
				◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
				◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑺𝑈𝑪𝑪𝐸𝑆𝑆
				◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 1$ 
				━━━━━━━━━━━━━━━━━
				◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
				◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
				◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
				◆ 𝑼𝑹𝑳 ➜ {url}
				━━━━━━━━━━━━━━━━━
				◆ 𝑩𝒀: @THE_S9
				◆ 𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				
				msg = f'''◆ 𝑪𝑨𝑹𝑫  ➜ {cc} 
				◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫!  ✅ 
				◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {last}
				◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 1$ 
				━━━━━━━━━━━━━━━━━
				◆ 𝑩𝑰𝑵 ➜ {cc[:6]} - {dicr} - {typ} 
				◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
				◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
				◆ 𝑼𝑹𝑳 ➜ {url}
				━━━━━━━━━━━━━━━━━
				◆ 𝑩𝒀: @THE_S9
				◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
				
				if "Your card's security code is" in last:
					bot.reply_to(message, msg)
					nok += 1
				elif "Your card has insufficient funds." in last:
					nok += 1
					bot.reply_to(message, msg)
				elif "Your card does not support this type of purchase." in last:
					nok += 1
					bot.reply_to(message, msg)
				elif "Your card's expiration month is invalid." in last:
					nok += 1
					bot.reply_to(message, msg)
				elif "ssss" in last:
					ok += 1
					bot.reply_to(message, msg1)
				else:
					bad += 1
				
@bot.message_handler(commands=["chk"])
def start(message):
	cc = message.text.replace('/chk ', '')
	ko = (bot.reply_to(message,"please wait...⏳").message_id)
	try:
		last = str(Tel(cc))
		bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=last)
	except Exception as e:
		bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text='''Invalid format, type it CORRECTLY!
Format: XXXXXXXXXXXXXXXX|MM|YYYY|CVV''')
		
		try:
			last = str(Tel(cc))
			bot.edit_message_text(chat_id=message.chat.id,message_id=ko,text=last)
		except Exception as e:
			print(e)
@bot.message_handler(commands=["premium"])
def start(message):
	user_id = message.from_user.id
	found = 'yy'
	with open("id.txt", "r") as file:
		for line in file:
			if str(user_id) in line.strip():
				if "ar" in line.strip():
					found='ar'
				else:
					found='en'
	if "ar" in found:
		invite_link = bot.export_chat_invite_link('@JPXZE')
		bot.reply_to(message,f"""يمكنك الان تفعيل البوت بروميوم مجانا كل ما ستحتاجة هو دعوه 40 مستخدم الي البوت عبر رابط الدعوة الخاص بك ها هو الرابط الخاص بك 

 https://t.me/BDKTBOT?start={user_id}
""")
	elif "en" in found:
		bot.reply_to(message,f'''You can now activate all the features of the bot for free. All you need is to invite 40 users to the bot via your invitation link. Here is your link

https://t.me/BDKTBOT?start={user_id}''')
	else:
			markup = types.InlineKeyboardMarkup(row_width=2)
			lucifer1 = types.InlineKeyboardButton("Arab 🇸🇦", callback_data='u8')
			lucifer2 = types.InlineKeyboardButton("English 🇺🇸", callback_data='u2')
			markup.add(lucifer1, lucifer2)
			bot.send_message(chat_id=message.chat.id, text="ما هي لغتك\n What is your language ", reply_markup=markup)
print("STARTED")
bot.polling()
