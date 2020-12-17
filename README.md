# Youtube-dl Music Downloader
An useful youtube-dl wrapper to download music

## Usage
Install the `youtube-dl` and `eyeD3` packages:

```bash
pip3 install youtube-dl
pip3 install eyeD3
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

The _album_ columnt can be empty (but you have to keep the | at the end). See `example.csv` for an example.

You then run the script like this:
```bash
python3 download.py <filename>
```

The downloaded files are automatically converted to MP3 and tagged properly.
