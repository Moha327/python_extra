from django.db import models
import re

from django.db.models.deletion import CASCADE	

class BlogManager(models.Manager):
    
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        lisOfEmails = User.objects.filter(email=postData['email'])
        if not EMAIL_REGEX.match(postData['email']):              
            errors['email'] = "Invalid email address!"
        if len(lisOfEmails):
            errors['email'] = "Email is Alerdy exist"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "User first should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = -"User Last name should be at least 2 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "User Password should be at least 8 characters"
        return errors
def login_Validator(self,postData):
        errors2={}
        if len(postData['loginemail']) == 0 :
            errors2["loginemail"] = "Please enter Valid email or Password to login "
        if len(postData['loginpass']) == 0:
            errors2["loginpass"] = "Please enter Valid email or Password to login "
        emails = User.objects.filter(email=postData['email'])
        password = User.objects.filter(passwod=postData['passwd'])

def thought_Validator(self,postData):
        errors3={}
        if len(postData['textbox']) < 5 :
            errors2["textbox"] = "Error "
        first_name = User.objects.filter(email=postData['first_name'])
      
class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    passwd= models.CharField(max_length=255)
    desc = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects = BlogManager() 



class Thought(models.Model):
    post = models.TextField()
    uploaded_by=models.ForeignKey(User, related_name="thoughts", on_delete=models.CASCADE)
    liked=models.ManyToManyField(User, related_name="likes")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

def createThought(desc, userId):
    thisUser = User.objects.get(id=userId)
    thisThought=Thought.objects.create(post=desc,uploadeBy=thisUser)
    thisUser.createdThoughts.add(thisThought)
    return thisThought

