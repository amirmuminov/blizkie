from django.urls import path
from . import views
urlpatterns = [
    path('sitters', views.SitterViews.as_view()),
    path('sitters/<int:pk>', views.SitterDeleteView.as_view())
]