# Import necessary libraries
from PIL import Image  # Used for image manipulation
import imageio  # Library for reading and writing images
import os  # Operating system dependent functionality

# Function to resize an image to the specified output size
def resize_image(image, output_size):
    return image.resize(output_size)

# Function to create an animated GIF from a folder containing images
def create_animated_gif_from_images(folder_path, output_gif, output_size):
    # Get a list of image files (JPG, JPEG, PNG) in the specified folder
    image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.jpg', '.jpeg', '.png','.gif','.webp','.bmp','.svg'))]

    images = []
    # Iterate over each image file, resize it, and append it to the list of images
    for image_file in image_files:
        image = Image.open(os.path.join(folder_path, image_file))  # Open the image file
        resized_image = resize_image(image, output_size)  # Resize the image
        images.append(resized_image)  # Append the resized image to the list

    # Save the images as frames in the animated GIF with specified parameters
    images[0].save(output_gif, save_all=True, append_images=images[1:], duration=500, loop=0)

    print(f"Animated GIF with input images from folder '{folder_path}' created as '{output_gif}'")

# Input path to the folder containing image files
input_folder_path = "input"

# Output path for the animated GIF file
output_folder_path = "output"
os.makedirs(output_folder_path, exist_ok=True)  # Create the output folder if it doesn't exist

# Specify the output animated GIF file
output_gif = os.path.join(output_folder_path, "animated_images.gif")

# Output image size for resizing
output_size = (256, 256)  # Default size is set to 256x256 pixels

# Function call to create the animated GIF from input images
create_animated_gif_from_images(input_folder_path, output_gif, output_size)
