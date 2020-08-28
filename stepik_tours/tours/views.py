from django.views import View
from django.shortcuts import render
from django.http import Http404

# Create your views here.


class MainView(View):
    def get(self, request):
        return render(request, 'index.html')


class DepartureView(View):
    def get(self, request, departure):
        context = {
            'departure': departure,
        }
        return render(request, 'departure.html', context)


class TourView(View):
    def get(self, request, id):
        context = {
            'id': id,
        }
        return render(request, 'tour.html', context)
