from django.utils.crypto import get_random_string
from django.db import models
from request_music.models import Gender

class BarConfigs(models.Model):
	code = models.CharField(max_length=10, default=get_random_string(length=10))
	name = models.CharField( max_length= 60, unique=True)
	phone = models.CharField(max_length=12)
	lat = models.CharField(max_length = 15)
	log = models.CharField(max_length = 15)
	block = models.BooleanField(default= False)

	def __str__(self):
		return self.name

class Gender_Bar(models.Model):
	bar = models.ForeignKey(BarConfigs, on_delete=models.CASCADE)
	gender_1 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_1',null=True,blank=True)
	gender_2 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_2',null=True,blank=True)
	gender_3 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_3',null=True,blank=True)
	gender_4 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_4',null=True,blank=True)
	gender_5 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_5',null=True,blank=True)
	gender_6 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_6',null=True,blank=True)
	gender_7 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_7',null=True,blank=True)
	gender_8 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_8',null=True,blank=True)
	gender_9 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_9',null=True,blank=True)
	gender_10 = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='gender_10',null=True,blank=True)


class Song(models.Model):
	bar = models.ForeignKey(BarConfigs, on_delete = models.CASCADE)
	music = models.CharField(max_length = 150)
	artist = models.CharField(max_length = 150)
	