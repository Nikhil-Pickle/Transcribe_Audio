# Audio Transcription to SRT

This project transcribes an audio file using OpenAI Whisper and saves the result as an SRT subtitle file in the same folder as the original audio.

## What it does

- Accepts an audio file path as a command-line argument
- Loads the Whisper "base" model
- Transcribes the audio into timed segments
- Writes a matching `.srt` file with the same name as the input file

## Usage

1. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Install FFmpeg on your system:

   macOS (Homebrew):
   ```bash
   brew install ffmpeg
   ```

   Windows:
   ```powershell
   winget install Gyan.Dev.FFmpeg
   ```

3. Run the script:

   ```bash
   python main.py "/path/to/audio.wav"
   ```

4. The script creates a subtitle file such as:

   ```bash
   /path/to/audio.srt
   ```

## Requirements

- Python
- `openai-whisper`
- FFmpeg

## License

MIT
