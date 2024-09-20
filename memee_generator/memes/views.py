from django.shortcuts import render
from .forms import MemeForm
from PIL import Image, ImageDraw, ImageFont
import io
import base64

def generate_meme(request):
    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            top_text = form.cleaned_data['top_text']
            bottom_text = form.cleaned_data['bottom_text']
            image_file = request.FILES['image']

            # Open the image using Pillow
            img = Image.open(image_file)
            draw = ImageDraw.Draw(img)

            # Define font and size (ensure you have the font file)
            font_path = 'path/to/impact.ttf'  # Update this path to your font file
            font_size = int(img.size[1] / 10)  # Font size based on image height
            font = ImageFont.truetype(font_path, font_size)

            # Add text to image (adjust positioning as needed)
            draw.text((10, 10), top_text, font=font, fill="white")
            draw.text((10, img.size[1] - font_size - 10), bottom_text, font=font, fill="white")

            # Save the modified image to a BytesIO object
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)

            # Encode the image to base64 for rendering in HTML
            meme_image_base64 = base64.b64encode(img_byte_arr.getvalue()).decode('utf-8')

            return render(request, 'memes/meme_result.html', {'meme_image': meme_image_base64})

    else:
        form = MemeForm()
    return render(request, 'memes/meme_form.html', {'form': form})