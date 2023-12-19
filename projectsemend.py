import moviepy.editor as mp
from gtts import gTTS
from pydub import AudioSegment
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk


def video_to_audio(video_file, audio_file, progress_bar, status_label):
    video_clip = mp.VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file)
    progress_bar["value"] = 100
    status_label.config(text="Video to Audio conversion successful!")

def text_to_audio(text_file, audio_file, status_label):
    with open(text_file, 'r') as f:
        text = f.read()
    tts = gTTS(text)
    tts.save(audio_file)
    status_label.config(text="Text to Audio conversion successful!")

def convert_video_to_audio(progress_bar, status_label):
    video_file = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if video_file:
        audio_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio Files", "*.wav")])
        if audio_file:
            progress_bar["value"] = 50
            status_label.config(text="Converting video to audio...")
            video_to_audio(video_file, audio_file, progress_bar, status_label)

def convert_text_to_audio(progress_bar, status_label):
    text_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if text_file:
        audio_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio Files", "*.wav")])
        if audio_file:
            status_label.config(text="Converting text to audio...")
            text_to_audio(text_file, audio_file, status_label)

def exit_app():
    app.quit()

app = tk.Tk()
app.title("Any_To_Audio")
app.attributes("-fullscreen", True)

app.configure(bg="#3498db")

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10, background="#e74c3c", foreground="black")

button_video_to_audio = ttk.Button(app, text="Convert Video to Audio", command=lambda: convert_video_to_audio(progress_bar, status_label))
button_text_to_audio = ttk.Button(app, text="Convert Text to Audio", command=lambda: convert_text_to_audio(progress_bar, status_label))
button_exit = ttk.Button(app, text="Exit", command=exit_app)

button_video_to_audio.pack(pady=10)
button_text_to_audio.pack(pady=10)
button_exit.pack(pady=10)

progress_bar = ttk.Progressbar(app, length=200, mode="determinate")
progress_bar.pack(pady=10)

status_label = tk.Label(app, text="", font=("Helvetica", 14))
status_label.pack(pady=10)

app.mainloop()