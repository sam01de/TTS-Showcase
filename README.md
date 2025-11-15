# XTTS-v2 Voice Cloning Showcase

A simple command-line tool for text-to-speech synthesis using the XTTS-v2 model with voice cloning capabilities.

## Get started

### 1. System Requirements

If you do not use a WAV file as speaker reference, you need to install **ffmpeg** for audio format conversion:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html)

### 2. Python Dependencies

Create a conda or local python environment and install dependencies:

```bash
# Create environment with Conda
conda create -n ai-hci-showcase python=3.10 pip -y
conda activate ai-hci-showcase

# Create environment with Local Python
python -m venv ai-hci-showcase
source ai-hci-showcase/bin/activate

# Install Python packages
pip install -r requirements.txt
```

## Usage

First run:

```bash
python xtts-v2-showcase.py
```

This will download the XTTS-v2 model (~1.8GB). After the run "output" should contain 'best_exercise.wav'.

Basic syntax:

```bash
python xtts-v2-showcase.py -t "MY TEXT" -o OUTPUT-Filename.wav -s Speaker-Filename.wav [-l LANGUAGE]
```

### Arguments

- `-t`, `--text`: Text to convert to speech
- `-o`, `--output`: Output WAV filename. Will be saved in output/
- `-s`, `--speaker`: Path to speaker reference audio in input/ (default: `trump_voice.wav`). The file will be converted to WAV if needed.
  - Supports: WAV, MP3, M4A, FLAC, OGG, and more
- `-l`, `--language`: Language code (default: `en`)
  - Examples: `en`, `de`, `es`, `fr`, `it`, `pt`, `pl`, `tr`, `ru`, `nl`, `cs`, `ar`, `zh-cn`, `ja`, `hu`, `ko`
- `--delete-converted`: Delete converted audio files after use (default: keep in `input/converted/` for reuse)

### Examples

**Basic usage (English):**
```bash
python xtts-v2-showcase.py \
  -t "Hello everyone, welcome to this presentation!" \
  -o output/greeting.wav \
  -s input/my_voice.wav
```


## Notes

- The first run will download the XTTS-v2 model (~1.8GB)
- GPU acceleration is automatic if CUDA is available
- Text longer than 250 characters may be truncated (warning will be shown)
- Output is always in WAV format
- Non-WAV speaker files are automatically converted to WAV and kept in `input/temp_converted/` for reuse (unless `--delete-converted` is specified)

## Troubleshooting

### Error: "Couldn't find ffmpeg or avconv"
Install ffmpeg as described in the Installation section.

### Error: "FileNotFoundError: 'ffprobe'"
ffmpeg is not installed or not in your PATH. Install ffmpeg.

### GPU Out of Memory
The model requires ~2GB of VRAM. If you don't have enough, it will automatically fall back to CPU.

### Model Download Issues
If the model download fails, try manually downloading from [Coqui TTS models](https://github.com/coqui-ai/TTS).

## Supported Languages

English (en), German (de), Spanish (es), French (fr), Italian (it), Portuguese (pt), Polish (pl), Turkish (tr), Russian (ru), Dutch (nl), Czech (cs), Arabic (ar), Chinese (zh-cn), Japanese (ja), Hungarian (hu), Korean (ko), and many more.

## Credits

Built with [Coqui TTS](https://github.com/coqui-ai/TTS) and the XTTS-v2 model.
