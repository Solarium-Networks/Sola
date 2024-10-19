import tkinter as tk
from tkinter import filedialog, messagebox
import pyaudio
import wave

# Initialize Tkinter root
root = tk.Tk()
root.title("Sola Audio Player")
root.geometry("400x200")

chunk = 1024
p = pyaudio.PyAudio()

# Function to open file dialog and play the audio
def play_audio():
    file = filedialog.askopenfilename(filetypes=[("Audio Files", "*.wav;*.mp3"), ("WAV files", "*.wav"), ("MP3 files", "*.mp3")])
    if not file:
        return

    try:
        f = wave.open(file, 'rb')

        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)

        data = f.readframes(chunk)

        while data:
            stream.write(data)
            data = f.readframes(chunk)

        stream.stop_stream()
        stream.close()

        messagebox.showinfo("Playback", "Playback finished")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Add a button to play audio
play_button = tk.Button(root, text="Select and Play Audio", command=play_audio)
play_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()

# Clean up PyAudio resources when done
p.terminate()