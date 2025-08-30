

class ScoreCard:


    def __init__(self, pins):
        self.pins = pins

    def get_pins(self):
        return self.pins

    def get_score(self):
        total = 0
        for i,pin in enumerate(self.pins):
            if pin == "-":
                continue
            if pin == "/":
                total += 10 - int(self.pins[i-1])
            else:
                total += int(pin)

        return total


    def symbols_to_numbers(self):
        total = ""
        for i,pin in enumerate(self.pins):
            if pin == "-":
                total += "0"

            elif pin == "X":
                total += "10"

            elif pin == "/":
                total += str(10 - int(self.pins[i-1]))
            else:
                total += pin
        return total

    



