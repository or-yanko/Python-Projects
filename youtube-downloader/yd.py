import pytube
from colorama import init, Fore

def on_complete(stream, filepath):
	print('download complete')
	print(filepath)

def on_progress(stream, chunk, bytes_remaining):
	progress_string = f'{round(100 - (bytes_remaining / stream.filesize * 100),2)}%'
	print(progress_string)
# download
print(
	Fore.RED + 'download:' + 
	Fore.GREEN + '(b)est \033[39m|' + 
	Fore.YELLOW + '(w)orst \033[39m|' + 
	Fore.BLUE + '(a)udio \033[39m| '+
	Fore.CYAN + '(l)ist of audio\'s \033[39m| (e)xit')
download_choice = input('choice: ')

init()


if download_choice == 'b':
	link = input('Youtube link: ')
	video_object = pytube.YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

	# information
	print(Fore.RED + f'title:  \033[39m {video_object.title}')
	print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
	print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
	print(Fore.RED + f'author: \033[39m {video_object.author}')

	video_object.streams.get_highest_resolution().download('./Downloads')
elif download_choice == 'w':
	link = input('Youtube link: ')
	video_object = pytube.YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

	# information
	print(Fore.RED + f'title:  \033[39m {video_object.title}')
	print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
	print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
	print(Fore.RED + f'author: \033[39m {video_object.author}')

	video_object.streams.get_lowest_resolution().download('./Downloads')
elif download_choice == 'a':
	link = input('Youtube link: ')
	video_object = pytube.YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

	# information
	print(Fore.RED + f'title:  \033[39m {video_object.title}')
	print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
	print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
	print(Fore.RED + f'author: \033[39m {video_object.author}')

	video_object.streams.get_audio_only().download('./Downloads',str(video_object.title+'.mp3'))
elif download_choice == 'l':
	print('enter q when you wanna stop.')
	link = input('Youtube link: ')
	while link !='q':
		video_object = pytube.YouTube(link, on_complete_callback = on_complete, on_progress_callback = on_progress)

		# information
		print(Fore.RED + f'title:  \033[39m {video_object.title}')
		print(Fore.RED + f'length: \033[39m {round(video_object.length / 60,2)} minutes')
		print(Fore.RED + f'views:  \033[39m {video_object.views / 1000000} million')
		print(Fore.RED + f'author: \033[39m {video_object.author}')

		video_object.streams.get_audio_only().download('./Downloads',str(video_object.title+'.mp3'))
		link = input('Youtube link: ')

print('\nbye bye thank you for downloading it with me ;-)')


