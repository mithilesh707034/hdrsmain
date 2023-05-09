from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=50,default="")
    phone = serializers.CharField(max_length=10,default="")
    email = serializers.EmailField(default="")
    password=serializers.CharField(max_length=15)
    country=serializers.CharField(max_length=50,default="")
    state=serializers.CharField(max_length=50,default="")
    city=serializers.CharField(max_length=50,default="")
    area=serializers.CharField(max_length=50,default="")
    address=serializers.CharField(max_length=200,default="")
    pinCode=serializers.CharField(max_length=6,default="")
    aadhaar=serializers.CharField(max_length=12,default="")  
    photo=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    sanstha_name=serializers.CharField(max_length=50,default="")
    position=serializers.CharField(max_length=50,default="")
    status=serializers.CharField(max_length=50,default="Deactive")
 
    def create(self,validatedData):
        return Member.objects.create(**validatedData)
    
    def update(self,instance,validatedData):
        if("status" in validatedData and validatedData['status']!=''):
            instance.status = validatedData['status']
        instance.save()
        return instance
    
class member_StorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    user_name=serializers.CharField(max_length=50,default='')
    user_image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    content=serializers.CharField(max_length=300,default='')
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    file=serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)
    status=serializers.CharField(max_length=10,default="Deactive")
    date=serializers.DateTimeField()
    
    def create(self,validatedData):
        return member_Story.objects.create(**validatedData)

class admin_StorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    content=serializers.CharField(max_length=300,default='')
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    file=serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)
    date=serializers.DateTimeField()
    def create(self,validatedData):
        return admin_Story.objects.create(**validatedData) 
    
class DonationSerializer(serializers.Serializer):
    id=models.IntegerField()
    amount=serializers.IntegerField()
    description=serializers.CharField(max_length=500,default='')
    created_at=serializers.DateTimeField()

    
    def create(self,validatedData):
        return Donation.objects.create(**validatedData)
    

class SliderSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    
    def create(self,validatedData):
        return Slider.objects.create(**validatedData)

class FutureEventSerializer(serializers.Serializer):
    id=models.IntegerField()
    title=serializers.CharField(max_length=300,default='')
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    description=serializers.CharField(max_length=500,default='')
    location=serializers.CharField(max_length=300,default='')
    date=serializers.CharField(max_length=100,default='')
    
    def create(self,validatedData):
        return FutureEvent.objects.create(**validatedData)
    
