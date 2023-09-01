from django.http.response import HttpResponse
from django.shortcuts import render
from app_cards.models import Cards
from django.http import Http404


# Create your views here.

def cards(request):
    all_cards = Cards.objects.all()
   
    return render(request,'app_cards/cards.html',{"all_cards":all_cards})

def card(request,card_id):
    card = Cards.objects.get(pk=card_id)
    if card is not None:
        return render(request, 'app_cards/cards.html',{"card":card})
    else:
        raise Http404('ไม่พบการ์ด')
 

