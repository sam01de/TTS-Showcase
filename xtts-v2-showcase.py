from TTS.api import TTS
import torch
import argparse
import os
from pydub import AudioSegment

def convert_audio_to_wav(audio_path):
    """
    Convert audio file to WAV format if needed.
    Supports common formats: mp3, m4a, flac, ogg, etc.
    Returns path to WAV file (original or temporary converted file).
    """
    # Check if already WAV
    if audio_path.lower().endswith('.wav'):
        return audio_path, None
    
    # Detect format from extension
    file_ext = os.path.splitext(audio_path)[1].lower().lstrip('.')
    base_name = os.path.basename(audio_path)
    base_name_no_ext = os.path.splitext(base_name)[0]
    
    # Create temp_converted directory if it doesn't exist
    temp_dir = os.path.join(os.path.dirname(__file__), 'input', 'converted')
    os.makedirs(temp_dir, exist_ok=True)
    
    # Create WAV file path in temp_converted folder
    temp_wav_path = os.path.join(temp_dir, f"{base_name_no_ext}.wav")
    
    # Load audio in original format
    print(f"Converting {file_ext.upper()} to WAV format...")
    audio = AudioSegment.from_file(audio_path, format=file_ext)
    
    # Export as WAV
    audio.export(temp_wav_path, format='wav')
    print(f"Converted to: {temp_wav_path}")
    
    return temp_wav_path, temp_wav_path

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Generate speech using XTTS-v2 voice cloning')
parser.add_argument('--text', '-t', type=str, default="This exercise is the best. Truly great. Nobody knows more about speech-synthesis than I do.", help='Text to convert to speech')
parser.add_argument('--output', '-o', type=str, default='best_exercise.wav', help='Filename. Will be saved in output/')
parser.add_argument('--speaker', '-s', type=str, default='trump_voice.wav', 
                    help='Path to speaker reference audio in input/ (supports WAV, MP3, M4A, FLAC, OGG, etc.)')
parser.add_argument('--language', '-l', type=str, default='en', 
                    help='Language code (default: en)')
parser.add_argument('--delete-converted', action='store_true',
                    help='Delete converted audio files after use (default: keep in input/temp_converted/)')
args = parser.parse_args()

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# Convert speaker audio to WAV if needed
speaker_wav_path, temp_file = convert_audio_to_wav(args.speaker)

try:
    # Generate speech by cloning a voice using provided parameters
    tts.tts_to_file(text=args.text, 
                    file_path='output/' + (args.output if args.output.lower().endswith('.wav') else args.output + '.wav'),
                    speaker_wav='input/' + speaker_wav_path,
                    split_sentences=False,
                    language=args.language)
    print(f"Successfully generated speech: {args.output}")
finally:
    # Clean up temporary converted file if --delete-converted is specified
    if temp_file and os.path.exists(temp_file):
        if args.delete_converted:
            os.unlink(temp_file)
            print(f"Cleaned up temporary converted file")
        else:
            print(f"Converted file kept at: {temp_file}")