from dataclasses import dataclass, field
from typing import ClassVar
from abc import ABCMeta, abstractmethod
import os 
import csv

@dataclass
class Score():
    name: str # = field(init=False)
    score: int # = field(init=False)

    # def __post_init__(self):
    #     self.name = player_name 
    #     self.score = round

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
    
    def display_score(self):
        if os.path.exists('./data/scores.csv') == False :
            print("==================================")
            print('Sorry no scores available for now.')
            print("==================================")

        else :
            print("==================================")
            # Display scores
            with open('./data/scores.csv') as score_csv:
                reader = csv.reader(score_csv, delimiter=',') #reader mode
                for ligne in reader: # read each line
                    if len(ligne) != 0 :
                        print(ligne[0], ' ', ligne[1])
            print("==================================")

# test
score = Score('Player', 45)
score.display_score()
score.save_score()
score.display_score()
