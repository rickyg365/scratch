import os

from PIL import Image


class Screenshot:
    def __init__(self, input_path, file_name="no_name", output_folder="output"):
        self.path = input_path
        self.directory = f"{output_folder}/split_image_{file_name}"
        self.check_dir()

    def check_dir(self):
        if os.path.isdir(self.directory):
            return True
        else:
            os.mkdir(self.directory)

    def get_network_img(self):
        img = Image.open(self.path)

        # Variables
        left = 240
        top = 880
        right = 490
        bot = 940

        img_res = img.crop((left, top, right, bot))

        img_res.save(f"{self.directory}/service_provider.png")
        # img_res.show()

    def get_ping_img(self):
        img = Image.open(self.path)

        # Variables
        left = 1095
        top = 435
        right = 1380
        bot = 600

        img_res = img.crop((left, top, right, bot))

        # img_res.show()
        img_res.save(f"{self.directory}/ping.png")

    def get_down_img(self):
        img = Image.open(self.path)

        # Variables
        left = 1520
        top = 435
        right = 1900
        bot = 600

        img_res = img.crop((left, top, right, bot))

        # img_res.show()
        img_res.save(f"{self.directory}/down.png")

    def get_up_img(self):
        img = Image.open(self.path)

        # Variables
        left = 2050
        top = 435
        right = 2400
        bot = 600

        img_res = img.crop((left, top, right, bot))

        # img_res.show()
        # img_res.save('split_image/up.png')
        img_res.save(f"{self.directory}/up.png")


def loadbar(func):
    def inner(*args, **kwargs):
        print("-- start --")
        func(*args, **kwargs)
        print("-- end --")
    return inner


@loadbar
def parse_folder(folder_name, folder_length):
    for img_number in range(1, folder_length + 1):
        print(f"\rprocessing {img_number*'.'}", end='')
        image_name = f"img{img_number}"
        path_name = f"{folder_name}/{image_name}.png"
        current_parse_image = Screenshot(path_name, file_name=image_name)
        current_parse_image.get_ping_img()
        current_parse_image.get_network_img()
        current_parse_image.get_up_img()
        current_parse_image.get_down_img()
    print(" done")


if __name__ == "__main__":

    input_folder = "sample_folder"
    input_length = 16

    parse_folder(input_folder, input_length)
