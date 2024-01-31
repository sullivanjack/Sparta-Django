from django import template
from ..models import Choice, Question, Round, Player

register = template.Library()

@register.inclusion_tag("polls/reuse/sidebar.html")
def show_sidebar():
    all_rounds = Round.objects.all()
    all_years = []
    for round in all_rounds:
        if round.year not in all_years:
            all_years.append(round.year)

    return {"all_years" : all_years}



# Helper class for passing data to scoreboard.html
class Player_Score:
    def __init__(self, playerName, scores, front9Score, back9Score, totalScore, handicap=-1):
        self.playerName = playerName
        self.scores = scores
        self.front9Score = front9Score
        self.back9Score = back9Score
        self.totalScore = totalScore
        self.handicap = handicap

@register.inclusion_tag("polls/reuse/scoreboard.html")
def show_scoreboard(*args, **kwargs):
    print(kwargs.keys())
    year = kwargs['current_year']
    round = kwargs['current_round']
    use_gross_scores = False
    if "add_handicap" in kwargs.keys():
        use_gross_scores = True

    #all_scores_for_year_and_round = Round.objects.all().filter(year=year).filter(round=round)
    
    #player_score_list = []
    ## Make player classes for displaying    
    #    # Net Scores
    #for round in all_scores_for_year_and_round:
    #    if not use_gross_scores:
    #        # Net Scores 
    #        player_score_list.append(Player_Score(round.player.name, round.get_net_scores, 
    #                                                round.get_front9_score, round.get_back9_score,
    #                                                round.get_total_score))
    #    else:
    #        # Gross Scores
    #        player_score_list.append(Player_Score(round.player.name, round.get_gross_scores,
    #                                              round.get_front9_score, round.get_back9_score,
    #                                              round.get_total_score, round.))



    all_scores_for_year_and_round = Round.objects.all().filter(year=year).filter(round=round)
    
    ## if the "add_handicap" field is present, assume gross scores.
    #if "add_handicap" in kwargs.keys():
    #    print("adding handicap field")
    #    net_scores_list = []
    #    for round in all_scores_for_year_and_round:
    #        net_scores_list.append(round.get_net_scores)
    #    all_scores_for_year_and_round = net_scores_list

    #print(all_scores_for_year_and_round)

    for k in all_scores_for_year_and_round:
        print(f"{k.player.name} score1: {k.get_net_hole1_score}")

    return {"year" : year, 
            "round" : round,
            "use_gross_scores" : use_gross_scores, 
            "all_player_rounds" : all_scores_for_year_and_round,
            }

    #year = kwargs["year"]
    #round = kwargs["round"]
    #all_player_rounds = kwargs["all_player_rounds"]

    #return kwargs 

@register.inclusion_tag("polls/reuse/navbar.html")
def show_navbar():
    testing = "Hello World"
    return {"test" : testing}

@register.inclusion_tag("polls/reuse/jscript_includes.html")
def javascript_includes():
    testing = "Hello World"
    return {"test" : testing}

@register.inclusion_tag("polls/reuse/footer.html")
def show_footer():
    testing = "Hello World"
    return {"test" : testing}
    
    
#all_rounds = Round.objects.all()
#years = []
#for round in all_rounds:
#    if round.year not in years:
#        years.append(round.year)
#return {"all_years" : years}