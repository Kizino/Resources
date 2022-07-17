from webbrowser import get
from PIL import Image
from io import BytesIO
import base64
import requests

# Convert Image to Base64 
def im_2_b64(image):
    buff = BytesIO()
    image.save(buff, format="JPEG")
    img_str = base64.b64encode(buff.getvalue())
    return img_str

# Convert Base64 to Image
def b64_2_img(data):
    buff = BytesIO(base64.b64decode(data))
    return Image.open(buff)

# Convert Image from Web to Base64
def get_as_base64_from_url(url):
    return base64.b64encode(requests.get(url).content)


def convert_b64_2_data_uri(b64_img):
    return f"data:image/png;base64,{b64_img.decode('ascii')}"

if __name__ == "__main__":
    image = (get_as_base64_from_url('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_92x30dp.png'))

    # Convert img to b64
    # img = Image.new('RGB', (120, 90), 'red')
    # img.show()

    # img_b64 = im_2_b64(img)
    # print(img_b64)

    # Convert b64 back to img
    # new_img = b64_2_img(img_b64)
    # new_img.show()

    # new_img = b64_2_img(image)
    # new_img.show()

    # Convert b64 to data-uri
    print(convert_b64_2_data_uri(image))