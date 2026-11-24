import pandas as pd
from abc import ABC #abstract base class i think
import re


class GameEngine:
    def __init__(self, rooms, suspects):
        self.suspects = suspects
        self.rooms = rooms
        self.inventory = []
        self.rooms_visted = []
        self.round_number = 1
        self.max_rounds = 3
    def get_evidence():
        pass
    def round_number():
        pass
    def max_rounds():
        pass
    def calculate_evidence(self):
        for item in self.inventory:
            pass
        # we will need an attribute in each object that links to a suspect
            # will also need an attribute of what specific piece of evidence an item contradicts with
            # whoever creates the evidence, we should first list all evidence we are going to have in the game
            # then, we should have some evidence that opposes other evidence
            # if contradictory_evidence = None, continue, elif contradictory evidence = __, _
    def calculate_contradictory_ev(): # not sure if this will be used or changed
        pass
    def calculate_prime_suspect():
            pass
        
suspects = ["fatimah", "nenuki", "etc"] # either goes before or after all classes. i think after, but i can double check 
rooms = ["kitchen", "closet", "attic", "etc"] # same as above
        
        
class Evidence:
    pass
class Rooms:
    pass
        
class Suspect:
    pass