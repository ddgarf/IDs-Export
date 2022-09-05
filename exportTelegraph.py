import requests
import re
from bs4 import BeautifulSoup 

def exportTelegraph():
	try:
		string = ""

		page1 = requests.get('https://telegra.ph/Acestream-08-22') 
		soup1 = BeautifulSoup(page1.text, 'html.parser')

		j = 0
		for content in soup1.find_all(['p', 'h3', 'h4', 'a']):

			if content.text == "": 
				pass
			else:
				if len(content.text.strip()) > 40:
					if ":" in content.text:
						ids = content.text.split(":")[1].strip()
						if len(ids) == 40:
							title = content.text.split(":")[0].strip()
							string+=str((title + "\n" + ids + "\n"))
					else:
						pass
				elif len(content.text.strip()) < 40:
					title = content.text
					title = title.replace(':', '')
					#string+=str((title + "\n"))
					j = 1
				elif len(content.text.strip()) == 40 and j == 1:
					ids = content.text
					string+=str((title+ "\n" + ids + "\n"))
					j = 0
				else:
					pass


		page2 = requests.get('https://telegra.ph/Ids-manuk0s-08-22') 
		soup2 = BeautifulSoup(page2.text, 'html.parser')

		j = 0
		for content in soup2.find_all(['p', 'h3', 'h4', 'a']):

			if content.text == "": 
				pass
			else:
				if len(content.text.strip()) > 40:
					if ":" in content.text:
						ids = content.text.split(":")[1].strip()
						if len(ids) == 40:
							title = content.text.split(":")[0].strip()
							string+=str((title + "\n" + ids + "\n"))
					else:
						pass
				elif len(content.text.strip()) < 40:
					title = content.text
					title = title.replace(':', '')
					#string+=str((title + "\n"))
					j = 1
				elif len(content.text.strip()) == 40 and j == 1:
					ids = content.text
					string+=str((title+ "\n" + ids + "\n"))
					j = 0
				else:
					pass

		page3 = requests.get('https://telegra.ph/El-diario-08-17') 
		soup3 = BeautifulSoup(page3.text, 'html.parser')

		j = 0
		for content in soup3.find_all(['p', 'h3', 'h4', 'a']):

			if '`' in content.text:	
				context_new = content.text.replace('`', '')
			else:
				context_new = content.text
			#print(context_new)

			if context_new == "": 
				pass
			else:
				if len(context_new.strip()) > 40:
					if ":" in context_new:
						ids = context_new.split(":")[1].strip()
						if len(ids) == 40:
							title = context_new.split(":")[0].strip()
							string+=str((title + "\n" + ids + "\n"))
					else:
						pass
				elif len(context_new.strip()) < 40:
					title = context_new
					title = title.replace(':', '')
					#string+=str((title + "\n"))
					j = 1
				elif len(context_new.strip()) == 40 and j == 1:
					ids = context_new
					string+=str((title+ "\n" + ids + "\n"))
					j = 0
				else:
					pass

		page4 = requests.get('https://telegra.ph/Coletilla-08-21-2') 
		soup4 = BeautifulSoup(page4.text, 'html.parser')

		j = 0
		for content in soup4.find_all(['p', 'h3', 'h4', 'a']):

			if content.text == "": 
				pass
			else:
				if len(content.text.strip()) > 40:
					if ":" in content.text:
						ids = content.text.split(":")[1].strip()
						if len(ids) == 40:
							title = content.text.split(":")[0].strip()
							string+=str((title + "\n" + ids + "\n"))
					else:
						pass
				elif len(content.text.strip()) < 40:
					title = content.text
					title = title.replace(':', '')
					#string+=str((title + "\n"))
					j = 1
				elif len(content.text.strip()) == 40 and j == 1:
					ids = content.text
					string+=str((title+ "\n" + ids + "\n"))
					j = 0
				else:
					pass
		contenido = ((string.replace(u'\xa0', u' ')).strip())

	except Exception as e:
            print("export_messages : ERROR :", e)
	print("export_messages : INFO : messages retrieved from Telegraph")

	return contenido