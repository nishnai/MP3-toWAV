import os
import sys
from pydub import AudioSegment

def convert_mp3_to_wav(mp3_folder, wav_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(wav_folder, exist_ok=True)

    # Iterate over the MP3 files in the input folder
    for filename in os.listdir(mp3_folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(mp3_folder, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_path = os.path.join(wav_folder, wav_filename)

            # Convert the MP3 file to WAV format
            sound = AudioSegment.from_mp3(mp3_path)
            sound.export(wav_path, format="wav")
            print(f"Converted {filename} to {wav_filename}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python audio_converter.py <mp3_folder> <wav_folder>")
        sys.exit(1)

    # Extract the command-line arguments
    mp3_folder = sys.argv[1]
    wav_folder = sys.argv[2]

    # Call the function to convert MP3 to WAV
    convert_mp3_to_wav(mp3_folder, wav_folder)
