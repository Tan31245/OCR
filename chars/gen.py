from PIL import ImageFont, ImageDraw, Image
def textsize(text, font):
    im = Image.new(mode="P", size=(0, 0))
    draw = ImageDraw.Draw(im)
    _, _, width, height = draw.textbbox((0, 0), text=text, font=font)
    return width, height
# Define characters
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Font and image size
font_path = "../Open_Sans/static/OpenSans_SemiCondensed-Regular.ttf"  # Replace with your desired font path
font_size = 200  # Adjust font size as needed
image_size = (500, 500)  # Adjust image size as needed

# Create background color
white = (255, 255, 255)

# Loop through each character
for char in characters:
    # Create new image
    image = Image.new("RGB", image_size, white)
    draw = ImageDraw.Draw(image)

    # Load font
    font = ImageFont.truetype(font_path, font_size)

    # Get text dimensions
    text_width, text_height = textsize(char, font)

    # Center text position
    x = (image_size[0] - text_width) // 2
    y = (image_size[1] - text_height) // 2

    # Draw text
    draw.text((x, y), char, fill=(0, 0, 0), font=font)

    # Save image
    image.save(f"character_{char}.png")

print("Created images for all characters successfully!")