from django.urls import path
from .views import main, learn, about, registration, get_word, API, next_learn

urlpatterns = [
    path('main/', main, name='main'),
    path('learn/', learn, name='learn'),
    path('about/', about, name='about'),
    path('registration/', registration, name='registration'),
    path('get-word/', API.as_view(), name='get-word'),
    path('next-learn/', next_learn, name='next-learn')
]