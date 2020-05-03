import os
import sys
import pyAesCrypt
from getpass import getpass
from colorama import Fore

passw = ''
choose = ''

def clear ():
	if os.name == 'nt':
		os.system ('cls')
	else:
		os.system ('clear')

def crypt (file):
	bufferSize = 512 * 1024
	if choose == '1':
		try:
			pyAesCrypt.encryptFile (file, file + '.aes', passw, bufferSize)
			print (Fore.GREEN + file + ' Зашифрован!')
			os.remove (file)
		except:
			print (Fore.RED + file + ' Не Расшифрован :(')

	elif choose == '2':
		if '.aes' in file:
			try:
				pyAesCrypt.decryptFile (file, file.replace ('.aes', ''), passw, bufferSize)
				print (Fore.GREEN + file + ' Расшифрован!')
				os.remove (file)
			except:
				print (Fore.RED + file + ' Не Расшифрован :(')
		else:
			return

def get_all_files (folder):
	for name in os.listdir (folder):
		truePath = os.path.join (folder, name)
		if os.path.isdir(truePath) == True:
			get_all_files (truePath) 
		else:
			crypt (truePath)

def main ():
	global passw, choose
	print ('''
Разраб: @nkitas
Наш телеграмчик: @Termuxtop
 ▄▄· ▄▄▄   ▄· ▄▌ ▄▄▄·▄▄▄▄▄▄▄▄ .▄▄▄  
▐█ ▌▪▀▄ █·▐█▪██▌▐█ ▄█•██  ▀▄.▀·▀▄ █·
██ ▄▄▐▀▀▄ ▐█▌▐█▪ ██▀· ▐█.▪▐▀▀▪▄▐▀▀▄ 
▐███▌▐█•█▌ ▐█▀·.▐█▪·• ▐█▌·▐█▄▄▌▐█•█▌
·▀▀▀ .▀  ▀  ▀ • .▀    ▀▀▀  ▀▀▀ .▀  ▀
[1] -> Зашифровать
[2] -> Расшифровать
	''')

	choose = input ('Выберите назначение: ')
	folder = input ('Выберите папку (абсолютный путь): ')
	passw = getpass ('Выберите пароль: ')
	get_all_files(folder)

if __name__ == '__main__':
	clear ()
	main ()
