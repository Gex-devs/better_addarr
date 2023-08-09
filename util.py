from PIL import Image
import requests
from io import BytesIO

def send_combined_album(image_urls):
    images = []
    desired_width = 400  # Adjust this value based on your preference

    # Load and resize images
    for url in image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            width, height = img.size
            aspect_ratio = height / width
            desired_height = int(desired_width * aspect_ratio)
            resized_img = img.resize((desired_width, desired_height))
            images.append(resized_img)

    # Combine images into a single row
    combined_image = Image.new("RGB", (desired_width * len(images), desired_height))
    x_offset = 0
    for img in images:
        combined_image.paste(img, (x_offset, 0))
        x_offset += desired_width

    # Save the combined image to a file-like object
    output_stream = BytesIO()
    combined_image.save(output_stream, format="JPEG")
    output_stream.seek(0)

    return output_stream

def cleanUp():
    print("clean up")
