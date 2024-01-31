from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.IndexView.as_view(), name="index"),
    # ex: /polls/round/2022/2
    path("round/<int:year>/<int:round>", views.RoundView.as_view(), name="Scores"),
    # ex: /polls/player/name
    path("players/<str:player_name>", views.PlayerView.as_view(), name="Player"),
    # ex: /polls/import
    path("import/", views.ImportView.as_view(), name="Import")
    #path("scores/<int:pk>/", views.DetailView.as_view(), name="detail"),
]
