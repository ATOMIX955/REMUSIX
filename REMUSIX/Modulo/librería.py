try:
	from Modulo.banners import Sin_conexión_a_internet
	from Modulo.banners import banner_uno
	from Modulo.banners import banner_dos
	from Modulo.banners import banner_tres
	from Modulo.descargar import video
	from Modulo.descargar import musica
	from Modulo.descargar import salir
	from Modulo.descargar import numeros
	import time , socket ,  platform , os
except:
	os.system("pip install shutil")
	os.system("pip install pytube")
	os.system("pip install platform")