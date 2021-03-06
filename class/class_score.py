from dataclasses import dataclass, field
from typing import ClassVar
from abc import ABCMeta, abstractmethod
import os 
import csv

@dataclass
class Score:
    name: str = field(init=False)
    score : int = field(init=False)

    def __post_init__(self):
        self.name = player_name 
        self.score = round

    def save_score(self):
        if os.path.exists('./data/scores.csv') == False : # check whether scores.csv exists, if not create it 
            header = ["Name", "Score"]
            with open('./data/scores.csv', 'w') as score_csv: # create scores.csv
                writer = csv.writer(score_csv, delimiter=',')
                writer.writerow(header) # write the header


        # Update scores.csv
        with open('./data/scores.csv', 'a', newline='') as score_csv: # add a new line in csv file
            writer = csv.writer(score_csv, delimiter=',')
            score_line = [self.name, self.score]
            writer.writerow(score_line) # add a line with current name and score

# tests
player_name = 'plop'
round = 5
score = Score()
print(f"Le joueur {score.name} a {score.score} points")
score.save_score()
