import os
from pytube import YouTube
from moviepy.editor import VideoFileClip

def convert_to_mp3(filename):
	clip = VideoFileClip(filename)
	clip.audio.write_audiofile(filename[:-4] + ".mp3")
	clip.close()

def download(link, video):
	yt = YouTube(link.strip())

	print("\nTitle: "+yt.title)
	print("Thumbanil: "+yt.thumbnail_url)

	# stream = yt.streams.filter().get_by_itag(22)
	stream = yt.streams.get_highest_resolution()
	stream.download('downloads/') # Download video

	if video != 'n':
		convert_to_mp3('downloads/'+stream.default_filename)
		os.remove('downloads/'+stream.default_filename)

def main():
	link = input("Enter the link: ")
	video = input("Download as audio? (Y/n): ").lower()

	download(link, video)
	print("Finished!")


if __name__ == '__main__':
	main()

"""
QUALITY           | ITAG
Low (360p)        - 18
Medium (720p)     - 22
High (1080p)      - 137
Very High (2160p) - 313

140 = Audio only (bad quality)
"""
