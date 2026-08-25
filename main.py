from pathlib import Path

import whisper

# receive a file path from the user
file_path = input("Please enter the absolute path to the audio file: ").strip()
if len(file_path) >= 2 and file_path[0] == file_path[-1] and file_path[0] in {"'", '"'}:
    file_path = file_path[1:-1]
file_path = Path(file_path).expanduser()

if not file_path.is_file():
    print(f"The file does not exist: {file_path}")
    raise SystemExit(1)

#load whisper model
model = whisper.load_model("base")
result = model.transcribe(str(file_path))
print(result["text"])