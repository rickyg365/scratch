import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
# driver.get("https://www.google.com")
#
# print(driver.title)
# print(driver.current_url)
#
#
# time.sleep(5)
# driver.quit()


class BuildBot:
    def __init__(self, champ_name, game_mode, role=None):
        """
        Reference URLS:
            https://www.metasrc.com/aram/na/champion/rengar
            https://www.metasrc.com/5v5/na/champion/rengar/jungle
            https://www.metasrc.com/5v5/na/champion/rengar/top
        """
        # chromedriver = r"C:\webdrivers\chromedriver.exe"
        # os.environ["webdriver.chrome.driver"] = chromedriver

        # load_options = Options()
        # load_options.page_load_strategy = 'eager'

        options = webdriver.ChromeOptions()
        # options.add_argument("log-level=2")
        options.add_argument('--ignore-certificate-errors-spki-list')
        options.add_argument('--ignore-ssl-errors')
        options.add_argument("--no-sandbox")  # This make Chromium reachable
        options.add_argument("--no-default-browser-check")  # Overrides default choices
        options.add_argument("--no-first-run")
        options.add_argument("--disable-default-apps")
        options.add_experimental_option("excludeSwitches", ["enable-logging"])

        service = Service(r"C:\webdrivers\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service, options=options)
        self.base_url = f"https://www.metasrc.com/{game_mode}/na/champion/{champ_name}/{''if role is None else role}"

    def __str__(self):
        text = ""
        return text

    def build_url(self, champ_name, game_mode, role=None):
        """
            Reference URLS:
                https://www.metasrc.com/aram/na/champion/rengar
                https://www.metasrc.com/5v5/na/champion/rengar/jungle
                https://www.metasrc.com/5v5/na/champion/rengar/top
        """
        pass

    def connect(self, new_url=None):
        """ connect to given url """
        if new_url is None:
            new_url = new_build_bot.base_url
        self.driver.get(new_url)

    def resize_window(self, x=None, y=None):
        if x is None or y is None:
            self.driver.maximize_window()
            return

        self.driver.set_window_size(x, y)

    def accept_cookie(self):
        pass

    def run(self):
        start_time = time.perf_counter()
        print(f"[ Starting ]\n")
        self.resize_window()
        time.sleep(.15)
        print(f"[ Resize ]: {time.perf_counter() - start_time:02.3f} sec")

        self.connect()
        time.sleep(.5)
        print(f"[ Connect ]: {time.perf_counter() - start_time:02.3f} s")
        input("[ Running ]")
        try:
            self.driver.quit()
        except Exception as e:
            print("Already closed, I wonder why?")
        print(f"[ Driver Stopped ]: {time.perf_counter() - start_time:02.3f} sec")

    def exit(self):
        self.driver.quit()


if __name__ == "__main__":
    # args: 1|filename 2|champ_name 3|game_mode 4|role
    # file_name = sys.argv[0]
    # champ_name = sys.argv[1]
    # game_mode = sys.argv[2]
    # role = sys.argv[3]

    num_inputs = len(sys.argv)
    used_arguments = {}
    possible_args = [
        "file_name",
        "champ_name",
        "game_mode",
        "role"
    ]

    for i in range(num_inputs):
        used_arguments[possible_args[i]] = sys.argv[i]

    if num_inputs < 3:
        used_arguments["game_mode"] = "aram"

    if num_inputs < 2:
        used_arguments["champ_name"] = "ashe"

    new_build_bot = BuildBot(used_arguments["champ_name"], used_arguments["game_mode"], used_arguments.get("role", None))
    initial_time = time.perf_counter()
    try:
        new_build_bot.run()
    except Exception as e:
        print("error")
        try:
            new_build_bot.exit()
        except Exception as e:
            print("already quit")
    finally:
        print(f"[ QUIT ] {time.perf_counter() - initial_time:02.3f} sec")
