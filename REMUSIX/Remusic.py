
from Modulo.librería import *


class Remusix:
	def __init__(self):
		banner_uno()
		
	def elije(self):
		numeros(self)
		
		
	def Menu(self):
						if self.num == 1:
							banner_dos()
							video()
							
						elif self.num == 2:
							banner_tres()
							musica()
						elif self.num == 3:
							salir()
						else:
							print("\nVolve a intentarlo\n")
							time.sleep(1)
				
		
			
			
		
	
		
if __name__ == "__main__":
	intento = 0
	while intento <= 5:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(1)
		vercion = platform.architecture()
		sistema = platform.system()
		try:
			s.connect(("www.google.com", 80))
		except (socket.gaierror, socket.timeout):
			Sin_conexión_a_internet()
			break
		else:
		  if platform.system() == "Linux" and vercion[0] == "32bit":
		  	Mi = Remusix()
		  	Mi.elije()
		  	Mi.Menu()
		  	s.close()	
		  else:
		  		print(f"""\033[1;30m
				
			[ \033[1;31mNO SOS {sistema} {vercion}\033[1;30m] 
				
				""")
				
		  		break
		  		