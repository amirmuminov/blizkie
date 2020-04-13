from django.urls import path
from . import views

urlpatterns = [
    path('meals', views.MealView.as_view()),
    path('meals/<int:pk>', views.MealDeleteView.as_view()),
    path('toilets', views.ToiletView.as_view()),
    path('toilets/<int:pk>', views.ToiletDeleteView.as_view()),
    path('mobilities', views.MobilityView.as_view()),
    path('mobilities/<int:pk>', views.MobilityDeleteView.as_view()),
    path('mentalstates', views.MentalStateView.as_view()),
    path('mentalstates/<int:pk>', views.MentalStateDeleteView.as_view()),
    path('levelselfserv', views.LevelSelfServView.as_view()),
    path('levelselfserv/<int:pk>', views.LevelSelfServDeleteView.as_view()),
    path('cities', views.CityView.as_view()),
    path('cities/<int:pk>', views.CityDeleteView.as_view()),
    path('places', views.PlaceView.as_view()),
    path('places/<int:pk>', views.PlaceDeleteView.as_view()),
    path('patients', views.PatientView.as_view())
]
