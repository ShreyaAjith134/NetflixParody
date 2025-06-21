from PIL import Image
import os

# Load all original frames
original_frames = [Image.open(f"images/cropped_image ({i}).png").convert("RGBA") for i in range(1, 24)]

# Parameters
frames = []
fade_steps = 5  # Number of blended frames between two images
display_duration = 2000  # Duration for full frame (in ms)
fade_duration = 200  # Duration for each fade frame (in ms)

# Build frames with fading transitions
for i in range(len(original_frames) - 1):
    current = original_frames[i]
    next_frame = original_frames[i + 1]

    # Add the current frame (displayed for longer)
    frames.append((current, display_duration))

    # Create fade transition frames
    for step in range(1, fade_steps + 1):
        alpha = step / (fade_steps + 1)
        blended = Image.blend(current, next_frame, alpha)
        frames.append((blended, fade_duration))

# Add the final frame
frames.append((original_frames[-1], display_duration))

# Save as animated GIF
frames[0][0].save(
    "fading_animated.gif",
    save_all=True,
    append_images=[f[0] for f in frames[1:]],
    duration=[f[1] for f in frames],
    loop=0
)
