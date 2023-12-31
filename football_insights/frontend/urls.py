from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('livescores', index),
    path('livescores/<int:id>', index),
    path('fixtures', index),
    path('fixtures/<int:id>', index),
    path('predictions', index),
    path('leaguetable', index),
    path('teams', index),
    path('teams/<int:id>', index),
    path('players/goalkeepers', index),
    path('players/defenders', index),
    path('players/midfielders', index),
    path('players/forwards', index),
    path('players/<int:id>', index),
]
