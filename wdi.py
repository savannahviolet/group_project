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
    def round_number(self):
        return self.round_number
    def round_loops(self):
        if self.round_number < self.max_rounds:
            self.round_number += 1
        else:
            pass 
            # would be where lost action/dialogue happens?? 
            # potentially abc decorator 
    def rooms_per_round(self):
        if len(self.rooms_visted) == 3:
            # go to calculation
            pass
        else:
            pass
    def calculate_evidence(self):
        for item in self.inventory:
            pass
        # we will need an attribute in each object that links to a suspect
            # will also need an attribute of what specific piece of evidence an item contradicts with
            # whoever creates the evidence, we should first list all evidence we are going to have in the game
            # then, we should have some evidence that opposes other evidence
            # if contradictory_evidence = None, continue, elif contradictory evidence = __, _
    def calculate_contradictory_ev(self): # not sure if this will be used or changed
        contradictions = []
        for item in self.inventory:
            # inventory items are evidence, which each have attributes
            # if the item's linekd suspect is equal to a suspect and the evidence contradicts a suspect, append to list
            # item needs to have a contradiction attribute, linked suspect, etc
                
        return contradictions
    def calculate_prime_suspect(self):
        # the rank is equal to the reversed order of the amount of evidence against each suspect
            ranked_suspects = sorted(self.suspects, key=self.get_evidence, reverse=True)
            return ranked_suspects[0]
        # format would be something like f"recommended suspect to investigate is {calculate_prime_suspect (or) ranked_suspects[0]}. 
        #                                   The suspect with the most contradictory evidence against them is {calculate_contradictory_ev (or) ranked_contradictions}.
        #                                   Who would you like to investigate? (or if only one option) Would you like to investigate {ranked_suspects[0]}? \n
        
suspects = ["fatimah", "nenuki", "etc"] # either goes before or after all classes. i think after, but i can double check 
rooms = ["kitchen", "closet", "attic", "etc"] # same as above
        
        
class Evidence:
    pass
class Rooms:
    pass
        
class Suspect:
    pass