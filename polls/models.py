from django.db import models
from django.utils import timezone

import datetime
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date Published")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self):
        return self.choice_text

class Course(models.Model):
    name = models.CharField(max_length=15, default="Test")
    hole1_handicap = models.IntegerField(default=0)
    hole2_handicap = models.IntegerField(default=0)
    hole3_handicap = models.IntegerField(default=0)
    hole4_handicap = models.IntegerField(default=0)
    hole5_handicap = models.IntegerField(default=0)
    hole6_handicap = models.IntegerField(default=0)
    hole7_handicap = models.IntegerField(default=0)
    hole8_handicap = models.IntegerField(default=0)
    hole9_handicap = models.IntegerField(default=0)
    hole10_handicap = models.IntegerField(default=0)
    hole11_handicap = models.IntegerField(default=0)
    hole12_handicap = models.IntegerField(default=0)
    hole13_handicap = models.IntegerField(default=0)
    hole14_handicap = models.IntegerField(default=0)
    hole15_handicap = models.IntegerField(default=0)
    hole16_handicap = models.IntegerField(default=0)
    hole17_handicap = models.IntegerField(default=0)
    hole18_handicap = models.IntegerField(default=0)
    hole1_par = models.IntegerField(default=0)
    hole2_par = models.IntegerField(default=0)
    hole3_par = models.IntegerField(default=0)
    hole4_par = models.IntegerField(default=0)
    hole5_par = models.IntegerField(default=0)
    hole6_par = models.IntegerField(default=0)
    hole7_par = models.IntegerField(default=0)
    hole8_par = models.IntegerField(default=0)
    hole9_par = models.IntegerField(default=0)
    hole10_par = models.IntegerField(default=0)
    hole11_par = models.IntegerField(default=0)
    hole12_par = models.IntegerField(default=0)
    hole13_par = models.IntegerField(default=0)
    hole14_par = models.IntegerField(default=0)
    hole15_par = models.IntegerField(default=0)
    hole16_par = models.IntegerField(default=0)
    hole17_par = models.IntegerField(default=0)
    hole18_par = models.IntegerField(default=0)
    blah = models.IntegerField(default=0)


    def __str__(self):
        return str(self.name)
    
    @property
    def get_sorted_list(self):
        return [(1, self.hole1_handicap), (2, self.hole2_handicap), (3, self.hole3_handicap),
                (4, self.hole4_handicap), (5, self.hole5_handicap), (6, self.hole6_handicap),
                (7, self.hole7_handicap), (8, self.hole8_handicap), (9, self.hole9_handicap),
                (10, self.hole10_handicap), (11, self.hole11_handicap), (12, self.hole12_handicap),
                (13, self.hole13_handicap), (14, self.hole14_handicap), (15, self.hole15_handicap),
                (16, self.hole16_handicap), (17, self.hole17_handicap), (18, self.hole18_handicap)]

class Player(models.Model):
    name = models.CharField(max_length=25)
    # This represents a players inital handicap. This field does not need to be updated, as it will be calculated whenever it is needed. 
    inital_handicap = models.IntegerField(default=0) 

    @property
    def get_handicap(self):
        player_rounds = Round.objects.all().filter(player=self)
        total_score = 0
        rounds = 0
        for round in player_rounds:
            rounds+=1
            total_score += round.get_total_gross_score
        return int(total_score/rounds)


    def __str__(self):
        return f"{self.name}"

