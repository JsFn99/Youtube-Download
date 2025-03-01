# YouTube MP3 Downloader

## Description
This script allows you to search for YouTube videos based on a list of titles and download them as MP3 files. It uses `yt-dlp` to extract the best available audio and convert it to MP3 format.

## Features
- Searches YouTube for a video based on a given query.
- Downloads the best available audio format.
- Converts the downloaded audio to MP3 (192 kbps) using FFmpeg.
- Saves the MP3 files in a designated `downloads` folder.

## Requirements
- Python 3.x
- `yt-dlp` (YouTube downloader)
- `ffmpeg` (for audio extraction)

## Installation
### 1. Install Python dependencies
```bash
pip install yt-dlp
```

### 2. Install FFmpeg
#### macOS (using Homebrew)
```bash
brew install ffmpeg
```
#### Ubuntu/Debian
```bash
sudo apt install ffmpeg
```
#### Windows
Download and install FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html), then add it to your system's PATH.

## Usage
1. Create a `titles.txt` file and add YouTube search queries, one per line.
2. Run the script:
```bash
python script.py
```
3. The MP3 files will be saved in the `downloads` directory.

## Example `titles.txt`
```
Lo-fi chill beats
Best classical music
Coding music playlist
```

## How It Works
1. The script reads `titles.txt` and searches YouTube for the first matching video.
2. It retrieves the video URL and downloads the best audio format.
3. The audio is converted to MP3 and stored in the `downloads` folder.

## Troubleshooting
- If FFmpeg is missing, ensure it is installed and added to your system's PATH.
- If a video is not found, check the query in `titles.txt`.
- If an error occurs during download, ensure `yt-dlp` is up to date:
```bash
pip install --upgrade yt-dlp
```

