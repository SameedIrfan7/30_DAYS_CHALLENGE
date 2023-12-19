from moviepy.editor import VideoFileClip

def convert_video_to_audio(input_video, output_audio):
    # Load the video file
    video = VideoFileClip(input_video)

    # Extract audio from the video
    audio = video.audio

    # Save the audio to an mp3 file
    audio.write_audiofile(output_audio)

    # Close the video file
    video.close()

if __name__ == "__main__":
    input_video = "videomoti.mp4"  # Change the input video file name
    output_audio = "audio.mp3"  # Change the output audio file name

    convert_video_to_audio(input_video, output_audio)

