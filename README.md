# XTTS-v2 Voice Cloning Showcase

A simple command-line tool for text-to-speech synthesis using the XTTS-v2 model with voice cloning capabilities.

## 🚀 Quick Start for Windows Uni-PCs

**Step-by-step guide for university computers without conda:**

1. **Download this repository**
   - Click the green "Code" button → "Download ZIP"
   - Extract the ZIP file to your desired location

2. **Open Command Prompt (cmd)**
   - Press `Win + R`, type `cmd`, press Enter
   - Navigate to the extracted folder:
     ```bash
     cd path\to\TTS-Showcase
     ```

3. **Create Python environment**
   ```bash
   python -m venv ai-hci-showcase
   ```

4. **Activate environment**
   ```bash
   ai-hci-showcase\Scripts\activate
   ```
   (You should see `(ai-hci-showcase)` at the start of your command line)

5. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   (This will take a few minutes)

6. **Run the showcase**
   ```bash
   python xtts-v2-showcase.py
   ```
   (First run will download the model ~1.8GB and generate `output/best_exercise.wav`)

7. **Create your own speech (optionally specify your own voice file)**
   ```bash
   python xtts-v2-showcase.py -t "Your text here" -o my_output.wav -s your_voice_file.wav
   ```
   *If you omit `-s`, the default voice sample will be used. For best results, provide a short, clean WAV file with 10-15 seconds of audio as your voice sample.*

8. **Get help anytime**
   ```bash
   python xtts-v2-showcase.py --help
   ```

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

**Using Conda (All platforms):**
```bash
conda create -n ai-hci-showcase python=3.10 pip -y
conda activate ai-hci-showcase
pip install -r requirements.txt
```

**Using Python venv (Linux/Mac):**
```bash
python -m venv ai-hci-showcase
source ai-hci-showcase/bin/activate
pip install -r requirements.txt
```

**Using Python venv (Windows):**
```cmd
python -m venv ai-hci-showcase
ai-hci-showcase\Scripts\activate
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
python xtts-v2-showcase.py -t "TEXT" -o output_file.wav -s speaker_file.wav
```

### Arguments

- `-t`, `--text`: Text to convert to speech
- `-o`, `--output`: Output filename (saved in `output/` folder)
- `-s`, `--speaker`: Speaker audio filename (from `input/` folder, default: `trump_voice.wav`)
  - Supports: WAV, MP3, M4A, FLAC, OGG, and more
  - Non-WAV files are automatically converted
- `-l`, `--language`: Language code (default: `en`)
  - Examples: `en`, `de`, `es`, `fr`, `it`, `pt`, `pl`, `tr`, `ru`, `nl`, `cs`, `ar`, `zh-cn`, `ja`, `hu`, `ko`
- `--delete-converted`: Delete converted audio files after use (default: keep in `input/converted/` for reuse)

### Examples

**Basic usage (English):**
```bash
python xtts-v2-showcase.py \
  -t "Hello everyone, welcome to this presentation!" \
  -o greeting.wav \
  -s my_voice.wav
```


## Notes

- The first run will download the XTTS-v2 model (~1.8GB)
- GPU acceleration is automatic if CUDA is available
- Text longer than 250 characters may be truncated (warning will be shown)
- Output is always in WAV format
- Non-WAV speaker files are automatically converted to WAV and kept in `input/converted/` for reuse (unless `--delete-converted` is specified)

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
