from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import generic, View

from .models import Choice, Question, Round, Player, Course
from . import utils, import_scores


class IndexView(generic.ListView):
    def __init__(self):
        super()
        pass    

class RoundView(generic.ListView):
    def __init__(self):
        super() 
        #utils.make_fake_data()

    model = Round
    template_name = "polls/year_scores.html"
    context_object_name = "scores"
    
    def get_context_data(self, **kwargs):
    
        context = super(RoundView, self).get_context_data(**kwargs)
        all_player_rounds = self.get_queryset()

        all_rounds = Round.objects.all()
        all_years = []
        for round in all_rounds:
            if round.year not in all_years:
                all_years.append(round.year)
        
        #print(f"get_context_data {all_player_rounds}")

        context['current_round'] = self.round
        context['current_year'] = self.year
        return context

    def get_data(rounds_objects):
        all_players_in_round = []

    def get_queryset(self):
        self.year = self.kwargs['year']
        self.round = self.kwargs['round']
        return Round.objects.all().filter(year=self.year).filter(round=self.round)


class PlayerView(generic.ListView):
    def __init__(self):
        super() 

    model = Player
    template_name = "polls/player_view.html"
    context_object_name = "players"
    
    def get_context_data(self, **kwargs):    
        context = super(PlayerView, self).get_context_data(**kwargs)
        player = self.get_queryset()[0]
        # Rounds by a player, order by year then round, then show a max of 7
        all_player_rounds = Round.objects.all().filter(player=player).order_by('-year', '-round')[:7]

        #print(f"Player {player}")
        context['player'] = player
        context['all_player_rounds'] = all_player_rounds
        return context

    def get_queryset(self):
        self.player_name = self.kwargs['player_name']
        return Player.objects.all().filter(name=self.player_name)

class CourseView(generic.ListView):
    def __init__(self):
        super() 
    model = Course
    context_object_name = "courses"

def simple_json_response(status, message):
    return JsonResponse({"status_code" : status, "message" : message})

class ImportView(View):
    def get(self, request):
        template_name = "polls/import.html"
        return render(request, template_name)

    def post(self, request):
        user = request.user
        file = request.FILES['scores_upload_file']
        status = 400
        returnmsg = "No return message set."

        #print(f"request by user {user}")
        # bad auth but it works 
        #if request.user.is_authenticated:
        if str(request.user) != "admin":
            status = 401
            returnmsg = f"User is not admin (is {user}), try logging into the admin console to authortize"
        else:
            import_return = import_scores.import_data_from_file(file)
            status = import_return[0]
            returnmsg = import_return[1]

        return simple_json_response(status, returnmsg)

    
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't pick a choice dumbass",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

    return HttpResponse(f"You are voting on question {question_id}")
