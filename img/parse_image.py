import os

from PIL import Image


# def get_network_img(input_file_path):
#     img = Image.open(input_file_path)
#
#     # Variables
#     left = 240
#     top = 880
#     right = 490
#     bot = 940
#
#     img_res = img.crop((left, top, right, bot))
#
#     # img_res.show()
#     img_res.save('split_image/network_name.png')
#
#
# def get_ping_img(input_file_path):
#     img = Image.open(input_file_path)
#
#     # Variables
#     left = 1095
#     top = 435
#     right = 1380
#     bot = 600
#
#     img_res = img.crop((left, top, right, bot))
#
#     # img_res.show()
#     img_res.save('split_image/ping.png')
#
#
# def get_down_img(input_file_path):
#     img = Image.open(input_file_path)
#
#     # Variables
#     left = 1520
#     top = 435
#     right = 1900
#     bot = 600
#
#     img_res = img.crop((left, top, right, bot))
#
#     # img_res.show()
#     img_res.save('split_image/down.png')
#
#
# def get_up_img(input_file_path):
#     img = Image.open(input_file_path)
#
#     # Variables
#     left = 2050
#     top = 435
#     right = 2400
#     bot = 600
#
#     img_res = img.crop((left, top, right, bot))
#
#     # img_res.show()
#     # img_res.save('split_image/up.png')
#     img_res.save('test.png')


class Screenshot:
    def __init__(self, input_path, file_name="no_name"):
        self.path = input_path
        self.directory = f"random_output/split_image_{file_name}"
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

        img_res.save(f"{self.directory}/network_name.png")
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


if __name__ == "__main__":
    # folder_name = "sample_folder"
    # image_name = "img1"
    # file_path = f"{folder_name}//{image_name}.png"

    folder_name = "sample_folder"

    # Range is 1-16 inclusive
    for i in range(1, 17):
        print(f"\rprocessing {i*'.'}", end='')
        image_name = f"img{i}"
        file_path = f"{folder_name}/{image_name}.png"
        current_parse_image = Screenshot(file_path, file_name=image_name)
        current_parse_image.get_ping_img()
        current_parse_image.get_network_img()
        current_parse_image.get_up_img()
        current_parse_image.get_down_img()

    print(" done")
