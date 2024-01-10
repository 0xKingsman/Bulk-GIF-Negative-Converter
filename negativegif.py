import os
from PIL import Image, ImageOps

# Get the current working directory where the Python script is located
directory = os.getcwd()

# Loop through each file in the directory
for file_name in os.listdir(directory):
    # Check if the file is a GIF image
    if file_name.endswith(".gif"):
        # Open the GIF image
        gif_image = Image.open(os.path.join(directory, file_name))

        # Create a list to hold each frame in the GIF image
        frames = []

        # Loop through each frame in the GIF image
        for frame in range(gif_image.n_frames):
            # Go to the specified frame
            gif_image.seek(frame)

            # Invert the colors of the frame
            negative_frame = ImageOps.invert(gif_image.convert('RGB'))

            # Append the negative frame to the list of frames
            frames.append(negative_frame)

        # Save the negative GIF image, replacing the original file
        frames[0].save(os.path.join(directory, file_name), format="GIF", save_all=True, append_images=frames[1:])
