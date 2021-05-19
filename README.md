# Youtube-dl Music Downloader
An useful youtube-dl wrapper to download music

## Usage
Install the `youtube-dl` and `music_tag` packages:

```bash
pip3 install youtube-dl
pip3 install music_tag
```

Specify the songs to download. This is done using a csv file with these columns:
- `url`
- `artist`
- `title`
- `album`

The columns are separated with a "|" and the first line of the file must be like this:
```
url|artist|title|album
```

The _album_ column can be empty (but you have to keep the | at the end). See `example.csv` for an example.

You then run the script like this:
```bash
python3 download.py <filename>
```

The downloaded files are automatically converted to OGG/Vorbis and tagged properly.
