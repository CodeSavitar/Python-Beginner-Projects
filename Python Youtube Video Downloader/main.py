from pytube import YouTube

link = input("INSERT YOUR YOUTUBE LIN HERE: ")
url = YouTube(link)
print("DOWNLOADING......")
video = url.streams.first()
video.download()
print("DOWNLOADED!!")