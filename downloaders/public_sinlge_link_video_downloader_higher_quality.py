import subprocess


# TikTok video link
url = 'https://www.tiktok.com/@username/video/video_number'


# Command that actually downloads the video from TikTok and saves it mp4
command = [
    "yt-dlp",
    "--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
    "-f b",
    "-o", "TikTok_Video/High/%(title)s.%(ext)s",
    "--merge-output-format", "mp4",
    url
]


# Simple error handling to void breaks,
try:
    subprocess.run(command)
except Exception as e:
    print(e)