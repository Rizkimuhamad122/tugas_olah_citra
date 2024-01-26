from PIL import Image, ImageFilter

original_image = Image.open("BLUR.jpeg")
blurred_image = original_image.filter(ImageFilter.BLUR)

original_image.show()
blurred_image.show()
blurred_image.save()