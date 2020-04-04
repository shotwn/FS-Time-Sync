class FlipFlop:
    def __init__(self, to_flop, default=" "):
        self.to_flop = to_flop
        self.default = default
        self.flop = True

    def __str__(self):
        return self.get()

    def get(self):
        to_return = self.default
        if self.flop:
            to_return = self.to_flop

        self.flop = not self.flop

        return to_return
