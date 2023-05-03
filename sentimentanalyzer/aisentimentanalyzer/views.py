from django.shortcuts import render

from .apps import AisentimentanalyzerConfig
from django.http import JsonResponse
from rest_framework.views import APIView

class call_model(APIView):
    def get(self, request):
        if request.method == 'GET':

            text = request.GET.get('text')

            #vectorize text
            vector = AisentimentanalyzerConfig.vectorizer.transform([text])
            #predict based on vector
            prediction = AisentimentanalyzerConfig.model.predict(vector)[0]
            #predict probabilities based on vector
            probabilities = AisentimentanalyzerConfig.model.predict_proba(vector)
            #Find the maximum probablity among the list
            max_prob = max(probabilities[0])
            #build response
            response = {
                'text': text,
                'sentiment': prediction,
                'probabilities': max_prob
            }

            return JsonResponse(response)
        else:
            return JsonResponse({'error': 'Text parameter is missing'})


