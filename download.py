#!/usr/bin/env python3
import csv
import music_tag
import youtube_dl
import sys

def help():
    print("%s <file>" % sys.argv[0])
    print("<file> is a csv file with these columns:")
    print("    url, artist, title, album")
    print("album can be null")
    print("collumns are separated by a pipe (|)")
    print("the file must begin with a header row")
    sys.exit(0)

def crash(msg):
    print(msg)
    sys.exit(1)

def format_filename(fname):
    ext_index = fname.rfind('.')
    return fname[:ext_index] + ".ogg"

# parse arguments
if len(sys.argv) == 1 or sys.argv[1] in ['-h', '--help']:
    help()

# load the csv
videos = []

try:
    with open(sys.argv[1]) as f:
        reader = csv.DictReader(f, delimiter='|')
        for row in reader:
            videos.append(row)
            
except FileNotFoundError:
    crash("File %s was not found!" % sys.argv[1])
except IOError as e:
    crash("I/O error: %s" % e.strerror)
except Exception as e:
    crash("Error: %s" % e.strerror)


# download the videos
ydl_opts = {
    'format': 'bestaudio/best',  # idk if this is necessary
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'vorbis',
        'preferredquality': '4'
    }]
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for video in videos:
        url = video['url']
        info = ydl.extract_info(url, download=True)
        video['filename'] = ydl.prepare_filename(info)


# add metadata to the downloaded files
for video in videos:
   print("Tagging \"%s\"" % video['title'])
   
   f = music_tag.load_file(format_filename(video['filename']))
   f['title'] = video['title']
   f['artist'] = video['artist']
   if video['album']: f['album'] = video['album']
   f.save()
