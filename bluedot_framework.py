from bluedot import BlueDot

class BlueDotFramework:

    def __init__(self):
        self.bd = BlueDot()
        self.start_state()
        self.playing = False

    def start_state(self):
        self.bd.wait_for_press()
        self.playing = True
