from moviepy.config import change_settings
from moviepy.editor import AudioFileClip, ImageClip, TextClip, CompositeVideoClip

# Set the path to ImageMagick
change_settings({"IMAGEMAGICK_BINARY": "C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"})

def create_video_from_audio(
    audio_path,
    image_path,
    output_path,
    title_text,
    logo_path,
    text_fontsize=20,
    logo_size=100,
    logo_margin=20,
    text_margin_bottom=50
):
    """
    Create a video with a background image, audio, a bottom-center title with shadow and border, and a top-left logo.

    :param audio_path: Path to the MP3 file.
    :param image_path: Path to the background image.
    :param output_path: Path to save the output video.
    :param title_text: Text to display at the bottom center of the video.
    :param logo_path: Path to the logo image (e.g., Facebook logo).
    :param text_fontsize: Font size for the bottom-center text.
    :param logo_size: Height of the logo in pixels.
    :param logo_margin: Margin around the logo in pixels.
    :param text_margin_bottom: Margin from the bottom of the video frame for the text.
    """
    # Load the audio
    audio = AudioFileClip(audio_path)

    # Load the background image and set duration to match the audio
    image = ImageClip(image_path).set_duration(audio.duration).resize(height=720, width=1280)

    # Add Facebook logo in the top-left corner with margin
    logo = (
        ImageClip(logo_path)
        .set_duration(audio.duration)
        .resize(height=logo_size)  # Resize logo height
        .set_position((logo_margin, logo_margin))  # Add margin
    )

    # Add border text as shadow (offset for visibility)
    shadow_offset = 3  # Offset for the shadow effect
    border = TextClip(
        title_text,
        fontsize=text_fontsize,
        color="black",  # Shadow color
        font="Arial",
        align="center",
    ).set_position(("center", 720 - text_margin_bottom + shadow_offset)).set_duration(audio.duration)

    # Add main text in white on top of the border
    text = TextClip(
        title_text,
        fontsize=text_fontsize,
        color="white",  # Main text color
        font="Arial",
        align="center",
    ).set_position(("center", 720 - text_margin_bottom)).set_duration(audio.duration)

    # Combine all elements (background image, logo, border, and text)
    video = CompositeVideoClip([image, logo, border, text])

    # Set the audio to the video
    video = video.set_audio(audio)

    # Export the video
    video.write_videofile(output_path, fps=24, codec="libx264", audio_codec="aac")

# Example usage
audio_file = "quran/001 - Al-Fatihah ( The Opening ) - A Abertura  .mp3"            # Path to the Quran MP3 file
image_file = "image/samsommer-vddccTqwal8-unsplash.jpg"            # Path to the background image
logo_file = "logo/facebook.png"              # Path to the Facebook logo image
output_file = "output/114.A Sura dos Humanos.mp4"          # Path to save the output video
title = "114.A Sura dos Humanos"                 # Title to display on the video
text_fontsize = 50                           # Font size for the bottom title

create_video_from_audio(
    audio_path=audio_file,
    image_path=image_file,
    output_path=output_file,
    title_text=title,
    logo_path=logo_file,
    text_fontsize=text_fontsize,
    logo_size=100,  # Adjust logo size
    logo_margin=20,  # Adjust logo margin
    text_margin_bottom=100  # Adjust margin for the bottom text
)
