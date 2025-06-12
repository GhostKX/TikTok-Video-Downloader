import subprocess

# TikTok video link
url = 'https://www.tiktok.com/@username/video/video_number'


# Command that actually downloads the audio file of the video and saves it in the mp3 file
command = [
    "yt-dlp",
    "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "-f", "bestaudio/best",
    "-x",
    "--audio-format", "mp3",
    "--audio-quality", "0",
    "-o", "TikTok_Audio/%(title)s.%(ext)s",
    url
]


# Simple error handling to void breaks,
try:
    subprocess.run(command)
except Exception as e:
    print(e)
