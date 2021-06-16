from django.db import models
import re

from django.db.models.deletion import CASCADE	# the regex module

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        Letters_REGEX = re.compile(r'^[a-zA-Z]+$')

        if len(postData['name']) < 2 or not Letters_REGEX.match(postData['name']):    # test whether a field matches the pattern            
                errors["name"] = "Blog name should be at least 2 letters"
        if len(postData['alios']) < 2 or not Letters_REGEX.match(postData['alios']):    # test whether a field matches the pattern            
                errors["alios"] = "Blog alios should be at least 2 letters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "Blog passwordd should be at least 8 characters"
        if postData['passwd'] != postData['conpasswd']:
            errors["conpasswd"] = "Password and Password confirmation don't match! "
        if len(postData['release_date']) < 10:
            errors["release_date"] = "Show release date should be at least 10 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors

class User(models.Model):
    name= models.CharField(max_length=255)
    alios= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    passwd= models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    release_date = models.DateTimeField()
    objects = UserManager()  

class Car(models.Model):
    name = models.CharField(max_length=255)
    model= models.IntegerField()
    users= models.ManyToManyField(User,related_name="cars")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True) 

def create_user(name,alios,email,passwd,release_date):
    return User.objects.create(name=name,alios=alios,email=email,passwd=passwd,release_date=release_date)
    

def get_user(email):
    users= User.objects.filter(email=email)
    if len(users)>0:
        return users[0]
    return None

def get_this_user(id):
    user = User.objects.get(id = id)
    print("Getted*****************************************")
    return user
