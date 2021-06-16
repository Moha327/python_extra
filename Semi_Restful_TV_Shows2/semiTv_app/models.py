from django.db import models

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Title should be at least 2 charachter"
        if len(postData['network']) < 3:
            errors["network"] = "network should be at least 10 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        return errors


class Show(models.Model):
    title=models.CharField(max_length=200)
    network=models.CharField(max_length=200)
    releaseDate=models.DateField()
    desc=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager() 
   


def create_show(title, network, date, desc):
    return Show.objects.create(title=title, network=network, releaseDate=date, desc=desc)    

def Show_with_Id(id):
    return Show.objects.get(id=id)    

def get_all_show():
    return Show.objects.all()