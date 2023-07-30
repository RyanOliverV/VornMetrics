from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.TeamsList.as_view(), name='teams-api'),
    path('teams/<int:id>/', views.TeamDetail.as_view(), name='team-detail-api'),
    path('players/', views.PlayerList.as_view(), name='players-api'),
    path('playerstats/<int:id>/', views.PlayerDetail.as_view(),
         name='player-detail-api'),
    path('goalkeepers/', views.GoalkeeperList.as_view(), name='goalkeepers-api'),
    path('centrebacks/', views.CentreBackList.as_view(), name='defenders-api'),
    path('fullbacks/', views.FullBackList.as_view(), name='midfielders-api'),
    path('defensivemidfielders/',
         views.DefensiveMidfielderList.as_view(), name='forwards-api'),
    path('attackingmidfielders/',
         views.AttackingMidfielderList.as_view(), name='forwards-api'),
    path('centralmidfielders/',
         views.CentralMidfielderList.as_view(), name='forwards-api'),
    path('centreforwards/', views.CentreForwardList.as_view(), name='forwards-api'),
    path('wingers/', views.WingerList.as_view(), name='forwards-api'),
    path('seasons/', views.SeasonList.as_view(), name='seasons-api'),
    path('standings/', views.LeagueTable.as_view(), name='standings-api'),
    path('live-standings/', views.LiveLeagueTable.as_view(),
         name='live-standings-api'),
    path('standings/<int:season_id>/', views.LeagueTable.as_view(),
         name='standings-api-with-season'),
    path('fixtures/', views.FixtureList.as_view(), name='fixtures-api'),
    path('fixtures/<int:id>/', views.FixtureDetail.as_view()),
    path('fixtures/<int:team1_id>/<int:team2_id>/',
         views.TeamsComparison.as_view()),
    path('latest-fixtures/<int:team1_id>/<int:team2_id>/',
         views.LatestFixtures.as_view()),
    path('livescores/', views.LiveScores.as_view(), name='livescores-api'),
]
