import rumps


class StandUpPleaseApp:
    def __init__(self):
        self.app = rumps.App("Stand-Up-Please")
        self.timer = rumps.Timer(self.ticker, 1)
        self.interval = 60 * 60
        self.bau_menu()
        self.start = rumps.MenuItem(title="Start Working!", callback=self.start_timer)
        self.stop = rumps.MenuItem(title="Stop!")
        self.app.menu = [self.stop, self.start]
        self.stand_up = "Stand Up, Please!"
        self.sit_down = "Sit Down, Please!"
        self.status = self.stand_up

    def bau_menu(self):
        self.timer.count = 0
        self.app.title = "⏳"

    def ticker(self, counter):
        time_left = counter.end - counter.count
        mins = time_left // 60 if time_left >= 0 else time_left // 60 + 1
        secs = time_left % 60 if time_left >= 0 else (-1 * time_left) % 60
        self.status = self.sit_down if self.status == self.stand_up else self.stand_up
        if mins == 0 and time_left < 0:
            self.app.title = "⌛"
            rumps.notification(title="Stand-Up-App", subtitle=self.status, message="")
            self.timer.count = 0
            time.sleep(10)
            rumps.notification(title="Stand-Up-App", subtitle="You can continue working now!", message="")
            self.app.title = "⏳"
            ticker()
        else:
            self.start.set_callback(None)
            self.stop.title = '{:2d}:{:02d}'.format(mins, secs)
        counter.count += 1

    def start_timer(self, counter):
        self.timer.count = 0
        self.timer.end = self.interval
        self.timer.start()

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = StandUpPleaseApp()
    app.run()
