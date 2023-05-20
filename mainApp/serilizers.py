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
    date=serializers.CharField(max_length=100,default='')
    like_count=serializers.IntegerField(default=0)
    
    def create(self,validatedData):
        return member_Story.objects.create(**validatedData)

class admin_StorySerializer(serializers.Serializer):
    id=serializers.IntegerField()
    content=serializers.CharField(max_length=300,default='')
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    file=serializers.FileField(max_length=None, use_url=True, allow_null=True, required=False)
    date=serializers.CharField(max_length=100,default='')
    like_count=serializers.IntegerField(default=0)
    def create(self,validatedData):
        return admin_Story.objects.create(**validatedData) 
    
class DonationSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name = serializers.CharField(max_length=50,default='')
    phone = serializers.CharField(max_length=10,default='')
    amount=serializers.IntegerField()
    description=serializers.CharField(max_length=500,default='')
    date=serializers.CharField(max_length=100,default='')

    
    def create(self,validatedData):
        return Donation.objects.create(**validatedData)
    

class SliderSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    
    def create(self,validatedData):
        return Slider.objects.create(**validatedData)

class FutureEventSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    title=serializers.CharField(max_length=300,default='')
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    description=serializers.CharField(max_length=500,default='')
    location=serializers.CharField(max_length=300,default='')
    date=serializers.CharField(max_length=100,default='')
    
    def create(self,validatedData):
        return FutureEvent.objects.create(**validatedData)
    

class Comment_SectionSerializer(serializers.Serializer):
       id=serializers.IntegerField()
       post_id=serializers.IntegerField()
       user_name=serializers.CharField(max_length=100)
       user_image=serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
       comment=serializers.CharField(max_length=1000)

       def create(self,validatedData):
        return Comment_Section.objects.create(**validatedData)
    
       

class Comment_SectionMemberSerializer(serializers.Serializer):
       id=serializers.IntegerField()
       post_id=serializers.IntegerField()
       user_name=serializers.CharField(max_length=100)
       user_image=serializers.ImageField(max_length=None,use_url=True,allow_null=True,required=False)
       comment=serializers.CharField(max_length=1000)

       def create(self,validatedData):
        return Comment_Section.objects.create(**validatedData)
    
       
class PustikaSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    file=serializers.FileField(max_length=None,use_url=True,allow_null=True,required=False)

    def create(self,validatedData):
        return Pustika.objects.create(**validatedData)
    
       
class Member_Login_NotificationSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    message=serializers.CharField(max_length=None,default='')

    def create(self,validatedData):
        return Member_Login_Notification.objects.create(**validatedData)
    

class Notification_For_MemberSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    message=serializers.CharField(max_length=None,default='')

    def create(self,validatedData):
        return Notification_For_Member.objects.create(**validatedData)
    
    