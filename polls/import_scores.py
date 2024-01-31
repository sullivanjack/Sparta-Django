"""

Utility for importing scores from a CSV.

Format is:
<Course Name>, <Year>, <Round Number>
<Player Name>, Hole 1 Score, Hole 2 Score, Hole 3 Score, etc.., Hole 18 Score
<Player Name 2>, Hole 1 Score, Hole 2 Score, Hole 3 Score, etc.., Hole 18 Score

<Course Name> will need to match an already exisiting Course in the database. A new one will not be created.
<Player Name> will need to match a player in the database, A new one will not be created.
<Year> The year of the round. (ex: 2023)
<Round Number> What round number in the year this is (valid: 1,2,3)

"""

import argparse
import csv
import io
import tempfile

from .models import Course, Player, Round
from django.core.exceptions import ObjectDoesNotExist

status = None
return_msg = None

class import_player():
    def __init__(self, name, scores_list):
        self.name = name
        self.scores_list = scores_list

    def __str__(self):
        print(f"Player {self.name}, has scores {self.scores}")



def import_data(course, year, round, player_scores):
    global return_msg
    global status

    try:
        course_model = Course.objects.all().filter(name=course)[0:1].get()
    except ObjectDoesNotExist:
        return_msg = f"Could not find course with name {course} in database! Make sure it is created."
        status = 400
        return

    if course_model != None:
        print(course_model) 
        for player in player_scores:
            player_model = None
            try:
                player_model = Player.objects.all().filter(name=player.name)[0:1].get()
            except ObjectDoesNotExist:
                status = 400
                return_msg = f"Could not find player {player.name} in database! Make sure they have been created"
                return
        
            if player_model != None:
                round_model = None
                try:
                    round_model = Round.objects.all().filter(player=player_model).filter(year=year).filter(round=round)[0:1].get()
                except ObjectDoesNotExist:
                    # This is good for import!
                    pass
                if round_model is not None:
                    status = 400
                    return_msg = f"Already found a round for player {player.name} Year: {round_model.year} Round {round_model.round}"
                    return

    # If we make here, data is good for import
    for player in player_scores:
        player_model = Player.objects.all().filter(name=player.name)[0:1].get()
        val = Round.objects.create(player=player_model, course=course_model, year=year, round=round,
                                hole1=player.scores_list[0], hole2=player.scores_list[1], hole3=player.scores_list[2],
                                hole4=player.scores_list[3], hole5=player.scores_list[4], hole6=player.scores_list[5],
                                hole7=player.scores_list[6], hole8=player.scores_list[7], hole9=player.scores_list[8],
                                hole10=player.scores_list[9], hole11=player.scores_list[10], hole12=player.scores_list[11],
                                hole13=player.scores_list[12], hole14=player.scores_list[13], hole15=player.scores_list[14],
                                hole16=player.scores_list[15], hole17=player.scores_list[16], hole18=player.scores_list[17])
        return_msg = return_msg + f", Created {val}"
        
                                
def import_data_from_file(file):
    global return_msg, status
    return_msg = "Success! "
    status = 200

    players = []
    course_name = ""
    year = ""
    round = ""

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file.read())
        temp_file.close()

    #TODO better input verification
    with open(temp_file.name, 'r') as file:
        line_count = 0
        for line in file:
            line = line.rstrip().split(",")
            if line_count == 0:
                course_name = line[0]
                year = line[1]
                round = line[2]
                #print(f"Course Name {course_name}, Year {year}, Round {round}")
            else:
                player = line[0]
                scores = line[1:19]          
                players.append(import_player(player, scores))
                #print(f"Player {player}, {scores}")

            line_count+=1
        file.close()

    # Import Data
    import_data(course_name, year, round, players)

    return (status, return_msg)
    
    