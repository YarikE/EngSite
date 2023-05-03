import random
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BdWords
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .serializer import WordsAPIserializer
from rest_framework.response import Response

def main(request):
    return render(request, 'main.html')

def learn(request):
    return render(request, 'learn.html')

def about(request):
    return render(request, 'about.html')

def registration(request):
    return render(request, 'registration.html')

@csrf_exempt
def get_word(request):
    if request.method == 'POST':
        count_words = BdWords.objects.all().count()
        random_id = random.randint(1, count_words)

        current_word = BdWords.objects.get(pk=random_id)

        data = {
            'word': current_word.word,
            'trl_word': current_word.trl_word
        }

        return JsonResponse(data)


class API(APIView):
    def post(self, request):
        count_words = BdWords.objects.all().count()
        random_id = random.randint(1, count_words)

        current_word = BdWords.objects.get(pk=random_id)

        output = {
            'word': current_word.word,
            'trl_word': current_word.trl_word
        }
        return Response(output)

    # def post(self, request):
    #     serializer = WordsAPIserializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

def next_learn(request):
    return redirect(learn)
