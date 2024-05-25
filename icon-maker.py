# Import necessary libraries
from PIL import Image
import imageio.v2 as imageio  # Use imageio.v2 to maintain previous behavior
import os

# Function to resize an image to the specified output size
def resize_image(image, output_size):
    return image.resize(output_size)

# Function to create an animated GIF from a folder containing images
def create_animated_gif_from_images(folder_path, output_gif, output_size):
    # Get a list of image files (JPG, JPEG, PNG) in the specified folder
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp', '.svg'))]

    images = []
    duration = 500  # Duration between frames (in milliseconds)

    # Iterate over each image file, resize it, and append it to the list of images
    for image_file in image_files:
        image = Image.open(os.path.join(folder_path, image_file))  # Open the image file
        resized_image = resize_image(image, output_size)  # Resize the image
        images.append(resized_image)  # Append the resized image to the list

    # Save the resized images as individual frames
    for idx, img in enumerate(images):
        frame_output_path = os.path.join(folder_path, f"frame_{idx}.png")
        img.save(frame_output_path, "PNG")

    # Collect the frames from the folder
    frame_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().endswith('.png')]

    # Create the animated GIF with looping
    gif_images = [imageio.imread(frame) for frame in frame_files]
    imageio.mimsave(output_gif, gif_images, format='GIF', duration=duration / 1000, loop=0)

    print(f"Animated GIF with input images from folder '{folder_path}' created as '{output_gif}'")

# Input path to the folder containing image files
input_folder_path = "input"

# Output path for the animated GIF file
output_folder_path = "output"
os.makedirs(output_folder_path, exist_ok=True)  # Create the output folder if it doesn't exist

# Specify the output animated GIF file
output_gif = os.path.join(output_folder_path, "animoji.gif")

# Output image size for resizing
output_size = (72, 72)  # Default size is set to 72x72 pixels

# Function call to create the animated GIF from input images
create_animated_gif_from_images(input_folder_path, output_gif, output_size)
