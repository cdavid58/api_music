from django.http import HttpResponse
from django.shortcuts import render
from .models import Gender

def Create(request):
	gender = [
			'Blues','Corrido','Country','Cumbia','Disco','Electrónica','Flamenco','Folk','Funk',
			'Gospel','Heavy Metal','Hip Hop','Indie','Jazz','Merengue','Pop','Punk','Ranchera',
			'Rap','Reggae','Reggaeton','Rumba','Rhythm and Blues','Rock','Rock and Roll',
			'Salsa','Son','Soul','Tango','Vallenato','Champeta'
		]
	for i in gender:
		try:
			Gender(name = i).save()
		except Exception as e:
			pass
		
	return HttpResponse("Listo")
