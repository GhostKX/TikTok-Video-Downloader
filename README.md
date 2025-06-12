# 🎭 TikTok Downloader Scripts Collection

A **powerful collection of Python scripts** for downloading TikTok videos and audio using the industry-standard **yt-dlp** library. Choose from **3 specialized scripts** designed for different download scenarios - from high-quality video downloads to audio-only extractions.

Built with **robust error handling**, **automatic codec optimization**, and **clean file management**, these scripts provide **reliable TikTok content downloading** with comprehensive browser emulation and anti-detection features.

---

## ✨ Features

### 🎵 Audio Downloads
- **High-Quality MP3 Audio Extraction** from TikTok videos
- **Automatic Format Conversion** with best audio quality
- **Zero Quality Loss** during audio extraction
- **Smart Browser Emulation** to bypass restrictions
- **Clean Output Directory Management**

### 🎬 Video Downloads
- **Multiple Quality Options** - from optimized to maximum resolution
- **Smart Codec Detection** - H.264 compatibility optimization
- **Dual Quality Modes** for different use cases
- **Automatic Format Standardization** to MP4
- **Advanced Browser User-Agent Spoofing**

### 🔧 Advanced Processing
- **yt-dlp Integration** for professional-grade downloading
- **Automatic Codec Optimization**
- **Chrome Browser Emulation**
- **Anti-Detection Technology**
- **Metadata Preservation**

---

## 🔧 Requirements

### System Dependencies
- **Python 3.8+**
- **yt-dlp** (latest version)
- **Stable Internet Connection**

### Python Libraries
```
yt-dlp>=2025.6.9
```

---

## 🚀 Installation

### 1. Clone or Download the Scripts
```bash
git clone <TikTok-Video-Downloader>
cd TikTok-Video-Downloader
```

### 2. Install Python Dependencies
```bash
pip install yt-dlp
```

### 3. Verify yt-dlp Installation
```bash
yt-dlp --version
```

### 4. Configure Your TikTok URL
Edit the script you want to use and replace the placeholder URL:
```python
url = 'https://www.tiktok.com/@username/video/1234567890123456789'
```

### 5. Run Your Chosen Script
```bash
python public_single_link_audio_downloader.py
```

---

## 📱 Script Overview

### 🎵 Audio Extraction Script

#### **`public_single_link_audio_downloader.py`** - Premium Audio Extraction
- **Downloads** best available audio stream from TikTok
- **Converts** to MP3 with zero quality loss
- **Output Directory**: `TikTok_Audio/`
- **Filename Format**: `[Video Title].mp3`
- **Features**: 
  - Advanced browser emulation
  - Best audio quality extraction (`--audio-quality 0`)
  - Automatic MP3 conversion
  - Chrome user-agent spoofing

### 🎬 Video Download Scripts

#### **`public_single_link_video_downloader_lower_quality.py`** - Optimized Quality Download
- **Downloads** H.264 encoded videos for maximum compatibility
- **Smart codec filtering** for optimal performance
- **Output Directory**: `TikTok_Video/Low/`
- **Filename Format**: `[Video Title].mp4`
- **Features**: 
  - H.264 codec preference
  - Balanced quality-to-size ratio
  - Enhanced error handling
  - Automatic MP4 format merging

#### **`public_sinlge_link_video_downloader_higher_quality.py`** - Maximum Quality Download
- **Downloads** best available video quality
- **No codec restrictions** for maximum fidelity
- **Output Directory**: `TikTok_Video/High/`
- **Filename Format**: `[Video Title].mp4`
- **Features**: 
  - Best quality format selection (`-f b`)
  - Maximum resolution preservation
  - Advanced error handling
  - Automatic MP4 format optimization

---

## 📖 Usage Guide

### Basic Usage Flow

#### 1. **Choose Your Script**
Select based on your needs:
- 🎵 **Audio only**: `public_single_link_audio_downloader.py`
- ⚖️ **Balanced quality**: `public_single_link_video_downloader_lower_quality.py`
- 🏆 **Maximum quality**: `public_sinlge_link_video_downloader_higher_quality.py`

#### 2. **Get TikTok Video URL**
```
1. Open TikTok video in browser/app
2. Click 'Share' button
3. Copy link (format: https://www.tiktok.com/@username/video/1234567890123456789)
```

#### 3. **Configure the URL**
```python
url = 'https://www.tiktok.com/@username/video/1234567890123456789'
```

#### 4. **Run the Script**
```bash
python public_single_link_audio_downloader.py
```

#### 5. **Monitor Progress**
Watch the console output for download progress and processing status.

