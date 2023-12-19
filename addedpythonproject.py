import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter.font import Font
import tkinter.scrolledtext as scrolledtext
import moviepy.editor as mp
from gtts import gTTS
from pydub import AudioSegment
import os

def video_to_audio(video_file, audio_file):
    video_clip = mp.VideoFileClip(video_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_file)
    progress_bar["value"] = 100
    status_label.config(text="Video to Audio conversion successful!", foreground="green")

def text_to_audio(text_file, audio_file):
    with open(text_file, 'r') as f:
        text = f.read()
    tts = gTTS(text)
    tts.save(audio_file)
    status_label.config(text="Text to Audio conversion successful!", foreground="green")

def convert_video_to_audio():
    video_file = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if video_file:
        audio_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio Files", "*.wav")])
        if audio_file:
            progress_bar["value"] = 50
            status_label.config(text="Converting video to audio...", foreground="blue")
            video_to_audio(video_file, audio_file)

def convert_text_to_audio():
    text_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if text_file:
        audio_file = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Audio Files", "*.wav")])
        if audio_file:
            status_label.config(text="Converting text to audio...", foreground="blue")
            text_to_audio(text_file, audio_file)

def exit_app():
    if messagebox.askyesno("Exit", "Do you want to exit the application?"):
        app.quit()

# Create the main application window
app = tk.Tk()
app.title("AnyToAudio")
app.geometry("600x500")  # Set the window dimensions
app.configure(bg="#f4f4f4")  # Set background color

# Create a custom font for labels and buttons
custom_font = Font(family="Arial", size=12)

# Create labels with custom styling
label1 = ttk.Label(app, text="Select an option:", font=(custom_font, 16), background="#f4f4f4", foreground="#333")
label1.pack(pady=(20, 10))

# Create buttons with custom styling
button_video_to_audio = ttk.Button(app, text="Convert Video to Audio", command=convert_video_to_audio, style='TButton')
button_text_to_audio = ttk.Button(app, text="Convert Text to Audio", command=convert_text_to_audio, style='TButton')
button_exit = ttk.Button(app, text="Exit", command=exit_app, style='TButton')

# Position the buttons
button_video_to_audio.pack(pady=10, padx=20, fill=tk.X)
button_text_to_audio.pack(pady=10, padx=20, fill=tk.X)
button_exit.pack(pady=10, padx=20, fill=tk.X)

# Create a progress bar
progress_bar = ttk.Progressbar(app, length=400, mode="determinate")
progress_bar.pack(pady=10)

# Create a status label
status_label = ttk.Label(app, text="", font=(custom_font, 12), background="#f4f4f4", foreground="#333")
status_label.pack(pady=10)

# Add a style for buttons
style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=10, background="#3498db", foreground="white")  # Set button colors

# Add a placeholder logo
logo = tk.PhotoImage(file="SPIDY.png")  # Replace with your logo file path
logo_label = ttk.Label(app, image=logo, background="#f4f4f4")
logo_label.pack(pady=(10, 0))

# Run the main event loop
app.mainloop()
