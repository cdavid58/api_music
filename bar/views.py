from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from bar.models import BarConfigs, Gender_Bar, Song
import logging, socket

@api_view(['POST'])
def Get_Gender_Bar(request):
	data = request.data
	i = Gender_Bar.objects.get(bar = BarConfigs.objects.get(code = data['code']))
	data = {
			'name':i.bar.name,
			'gender_1':i.gender_1.name,
			'gender_2':i.gender_2.name if i.gender_2 is not None else None,
			'gender_3':i.gender_3.name if i.gender_3 is not None else None,
			'gender_4':i.gender_4.name if i.gender_4 is not None else None,
			'gender_5':i.gender_5.name if i.gender_5 is not None else None,
			'gender_6':i.gender_6.name if i.gender_6 is not None else None,
			'gender_7':i.gender_7.name if i.gender_7 is not None else None,
			'gender_8':i.gender_8.name if i.gender_8 is not None else None,
			'gender_9':i.gender_9.name if i.gender_9 is not None else None,
			'gender_10':i.gender_10.name if i.gender_10 is not None else None
		}
	return Response(data)

@api_view(['POST'])
def Verified_Login(request):
	data = request.data
	try:
		bar = BarConfigs.objects.get(code=data['code'])
		logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')
		logging.info('Número que ingreso es:'+data['number_phone'])
		request.session['code'] = bar.code
		bar = {'Message':True}
	except BarConfigs.DoesNotExist:
		bar = {'Message':False}
	return Response(bar)


@api_view(['POST'])
def Save_Song(request):
	data = request.data
	print(data)
	Song(
		bar = BarConfigs.objects.get(code=data['code']),
		music = data['music'],
		artist=data['artist']
	).save()
	return Response({'message':True})


@api_view(['POST'])
def Get_List_Song(request):
	data = request.data
	song = Song.objects.filter(bar = BarConfigs.objects.get(code=data['code']))
	data = [
		{
			'music':i.music,
			'artist': i.artist
		}
		for i in song
	]
	return Response(data)
