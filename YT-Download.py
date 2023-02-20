from pytube import YouTube
import moviepy.editor as mp

# URL des YouTube-Videos angeben
video_url = 'https://youtu.be/PHW1RLjm1-w'

# YouTube-Video mit pytube herunterladen
yt = YouTube(video_url)
stream = yt.streams.filter(only_audio=True).first()
stream.download()

# Konvertieren Sie das Video in eine MP3-Datei
video_path = stream.default_filename
mp3_path = video_path.replace(".mp4", ".mp3")
clip = mp.AudioFileClip(video_path).write_audiofile(mp3_path)

# Optional: löschen Sie das ursprüngliche Video
import os
os.remove(video_path)

print('Das Video wurde als MP3 heruntergeladen und unter', mp3_path, 'gespeichert. Script geschrieben von Rene B.')
