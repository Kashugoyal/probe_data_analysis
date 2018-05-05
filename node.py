class Node():
    latitude=0#A
    longitude=0#B

    def __init__(self, data):
        self.latitude=data.split("/")[0]
        self.longitude=data.split("/")[1]

