import pandas as pd
import abc


class Evidence:
    pass
class GameEngine:
    def __init__(self, rooms, suspects):
        self.suspects = suspects
        self.rooms = rooms
        self.inventory = []
        self.rooms_visted = []
        self.round_number = 1
        self.max_rounds = 3
class Suspect:
    pass

suspects = ["fatimah", "nenuki", "etc"]
rooms = ["kitchen", "closet", "attic", "etc"]