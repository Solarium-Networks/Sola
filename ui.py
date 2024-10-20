import tkinter as tk
from tkinter import filedialog, messagebox
import pyaudio
import wave
import threading

# Initialize Tkinter root
root = tk.Tk()
root.title("Sola Audio Player")
root.geometry("400x200")

chunk = 1024
p = pyaudio.PyAudio()

# Flag to stop audio playback
stop_flag = False

# Function to open file dialog and play the audio
def play_audio():
    global stop_flag
    stop_flag = False
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

        while data and not stop_flag:
            stream.write(data)
            data = f.readframes(chunk)

        stream.stop_stream()
        stream.close()

        if not stop_flag:
            messagebox.showinfo("Playback", "Playback finished")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to start audio playback in a new thread
def start_audio_thread():
    audio_thread = threading.Thread(target=play_audio)
    audio_thread.start()

# Function to stop audio playback
def stop_audio_playback():
    global stop_flag
    stop_flag = True

# Add a button to play audio
play_button = tk.Button(root, text="Select and Play Audio", command=start_audio_thread)
play_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop", command=stop_audio_playback)
stop_button.pack()

# Run the Tkinter event loop
root.mainloop()

# Clean up PyAudio resources when done
p.terminate()