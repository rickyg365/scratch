
import urllib.request

from PIL import Image


image_url = 'https://images.unsplash.com/photo-1622448469111-9627e13ebad2?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=3000&q=80'
new_file_name = 'my_img.png'

urllib.request.urlretrieve(image_url, new_file_name)

img = Image.open(new_file_name)

img.show()


if __name__ == "__main__":
    ...
