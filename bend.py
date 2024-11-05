#bend.py (backend)

import json
import os

DATA_FILE = 'road_data.json'

class Road:
    def __init__(self, name, difficult, location, length, description, photos=None):
        self.name = name
        self.difficult = difficult
        self.location = location
        self.length = length
        self.description = description
        self.photos = photos if photos is not None else []

    def to_dict(self):
        return {
            'Name: ': self.name,
            'Difficulty: ': self.difficult,
            'Location: ': self.location,
            'Length: ': self.length,      
            'Description: ': self.description,
            'Photos: ': self.photos      
        }
    
    def from_dict(road):
        return Road(
            name = road['name'],
            location = road['location'],
            difficulty = road['difficult'],
            length = road['length'],
            photos = road.get('photos', [])
        )
    
    
def load_roads():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as json_file:
            try:
                roads = json.load(json_file)
            except json.JSONDecodeError:
                roads = []
    else:
        roads = []

    return roads


