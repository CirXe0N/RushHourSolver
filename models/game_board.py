
class GameBoard(object):

    def __init__(self, height, width):
        self.vehicles = []
        self.height = height
        self.width = width

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles.remove(vehicle)

    def get_vehicles(self):
        return self.vehicles

    def set_height(self, height):
        self.height = height

    def get_height(self):
        return self.height

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width