class Round(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    # The Course Object to use for handicap calculations
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    #  Ex: year 2023, round 1 
    year = models.IntegerField(default=0)
    round = models.IntegerField(default=0)
    # Holes
    hole1 = models.IntegerField(default=0)
    hole2 = models.IntegerField(default=0)
    hole3 = models.IntegerField(default=0)
    hole4 = models.IntegerField(default=0)
    hole5 = models.IntegerField(default=0)
    hole6 = models.IntegerField(default=0)
    hole7 = models.IntegerField(default=0)
    hole8 = models.IntegerField(default=0)
    hole9 = models.IntegerField(default=0)
    hole10 = models.IntegerField(default=0)
    hole11 = models.IntegerField(default=0)
    hole12 = models.IntegerField(default=0)
    hole13 = models.IntegerField(default=0)
    hole14 = models.IntegerField(default=0)
    hole15 = models.IntegerField(default=0)
    hole16 = models.IntegerField(default=0)
    hole17 = models.IntegerField(default=0)
    hole18 = models.IntegerField(default=0)

    # Helper properties for common values we will need with Score data.
    @property
    def get_front9_gross_score(self):
        return self.hole1 + self.hole2 + self.hole3 + self.hole4 + self.hole5 + self.hole6 + self.hole7 + self.hole8 + self.hole9
    
    @property
    def get_back9_gross_score(self):
        return self.hole10 + self.hole11 + self.hole12 + self.hole13 + self.hole14 + self.hole15 + self.hole16 + self.hole17 + self.hole18
    
    @property
    def get_total_gross_score(self):
        return self.get_front9_gross_score + self.get_back9_gross_score
    
    @property
    def get_front9_net_score(self):
        net_scores = self.get_net_scores
        total_score = 0
        for i in range(0,8):
            total_score += net_scores[i]
        return total_score
    
    @property
    def get_back9_net_score(self):
        net_scores = self.get_net_scores
        total_score = 0
        for i in range(9,17):
            total_score += net_scores[i]
        return total_score
    
    @property
    def get_total_net_score(self):
        return self.get_front9_net_score + self.get_back9_net_score
    
    @property
    def get_handicap_score_matrix(self):
        return [(self.course.hole1_handicap, self.hole1, 1), (self.course.hole2_handicap, self.hole2, 2),
            (self.course.hole3_handicap, self.hole3, 3), (self.course.hole4_handicap, self.hole4, 4),
            (self.course.hole5_handicap, self.hole5, 5), (self.course.hole6_handicap, self.hole6, 6),
            (self.course.hole7_handicap, self.hole7, 7), (self.course.hole8_handicap, self.hole8, 8),
            (self.course.hole9_handicap, self.hole9, 9), (self.course.hole10_handicap, self.hole10, 10),
            (self.course.hole11_handicap, self.hole11, 11), (self.course.hole12_handicap, self.hole12, 12),
            (self.course.hole13_handicap, self.hole13, 13), (self.course.hole14_handicap, self.hole14, 14),
            (self.course.hole15_handicap, self.hole15, 15), (self.course.hole16_handicap, self.hole16, 16),
            (self.course.hole17_handicap, self.hole17, 17), (self.course.hole18_handicap, self.hole18, 18)]
         
    @property
    def get_net_scores(self):
        handicap = self.get_handicap
        handicap_scores = self.get_handicap_score_matrix

        # Sort matrix by the handicap, so we can loop and apply subtractions in order 
        handicap_scores = sorted(handicap_scores, key=lambda tuple: tuple[0])

        #print("-------------------------------")
        #print(f" name: {self.player} handi {handicap}")
        #print(handicap_scores)        
        while handicap > 0:
            for i in range(0, len(handicap_scores)):
                if (handicap_scores[i][1] - 1) < 0:
                    # If we are going to get a negative score, just go to the next hole.
                    continue
                handicap_scores[i] = (handicap_scores[i][0], handicap_scores[i][1]-1, handicap_scores[i][2])
                handicap -= 1

        #print(handicap_scores)
        # Scores in order from 1 to 18

        in_order_net_scores = sorted(handicap_scores, key=lambda tuple: tuple[2])
        for i in range(0, len(in_order_net_scores)):
            # Second column of tuple is actual score, that's all we want here.
            in_order_net_scores[i] = in_order_net_scores[i][1]
        #print(in_order_net_scores)
        #print("-------------------------------")

        return in_order_net_scores

    @property
    def get_gross_scores(self):
        return [self.hole1, self.hole2,  self.hole3,
                self.hole4, self.hole5,  self.hole6,
                self.hole7, self.hole8,  self.hole9,
                self.hole10, self.hole11, self.hole12,
                self.hole13, self.hole14, self.hole15,
                self.hole16, self.hole17, self.hole18]

    @property
    def get_handicap(self):
        '''
            Get the Player's Handicap by using score data from the rounds before this one
        '''
        player_rounds = Round.objects.all().filter(player=self.player)
        total_score_over_par = 0
        rounds = 0
        for round in player_rounds:
            if (round.year < self.year) or (round.year == self.year and round.round < self.round ):
                print(f"Player {self.player} Using Year {round.year} Day {round.round}")
                rounds+=1
                total_score_over_par += (round.get_total_gross_score - 72)
        
        if rounds == 0 or total_score_over_par == 0:
            print("No handicap found, using inital handicap")
            return self.player.inital_handicap
        else:
            print(f"Player {self.player} Total Score {total_score_over_par} Rounds {rounds}")
            return int((total_score_over_par/rounds) * .875)

    @property
    def get_net_hole1_score(self):
        return self.get_net_scores[0] 
    @property
    def get_net_hole2_score(self):
        return self.get_net_scores[1]
    @property
    def get_net_hole3_score(self):
        return self.get_net_scores[2]
    @property
    def get_net_hole4_score(self):
        return self.get_net_scores[3]
    @property
    def get_net_hole5_score(self):
        return self.get_net_scores[4]
    @property
    def get_net_hole6_score(self):
        return self.get_net_scores[5]
    @property
    def get_net_hole7_score(self):
        return self.get_net_scores[6]
    @property
    def get_net_hole8_score(self):
        return self.get_net_scores[7]
    @property
    def get_net_hole9_score(self):
        return self.get_net_scores[8]
    
    @property
    def get_net_hole10_score(self):
        return self.get_net_scores[9] 
    @property
    def get_net_hole11_score(self):
        return self.get_net_scores[10]
    @property
    def get_net_hole12_score(self):
        return self.get_net_scores[11]
    @property
    def get_net_hole13_score(self):
        return self.get_net_scores[12]
    @property
    def get_net_hole14_score(self):
        return self.get_net_scores[13]
    @property
    def get_net_hole15_score(self):
        return self.get_net_scores[14]
    @property
    def get_net_hole16_score(self):
        return self.get_net_scores[15]
    @property
    def get_net_hole17_score(self):
        return self.get_net_scores[16]
    @property
    def get_net_hole18_score(self):
        return self.get_net_scores[17]

    def __str__(self):
        return f"{self.player} Year:{self.year} Round:{self.round}"
