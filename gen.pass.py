import random 

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

number = int( input( 'Кол-во паролей: ' ) )
lenght = int( input( 'Длина строки: ' ) )

for x in range( number ):
	password = ''

	for i in range( lenght ):
		password += random.choice( chars )

	print( password )

	file = open( 'password.txt', 'a' )
	file.write( '\n' + password )
	file.close()

# Закрытие программы при нажатии клавиши для консоли	
import os
os.system( 'pause' )