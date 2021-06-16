from django.db import models
from time import localtime, strftime
import re

from django.db.models.deletion import CASCADE
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        lisOfEmails = User.objects.filter(email=postData['email'])
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if len(lisOfEmails):
            errors['email'] = "Email is Alerdy exist"

        # add keys and values to errors dictionary for each invalid fieldcopy
        if len(postData['firstname']) < 2:
            errors["firstname"] = "User first should be at least 2 characters"
        if len(postData['lastname']) < 2:
            errors["lastname"] = "User Last name should be at least 2 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "User Password should be at least 8 characters"
        todayTime= strftime("%Y-%m-%d", localtime())
        postTime = postData['birth_date']
        todayTimeList = todayTime.split("-")
        postTimeList = postTime.split("-")
        if (todayTimeList[0] <= postTimeList[0]):
            if  (todayTimeList[1] <= postTimeList[1]):
                if (todayTimeList[2] < postTimeList[2]):
                    errors["birth_date"] = "BirthDay is in the future"
        if postTime:
            todayTimeAge = int(todayTimeList[0]) + int(todayTimeList[1]) + int(todayTimeList[2])
            postTimeAge = int(postTimeList[0]) + int(postTimeList[1]) + int(postTimeList[2])
            age = todayTimeAge - postTimeAge 
            if age < 13:
                errors["Age"] = "Sorry Your Age less than 13 !"+str(age)
        return errors
    def login_Validator(self,postData):
        errors2={}
        if len(postData['loginemail']) == 0 :
            errors2["loginemail"] = "Please enter Valid email or Password to login "
        if len(postData['loginpass']) == 0:
            errors2["loginpass"] = "Please enter Valid email or Password to login "
        lisOfEmails = User.objects.filter(email=postData['loginemail'])
        lisOfPassword = User.objects.filter(passwod=postData['loginpass'])
        
        
        return errors2
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    passwod = models.CharField(max_length=255)
    dateOfBirth = models.DateField(null=True, verbose_name='Date of Birth')
    objects = BlogManager()
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User , related_name="books_uploaded",on_delete=CASCADE)
    users_who_like = models.ManyToManyField(User,related_name="liked_books" )
