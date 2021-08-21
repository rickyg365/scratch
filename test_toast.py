import time

from win10toast import ToastNotifier


# Classes
class WinNotif:
    """
    Implement icon_path later
    """
    def __init__(self, toast_icon_path=None):
        self.flags = {
            'start': False,
            'done': False
        }

        self.data = {
            'start': ['Start', 'start message'],
            'done': ['Done', 'done message']
        }

        self.available_flags = ['start', 'done']

        self.duration = 7
        self.toast = ToastNotifier()

    def __str__(self):

        text = f"{', '.join(self.available_flags)}"
        return text

    def set_flag(self, flag_name, flag_title=None, flag_msg=None, flag_status=False):
        if flag_title is None:
            flag_title = f"{flag_name}_title"
        if flag_msg is None:
            flag_msg = f"{flag_name} message"

        try:
            self.flags[flag_name] = flag_status
            self.data[flag_name] = [flag_title, flag_msg]
            self.available_flags.append(flag_name)
            return True

        except Exception as error:
            print(error[:9])
            return False

    def edit_flag(self, flag_name, flag_title, flag_msg):
        self.data[flag_name] = [flag_title, flag_msg]

    def check_flag(self, flag_name):
        status = self.flags.get(flag_name)

        if status is None:
            print("flag did not exist")
            return None

        return status

    def check_all(self):
        triggered = []
        for flag in self.available_flags:
            if self.flags.get(flag):
                triggered.append(flag)
        return triggered

    def flip_flag(self, flag_name):
        """
        Switches current flag status and returns the updated status
        """
        current_status = self.check_flag(flag_name)

        if current_status:
            self.flags[flag_name] = False
            return False
        elif current_status is None:
            print("flag does not exist")
            return None
        self.flags[flag_name] = True
        return True

    def run_toast(self, toast_flag):
        check = self.check_flag(toast_flag)
        if check:
            self.flip_flag(toast_flag)

        toast_title = self.data.get(toast_flag)[0]
        toast_msg = self.data.get(toast_flag)[1]

        self.toast.show_toast(toast_title, toast_msg, duration=self.duration)  # can add icon_path="icon.ico"


if __name__ == "__main__":
    notif_handler = WinNotif()

    notif_handler.set_flag(
        'CTF',
        "Captured the Flag",
        "Congrats! You managed to capture the flag, way to go!"
    )

    for i in range(20):
        try:
            print(f"\n[{i}]")
            # Flag Triggers
            if i == 0:
                notif_handler.flip_flag('start')

            elif i % 5 == 0:
                notif_handler.flip_flag('CTF')

            elif i == 19:
                notif_handler.flip_flag('done')

            # Check Flags
            print("Available Flags: ", notif_handler)

            status = notif_handler.check_all()
            print("Triggered Flags: ", ', '.join(status))

            for item in status:
                notif_handler.run_toast(item)

            time.sleep(.25)

        except KeyboardInterrupt:
            print("\n[Program Stopped]")
            break



