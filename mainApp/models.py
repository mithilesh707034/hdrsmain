from django.db import models


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default='',null=True,blank=True)
    phone = models.CharField(max_length=10,default='',null=True,blank=True)
    email = models.EmailField()
    password=models.CharField(max_length=15,default='',null=True,blank=True)
    country=models.CharField(max_length=50,default='',null=True,blank=True)
    state=models.CharField(max_length=50,default='',null=True,blank=True)
    city=models.CharField(max_length=50,default='',null=True,blank=True)
    area=models.CharField(max_length=50,default='',null=True,blank=True)
    address=models.CharField(max_length=200,default='',null=True,blank=True)
    pinCode=models.CharField(max_length=6,default='',null=True,blank=True)
    aadhaar=models.CharField(max_length=12,default='',null=True,blank=True)  
    photo=models.ImageField(upload_to="uploads",default='',blank=True,null=True)
    sanstha_name=models.CharField(max_length=50,default='',null=True,blank=True)
    position=models.CharField(max_length=50,default='',null=True,blank=True)
    status=models.CharField(max_length=50,default='Deactive',null=True,blank=True)
    
    def __str__(self):
        return self.name
     
class member_Story(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=50,default='',null=True,blank=True)
    user_image=models.ImageField(upload_to="uploads",default='',blank=True,null=True)
    content=models.CharField(max_length=300,default='',blank=True,null=True)
    image=models.ImageField(upload_to="uploads",default='',blank=True,null=True)
    file=models.FileField(upload_to='uploads',default='',blank=True,null=True)
    status=models.CharField(max_length=10,default="Deactive",blank=True,null=True)
    date=models.DateTimeField(auto_created=True)

class admin_Story(models.Model):
    id=models.AutoField(primary_key=True)
    content=models.CharField(max_length=300,default='',blank=True,null=True)
    image=models.ImageField(upload_to="uploads",default='',blank=True,null=True)
    file=models.FileField(upload_to='uploads',default='',blank=True,null=True)
    date=models.DateTimeField(auto_created=True)

    
class Donation(models.Model):
    id=models.AutoField(primary_key=True)
    amount=models.IntegerField()
    description=models.CharField(max_length=300,default='',blank=True,null=True)
    date = models.DateTimeField(auto_created=True,null=True,blank=True)
    def __str__(self):
        return str(self.amount)
    

class Slider(models.Model):
    id=models.AutoField(primary_key=True)
    image=models.ImageField(upload_to="uploads",default='',blank=True,null=True)


class FutureEvent(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=300,default='',blank=True,null=True)
    image=models.ImageField(upload_to="uploads",default='',blank=True,null=True)
    description=models.TextField(default='',blank=True,null=True)
    location=models.CharField(max_length=300,default='',blank=True,null=True)
    date=models.CharField(max_length=100,default='',blank=True,null=True)
    def __str__(self):
        return self.title
    