### Example Processing Flow:
```
🔍 Analyzing TikTok video...
📊 Video Title: "Amazing TikTok Dance"
🌐 Using Chrome browser emulation...
⬇️ Downloading audio stream...
🎧 Converting to MP3 format...
✅ Download complete: TikTok_Audio/Amazing TikTok Dance.mp3
✅ Process finished successfully!
```

---

## 📊 Detailed Script Comparison

### Complete Feature Matrix

| Script | Purpose | Quality | Output Directory | Format | Codec | File Size | Speed |
|--------|---------|---------|------------------|--------|-------|-----------|-------|
| `audio_downloader.py` | Audio extraction | Best audio | `TikTok_Audio/` | MP3 | Best available | Small | Fast  |
| `video_downloader_lower_quality.py` | Balanced video | H.264 optimized | `TikTok_Video/Low/` | MP4 | H.264 | Medium | Fast  |
| `video_downloader_higher_quality.py` | Maximum video | Best available | `TikTok_Video/High/` | MP4 | Any | Large | Fast  |

### Quality vs Performance Trade-offs

#### **Fastest Download** ⚡
- **Use**: `public_single_link_audio_downloader.py`
- **Pros**: Small files, quick processing, universal compatibility
- **Cons**: Audio only, no video content

#### **Best Balance** ⚖️
- **Use**: `public_single_link_video_downloader_lower_quality.py`
- **Pros**: Good quality, reasonable file size, H.264 compatibility
- **Cons**: May not capture absolute maximum quality

#### **Maximum Quality** 🏆
- **Use**: `public_sinlge_link_video_downloader_higher_quality.py`
- **Pros**: Best possible quality, no codec restrictions
- **Cons**: Larger files, longer download times

---

## 🔍 Advanced Features

### Smart Browser Emulation
All scripts use advanced browser spoofing to avoid detection:
```python
"--user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
```

### Intelligent Format Selection
Scripts automatically choose optimal formats:
```python
# Audio Script: Best audio with MP3 conversion
"-f", "bestaudio/best", "-x", "--audio-format", "mp3"

# Lower Quality: H.264 compatible video
"-f", "best[ext=mp4][vcodec*=h264]"

# Higher Quality: Best available format
"-f b"
```

### Automatic Directory Management
Scripts create organized folder structures:
```
TikTok-Downloads/
├── TikTok_Audio/           # Audio files (.mp3)
├── TikTok_Video/
│   ├── Low/                # H.264 optimized videos
│   └── High/               # Maximum quality videos
```

### Enhanced Error Handling
Comprehensive error management:
```python
try:
    subprocess.run(command)
except Exception as e:
    print(f"Download failed: {e}")
    # Graceful error handling and user feedback
```

---

## 🛠️ Configuration Options

### Audio Quality Settings
```python
"--audio-quality", "0"      # Best quality (0 = best, 9 = worst)
```

### Video Format Preferences
```python
# Lower Quality Script
"-f", "best[ext=mp4][vcodec*=h264]"    # H.264 codec priority

# Higher Quality Script  
"-f b"                                  # Best format available
```

### Output Filename Templates
```python
"-o", "TikTok_Audio/%(title)s.%(ext)s"     # Audio files
"-o", "TikTok_Video/Low/%(title)s.%(ext)s" # Lower quality videos
"-o", "TikTok_Video/High/%(title)s.%(ext)s" # Higher quality videos
```

---

## 📄 File Output Reference

| Script | Output Location | Filename Format | File Extension | Typical Size | Quality Level |
|--------|-----------------|----------------|----------------|--------------|---------------|
| Audio Downloader | `TikTok_Audio/` | `[Video Title].mp3` | .mp3 | 1-10 MB      | Best Audio |
| Lower Quality Video | `TikTok_Video/Low/` | `[Video Title].mp4` | .mp4 | 5-25 MB      | H.264 Optimized |
| Higher Quality Video | `TikTok_Video/High/` | `[Video Title].mp4` | .mp4 | 10-25 MB     | Maximum Available |


---

## 📊 Performance Benchmarks

### Average Download Times*
| Script Type | File Size | Download Time | Processing Time | Total Time   |
|-------------|-----------|---------------|-----------------|--------------|
| Audio Only | 10 MB     | 5-15 seconds  | 2-5 seconds | 5-15 seconds |
| Lower Quality | 20 MB     | 5-20 seconds  | 3-8 seconds | 5-20 seconds |
| Higher Quality | 25 MB     | 5-20 seconds  | 5-15 seconds | 5-20 seconds |

*Times vary based on internet speed, video length, and system performance

---

## 👨‍💻 Author

Developed by **GhostKX**

- 🌐 **GitHub**: [@GhostKX](https://github.com/GhostKX)
