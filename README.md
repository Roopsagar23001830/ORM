# Ex02 Django ORM Web Application
## Date: 26/02/2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![Screenshot 2024-03-26 145205](https://github.com/Roopsagar23001830/ORM/assets/145972515/5b850530-7384-4a55-8242-ec6363ce855c)



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
Models.py
from django.db import models
from django.contrib import admin
class Book(models.Model):
     bookid=models.IntegerField(primary_key=True);
     bookname=models.CharField(max_length=20);
     author=models.CharField(max_length=50);
     price=models.IntegerField();
     publishdate=models.DateField();
class BookAdmin(admin.ModelAdmin):
     list_display=("bookid","bookname","author","price","publishdate");
```
```
Admin.py
from django.contrib import admin
from .models import Book ,BookAdmin
admin.site.register(BookAdmin)
```



## OUTPUT
![alt text](<Screenshot 2024-03-26 144031.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
