from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    # books = 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title=models.CharField(max_length=200)
    desc=models.TextField()
    users=models.ManyToManyField(User,related_name="books")
    uploaded_by_id=models.ForeignKey(User,related_name="user_books", on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Car(models.Model):
    name =  models.CharField(max_length=200)
    model = models.IntegerField()
    clients = models.ManyToManyField(User,related_name = "cars")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

def create_user(first_name, last_name,email,passwd):                     
    return User.objects.create(first_name=first_name,last_name=last_name,email=email,passwd=passwd)
def create_book(title,desc,user_id):   
    user=User.objects.get(id=user_id)    

    book = Book.objects.create(title=title,de)

def get_user(email,passwd):
    users = User.objects.filter(email=email,passwd=passwd)
    if len(users) > 0:
        return users[0]
    return None

def get_user_cars(id):
    user = User.objects.get(id=id)
    return user.cars.all()

def get_user_cars(id):
    user = User.objects.get(id=id)
    return user.cars.all()

