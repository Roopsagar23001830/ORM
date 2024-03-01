from django.db import models
from django.contrib import admin 
class book(models.Model):
	bookid=models.IntegerField(primary_key=True);
	booktitle=models.CharField(max_length=100);
	bookauthor=models.CharField(max_length=100);
	year=models.DateField();
	authoremail=models.EmailField();
class bookAdmin(admin.ModelAdmin):
	list_display=("bookid","booktitle","bookauthor","year","authoremail")