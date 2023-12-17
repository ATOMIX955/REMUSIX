try:
	import shutil 
	import os
	from pytube import YouTube
	from pytube.cli import on_progress
	from os import mkdir
	import time
	
except:
	os.system("pip install shutil")
	os.system("pip install pytube")
	
	
def musica():
		if os.path.exists("/data/data/com.termux/files/home/storage/shared/audio pytube"):
			
			
			
			link = input("\033[0;37m[ \033[1;33mURL \033[0;37m]\033[1;37m: \033[1;32m")
			
			
			yt=YouTube(link,on_progress_callback=on_progress)
			
			print(f"""
 
        \033[0;34mINFORMACION DEL MUSICA 
   
 \033[1;33mNombre: \033[0;32m{yt.title} 
 
 \033[1;33mduracion: \033[0;32m{yt.length}
 
 \033[1;33mfecha de publicación: \033[0;32m{yt.publish_date}
 
 \033[1;33mel número de veces que se ha visto el vídeo:  \033[0;32m{yt.views}
 
 """)
			
			
			
			Audio = yt.streams.filter(only_audio=True).first()
			
			download = Audio.download("/data/data/com.termux/files/home/storage/shared/audio pytube")
			
			base, ext = os.path.splitext(download)
			
			os.rename(download, f"{base}.mp3")
			print("\nFin de la descarga\n")
			time.sleep(5)

			
		else:
			os.mkdir("/data/data/com.termux/files/home/storage/shared/audio pytube")
			
			
			link = input("\033[0;37m[ \033[1;33mURL \033[0;37m]\033[1;37m: \033[1;32m")
			
			
			yt=YouTube(link,on_progress_callback=on_progress)
			print(f"""
 
        \033[0;34mINFORMACION DEL MUSICA 
   
 \033[1;33mNombre: \033[0;32m{yt.title} 
 
 \033[1;33mduracion: \033[0;32m{yt.length}
 
 \033[1;33mfecha de publicación: \033[0;32m{yt.publish_date}
 
 \033[1;33mel número de veces que se ha visto el vídeo:  \033[0;32m{yt.views}
 
 """)
			
			
			Audio = yt.streams.filter(only_audio=True).first()
			
			download = Audio.download("/data/data/com.termux/files/home/storage/shared//audio pytube")
			
			base, ext = os.path.splitext(download)
			
			os.rename(download, f"{base}.mp3")
			print("\nFin de la descarga\n")
			time.sleep(5)


	

			
			
def salir():
	print("\n\033[1;33mCHAU CHAU\033[1;37m\n")
	exit(0)
	

def video():
		if os.path.exists("/data/data/com.termux/files/home/storage/shared/videos pytube"):
			
	
			link = input("\033[0;37m[ \033[1;33mURL \033[0;37m]\033[1;37m: \033[1;32m")
			
			yt=YouTube(link,on_progress_callback=on_progress)
			try:
				print(f"""
 
        \033[0;34mINFORMACION DEL VIDEO 
   
 \033[1;33mNombre: \033[0;32m{yt.title} 
 
 \033[1;33mduracion: \033[0;32m{yt.length}
 
 \033[1;33mfecha de publicación: \033[0;32m{yt.publish_date}
 
 \033[1;33mel número de veces que se ha visto el vídeo:  \033[0;32m{yt.views}
 
 """)
			
				yt = yt.streams.get_highest_resolution()
				yt.download("/data/data/com.termux/files/home/storage/shared/videos pytube")
				
				
			except:
				print("No se puede descargar el video )-:")
			print("\nFin de la descarga\n")
			time.sleep(5)
			
		else:
			os.mkdir("/data/data/com.termux/files/home/storage/shared/videos pytube")
			
			link = input("\033[0;37m[ \033[1;33mURL \033[0;37m]\033[1;37m: \033[1;32m")
			
			yt=YouTube(link,on_progress_callback=on_progress)
			try:
				print(f"""
 
        \033[0;34mINFORMACION DEL VIDEO 
   
 \033[1;33mNombre: \033[0;32m{yt.title} 
 
 \033[1;33mduracion: \033[0;32m{yt.length}
 
 \033[1;33mfecha de publicación: \033[0;32m{yt.publish_date}
 
 \033[1;33mel número de veces que se ha visto el vídeo:  \033[0;32m{yt.views}
 
 """)
			
				yt = yt.streams.get_highest_resolution()
				yt.download("/data/data/com.termux/files/home/storage/shared/videos pytube")
				
			except:
				print("No se puede descargar el video )-:")
			print("\nFin de la descarga\n")
			time.sleep(5)
		



	
	
	
def numeros(self):
		try:
			self.num = int(input("\033[1;34mElije >> \033[0;37m"))
		except:
			print("\n\033[1;33merro 87\033[1;37m")
			exit(0)
			
		
			
		
	