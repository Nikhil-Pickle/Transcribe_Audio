import argparse
from pathlib import Path

import whisper

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Transcribe an audio file with Whisper.")
parser.add_argument("file_path", help="Path to the audio file")
args = parser.parse_args()

# Process the file path argument
file_path = args.file_path.strip()
if len(file_path) >= 2 and file_path[0] == file_path[-1] and file_path[0] in {"'", '"'}:
    file_path = file_path[1:-1]
file_path = Path(file_path).expanduser()

# Check if the file exists
if not file_path.is_file():
    print(f"The file does not exist: {file_path}")
    raise SystemExit(1)

# Function to format timestamps in SRT format
def format_srt_timestamp(seconds):
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    seconds, milliseconds = divmod(milliseconds, 1_000)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"


#load whisper model
model = whisper.load_model("base")
result = model.transcribe(str(file_path))

# Write timed subtitle segments to an SRT file with the same name as the audio file
subtitle_entries = []
for index, segment in enumerate(result["segments"], start=1):
    start = format_srt_timestamp(segment["start"])
    end = format_srt_timestamp(segment["end"])
    text = segment["text"].strip()
    subtitle_entries.append(f"{index}\n{start} --> {end}\n{text}")

# Write the SRT file
output_path = file_path.with_suffix(".srt")
output_path.write_text("\n\n".join(subtitle_entries) + "\n", encoding="utf-8")
print(f"Subtitles written to: {output_path}")