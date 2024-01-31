
from .models import Choice, Question, Round, Player

COURSE_PAR = 72

def calculate_handicap(player):
    '''
        A function for calculating a players handicap. 
    '''
    player_rounds = Round.objects.all().filter(player=player)
    for round in player_rounds:
        score = round.get_total_score
        



def make_fake_data():
    for p in Player.objects.all():
        p.delete()
    for r in Round.objects.all():
        r.delete()

    jack_player = Player.objects.create(name="Jack")
    sam_player = Player.objects.create(name="Sam")

    jack_2022_round1 = Round.objects.create(player=jack_player, year=2022, round=1,
                                            hole1=5, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=4, hole14=6, hole15=5, hole16=2, hole17=4, hole18=6)
    jack_2022_round2 = Round.objects.create(player=jack_player, year=2022, round=2,
                                            hole1=5, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=4, hole14=6, hole15=5, hole16=2, hole17=4, hole18=6)
    jack_2022_round3 = Round.objects.create(player=jack_player, year=2022, round=3,
                                            hole1=5, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=4, hole14=6, hole15=5, hole16=2, hole17=4, hole18=6)

    jack_2023_round1 = Round.objects.create(player=jack_player, year=2023, round=1,
                                            hole1=5, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=4, hole14=6, hole15=5, hole16=2, hole17=4, hole18=6)
    jack_2023_round2 = Round.objects.create(player=jack_player, year=2023, round=2,
                                            hole1=5, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=4, hole14=6, hole15=5, hole16=2, hole17=4, hole18=6)
    jack_2023_round3 = Round.objects.create(player=jack_player, year=2023, round=3,
                                            hole1=5, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=4, hole14=6, hole15=5, hole16=2, hole17=4, hole18=6)

        

    sam_2022_round1 = Round.objects.create(player=sam_player, year=2022, round=1,
                                            hole1=8, hole2=3, hole3=5, hole4=6, hole5=2, hole6=2, hole7=1, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=5, hole13=4, hole14=6, hole15=3, hole16=2, hole17=4, hole18=6)
    sam_2022_round2 = Round.objects.create(player=sam_player, year=2022, round=2,
                                            hole1=5, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=8, hole14=6, hole15=9, hole16=2, hole17=4, hole18=6)
    sam_2022_round3 = Round.objects.create(player=sam_player, year=2022, round=3,
                                            hole1=5, hole2=6, hole3=4, hole4=6, hole5=5, hole6=2, hole7=6, hole8=6, hole9=5,
                                            hole10=5, hole11=4, hole12=2, hole13=4, hole14=6, hole15=5, hole16=2, hole17=4, hole18=6)

    sam_2023_round1 = Round.objects.create(player=sam_player, year=2023, round=1,
                                            hole1=7, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=7, hole11=5, hole12=7, hole13=4, hole14=6, hole15=5, hole16=8, hole17=4, hole18=6)
    sam_2023_round2 = Round.objects.create(player=sam_player, year=2023, round=2,
                                            hole1=5, hole2=2, hole3=10, hole4=6, hole5=3, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=5, hole11=5, hole12=2, hole13=4, hole14=6, hole15=5, hole16=8, hole17=4, hole18=6)
    sam_2023_round3 = Round.objects.create(player=sam_player, year=2023, round=3,
                                            hole1=9, hole2=2, hole3=4, hole4=6, hole5=5, hole6=2, hole7=4, hole8=6, hole9=5,
                                            hole10=9, hole11=5, hole12=2, hole13=4, hole14=7, hole15=5, hole16=2, hole17=14, hole18=6)