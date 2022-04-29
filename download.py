#!/usr/bin/env python3
import csv
import music_tag
from yt_dlp import YoutubeDL
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

def download(video, ydl):
    '''Dowloads a specified video. Returns the dowloaded filename.'''
    url = video['url']
    info = ydl.extract_info(url, download=True)
    return ydl.prepare_filename(info)

def tag(filename, info):
    '''Tags a file with the specified information.'''
    f = music_tag.load_file(format_filename(filename))
    f['title'] = info['title']
    f['artist'] = info['artist']
    if info['album']: f['album'] = info['album']
    f.save()

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

with YoutubeDL(ydl_opts) as ydl:
    for video in videos:
        print(f"Processing {video['title']}")
        print("  - downloading")
        filename = download(video, ydl)

        print("  - tagging")
        tag(filename, video)

