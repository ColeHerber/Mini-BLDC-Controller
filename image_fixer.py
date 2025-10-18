# pip install pillow
from PIL import Image

def bw_remove_white(input_path, output_path, threshold=128):
    """
    Converts the image to black and white, then removes white pixels.
    Everything white becomes transparent; everything black remains opaque.
    
    threshold: 0–255 (lower = more black, higher = more white)
    """
    # Convert to grayscale
    img = Image.open(input_path).convert("L")

    # Convert to pure black & white (binarize)
    bw = img.point(lambda x: 255 if x > threshold else 0, "L")

    # Convert to RGBA for transparency
    rgba = bw.convert("RGBA")
    data = rgba.getdata()

    new_data = []
    for item in data:
        r, g, b, a = item
        # white -> transparent
        if r == 255 and g == 255 and b == 255:
            new_data.append((255, 255, 255, 0))
        else:
            new_data.append((0, 0, 0, 255))  # solid black

    rgba.putdata(new_data)
    rgba.save(output_path, "PNG")
    print(f"Saved black/transparent PNG → {output_path}")

# Example:
bw_remove_white("zoom_icon.png", "zoom_icon_transparent.png", threshold=200)