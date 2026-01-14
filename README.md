# yt-dlp Music Downloader
A useful youtube-dl wrapper to download music

## Usage
Install the `yt-dlp` and `music-tag` packages:

```bash
pip3 install yt-dlp
pip3 install music-tag
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

The _album_ column can be empty (but you have to keep the | at the end).
Multiple artists can be specified by separating them with `&&`.
See `example.csv` for an example.

You then run the script like this:
```bash
python3 download.py <filename>
```

The downloaded files are automatically converted to OGG/Vorbis and tagged properly.

### Running from a virtual environment
Some Python installations nowadays (such as in Debian) complain when you try to install PIP packages globally.
To make invoking the script with a virtual environment easier, there is a `download.sh` script which activates the virutal environment (must be named `venv`) and runs `download.py`.

Practical example:

```bash
python3 -m venv venv
. venv/bin/activate
pip3 install yt-dlp
pip3 install music-tag

# in a different terminal
./download.sh list.csv
```

The script even works when being symlinked to, so you don't have to clutter your music directory with the venv:

```bash
ln -s <repo path>/download.sh ~/Music/download.sh
cd ~/Music
./download.sh list.csv
```
