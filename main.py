import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def convert_to_mp3(filename):
	clip = VideoFileClip(filename)
	clip.audio.write_audiofile(filename[:-4] + ".mp3")
	clip.close()

def main():
	link = input("Enter the link: ")
	yt = YouTube(link.strip())
	# yt = YouTube("https://www.youtube.com/watch?v=Ba463jCxmow")


	print("\nTitle: "+yt.title)
	print("Thumbanil: "+yt.thumbnail_url)

	stream = yt.streams.filter().get_by_itag(22)
	stream.download('downloads/')
	convert_to_mp3('downloads/'+stream.default_filename)
	os.remove('downloads/'+stream.default_filename)

if __name__ == '__main__':
	main()

# Quality | itag
# Low (360p) = 18
# Medium = (720p) 22
# High (1080p) = 137
# Very High (2160p) = 313

# 140 = Audio only