

class Ticks:
    def __init__(self):
        pass

    def decodeData(self,data):
        string_data = data.decode('utf-8','ignore')
        stripped_data = string_data.strip()
        return stripped_data.split(",")


    def get_ticks(self,data):
        stripped_ticks = self.decodeData(data)
        if len(stripped_ticks)==4 and stripped_ticks:
                ticks = list(map(int, stripped_ticks))
                scaled_ticks = [element / 100 for element in ticks]
                return scaled_ticks