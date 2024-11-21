from moviepy.config import change_settings
from moviepy.editor import AudioFileClip, ImageClip, TextClip, CompositeVideoClip

# Set the path to ImageMagick
change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"})

def create_video_from_audio(audio_path, image_path, output_path, title_text):
    # Load the audio
    audio = AudioFileClip(audio_path)
    
    # Load the background image and set duration to match the audio
    image = ImageClip(image_path).set_duration(audio.duration).resize(height=720, width=1280)
    
    # Add title text with styling
    # Main text
    title = TextClip(
        title_text,
        fontsize=80,  # Larger font size
        color='black',  # Text color
        font='Times-New-Roman',  # Font style (ensure the font is installed on your system)
        size=(1200, None),  # Limit the width, height auto-adjusts
        method='caption'  # Wraps text if it exceeds size
    )
    title = title.set_position(('center', 'center')).set_duration(audio.duration)

    # Add shadow effect (slightly offset black background for depth)
    shadow = TextClip(
        title_text,
        fontsize=80,
        color='gray',
        font='Times-New-Roman',
        size=(1200, None),
        method='caption'
    ).set_position(('center', 'center')).set_duration(audio.duration).set_position(lambda t: ('center', 'center'))

    # Combine the shadow and the main text for a styled effect
    styled_title = CompositeVideoClip([image, shadow.set_position((2, 2)), title])

    # Set the audio to the video
    video = styled_title.set_audio(audio)
    
    # Export the video
    video.write_videofile(output_path, fps=24, codec='libx264', audio_codec='aac')

# Example usage
audio_file = "quran/abertura.mp3"           # Path to the Quran MP3 file
image_file = "image/abertura.jpg"           # Path to the background image
output_file = "quran_video.mp4"             # Output video file path
title = "Recitação do Alcorão"              # Title to display on the video

create_video_from_audio(audio_file, image_file, output_file, title)
