from django.shortcuts import render,HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
import io
import json
from django.conf import settings
from django.core.mail import send_mail

from .models import *
from .serilizers import *
@csrf_exempt
def registerMember(Request):
    # jsonData = Request.body
    # stream = io.BytesIO(jsonData)
    # pythonData = JSONParser().parse(stream)
    # phone=pythonData['phone']
    # try:
    #    data1 = Member.objects.filter(phone=phone)
    #    if(data1):
    #      msg = {"result":"Fail","msg":"Phone Number Already Exist!!!"}
    #    else:
    #       empSerializer = MemberSerializer(data=pythonData)
    #       if(empSerializer.is_valid()):
    #           empSerializer.save()
    #           msg = {"result":"Done","msg":"Member Added Successfuly !!!"}
    #       else:
    #          msg = {"result":"Fail","msg":"Record is Invalid !!!"}
    # except:
    #     msg = {"result":"Fail","msg":"Record is Invalid or User Already Exist!!!"}
    
    # responseMessage = JSONRenderer().render(msg)
    # return HttpResponse(responseMessage,content_type="application/json")
    

    if (Request.method=="POST"):
        p=Request.POST.get('phone')
        p1=Member.objects.filter(phone=p)
        if(p1):
             msg = {"result":"Fail","msg":"Phone Number Already Exist!!!"} 
        else:
              m=Member()
              m.name=Request.POST.get('name')
              m.phone=p
              m.email=Request.POST.get('email')
              m.password=Request.POST.get('password')
              m.country=Request.POST.get('country')
              m.state=Request.POST.get('state')
              m.city=Request.POST.get('city')
              m.area=Request.POST.get('area')
              m.address=Request.POST.get('address')
              m.pinCode=Request.POST.get('pinCode')
              m.aadhaar=Request.POST.get('aadhaar')
              m.photo=Request.FILES.get('photo')
              m.sanstha_name=Request.POST.get('sanstha_name')
              m.position=Request.POST.get('position')
              m.save()
      
              msg = {"result":"Done","msg":"Member Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def memberLogin(Request):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    phone=pythonData['phone']
    password=pythonData['password']
    try:
        data = Member.objects.get(phone=phone,password=password)
        if(data.status=="Active"):
          dataSerializer = MemberSerializer(data,many=False)
          realData={'status':True,'messgae':"Authentication Completed",'data':[dataSerializer.data]}
          return HttpResponse(json.dumps(realData),content_type="application/json")
            
        else:
            msg = {"result":"Fail","msg":"You Are Not Eligible To Login"}
    except:
        msg = {"result":"Fail","msg":"Record Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")





@csrf_exempt
def adminLogin(Request):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    username=pythonData['username']
    password=pythonData['password']
    try:
        user = authenticate(username=username, password=password)
        if (user is not None):
            login(Request, user)
            subject = 'Login Successfully : Team Eshop'
            message = "Helllo "+Request.user.first_name+"\nThanks For Login\ Eshop"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [Request.user.email ]
            send_mail( subject, message, email_from, recipient_list )
               
            # first_name=Request.user.first_name
            msg = {"result":"Done","msg":"Login Successfully!!!"}
        else:
            msg = {"result":"Fail","msg":"Invalid username and password!!!"}
             
    except:
        msg = {"result":"Fail","msg":"Record Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def updateMemberStatus(Request):
    jsonData = Request.body
    stream = io.BytesIO(jsonData)
    pythonData = JSONParser().parse(stream)
    try:
        emp=Member.objects.get(phone=pythonData['phone'])
        empSerializer = MemberSerializer(emp,data=pythonData,partial=True)
        if(empSerializer.is_valid()):
            empSerializer.save()
            msg = {"result":"Done","msg":"Record is Upated!!!"}            
        else:   
            msg = {"result":"Fail","msg":"Record is Not Valid!!!"}            
    except:
        msg = {"result":"Fail","msg":"Record Not Fond!!!"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")




@csrf_exempt
def addStory(Request):
    # jsonData = Request.body
    # stream = io.BytesIO(jsonData)
    # pythonData = JSONParser().parse(stream)
    # try:
    #       empSerializer = member_StorySerializer(data=pythonData)
    #       if(empSerializer.is_valid()):
    #           empSerializer.save()
    #           msg = {"result":"Done","msg":"Story Added Successfuly !!!"}
    #       else:
    #          msg = {"result":"Fail","msg":"Record is Invalid !!!"}
    # except:
    #     msg = {"result":"Fail","msg":"Record is Invalid Exception !!!"}
    
    # responseMessage = JSONRenderer().render(msg)
    # return HttpResponse(responseMessage,content_type="application/json")
    if Request.method=="POST":
        s=member_Story()
        s.user_name=Request.POST.get('user_name')
        s.user_image=Request.FILES.get('image')
        s.content=Request.POST.get('content')
        s.image=Request.FILES.get('image')
        s.file=Request.FILES.get('file')
        s.date=Request.POST.get('date')
        s.save()
        msg = {"result":"Done","msg":"Story Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewStory(Request):
    try:
        data = member_Story.objects.all().order_by('id').reverse()
        dataSerializer = member_StorySerializer(data,many=True)
        realData={'status':True,'messgae':"Story got Successfully ",'data':[dataSerializer.data]}
        return HttpResponse(json.dumps(realData),content_type="application/json")
            
    except:
        msg = {"result":"Fail","msg":"Story Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def updateMemberStory(Request,id):
    if Request.method=="POST":
        s=member_Story.objects.get(id=id)
        s.user_name=Request.POST.get('user_name')
        s.user_image=Request.FILES.get('image')
        s.content=Request.POST.get('content')
        s.image=Request.FILES.get('image')
        s.file=Request.FILES.get('file')
        s.date=Request.POST.get('date')
        s.save()
        msg = {"result":"Done","msg":"Story Updated Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def deleteMemberStory(Request,id):
        s=member_Story.objects.get(id=id)
        s.delete()
        msg = {"result":"Done","msg":"Story deleted Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def addDonation(Request):
    if Request.method=="POST":
        d=Donation()
        d.amount=Request.POST.get('amount')
        d.description=Request.POST.get('description')
        d.date=Request.POST.get('date')
        d.save()
        msg = {"result":"Done","msg":"Donation Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")



@csrf_exempt
def addAdminStory(Request):
    # jsonData = Request.body
    # stream = io.BytesIO(jsonData)
    # pythonData = JSONParser().parse(stream)
    # try:
    #       empSerializer = member_StorySerializer(data=pythonData)
    #       if(empSerializer.is_valid()):
    #           empSerializer.save()
    #           msg = {"result":"Done","msg":"Story Added Successfuly !!!"}
    #       else:
    #          msg = {"result":"Fail","msg":"Record is Invalid !!!"}
    # except:
    #     msg = {"result":"Fail","msg":"Record is Invalid Exception !!!"}
    
    # responseMessage = JSONRenderer().render(msg)
    # return HttpResponse(responseMessage,content_type="application/json")
    if Request.method=="POST":
        s=admin_Story()
        s.content=Request.POST.get('content')
        s.image=Request.FILES.get('image')
        s.file=Request.FILES.get('file')
        s.date=Request.POST.get('date')
        s.save()
        msg = {"result":"Done","msg":"Story Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewAdminStory(Request):
    try:
        data = admin_Story.objects.all().order_by('id').reverse()
        dataSerializer = admin_StorySerializer(data,many=True)
        realData={'status':True,'messgae':"Story got Successfully ",'data':[dataSerializer.data]}
        return HttpResponse(json.dumps(realData),content_type="application/json")
            
    except:
        msg = {"result":"Fail","msg":"Story Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def updateAdminStory(Request,id):
    if Request.method=="POST":
        s=admin_Story.objects.get(id=id)
        s.content=Request.POST.get('content')
        s.image=Request.FILES.get('image')
        s.file=Request.FILES.get('file')
        s.date=Request.POST.get('date')
        s.save()
        msg = {"result":"Done","msg":"Story Updated Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def deleteAdminStory(Request,id):
        s=admin_Story.objects.get(id=id)
        s.delete()
        msg = {"result":"Done","msg":"Story deleted Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def addDonation(Request):
    if Request.method=="POST":
        d=Donation()
        d.amount=Request.POST.get('amount')
        d.description=Request.POST.get('description')
        d.date=Request.POST.get('date')
        d.save()
        msg = {"result":"Done","msg":"Donation Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")



@csrf_exempt
def viewDonation(Request):
    try:
        data = Donation.objects.all().order_by('id').reverse()
        dataSerializer = DonationSerializer(data,many=True)
        realData={'status':True,'messgae':"Donation got Successfully ",'data':[dataSerializer.data]}
        return HttpResponse(json.dumps(realData),content_type="application/json")
            
    except:
        msg = {"result":"Fail","msg":"Donation Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def addSlider(Request):
    if Request.method=="POST":
        s=Slider()
        s.image=Request.FILES.get('image')
        if(s.image): 
           s.save()
           msg = {"result":"Done","msg":"Slider Added Successfuly !!!"}
        else:
            msg = {"result":"Fail","msg":"Please Select an Image !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewSlider(Request):
    try:
        data = Slider.objects.all().order_by('id').reverse()
        dataSerializer = SliderSerializer(data,many=True)
        realData={'status':True,'messgae':"Slider got Successfully ",'data':[dataSerializer.data]}
        return HttpResponse(json.dumps(realData),content_type="application/json")
            
    except:
        msg = {"result":"Fail","msg":"Slider Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

def deleteSlider(Request,id):
    s=Slider.objects.get(id=id)
    s.delete()
    msg={'status':True,'message':"Slider Deleted Successfully"}
    jsonData=JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def addFutureEvent(Request):
    if Request.method=="POST":
        f=FutureEvent()
        f.title=Request.POST.get('title')
        f.image=Request.FILES.get('image')
        f.description=Request.POST.get('description')
        f.location=Request.POST.get('location')
        f.date=Request.POST.get('date')
        f.save()
        
        msg = {"result":"Done","msg":"FutureEvent Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewFutureEvent(Request):
    try:
        data = FutureEvent.objects.all().order_by('id').reverse()
        dataSerializer = FutureEventSerializer(data,many=True)
        realData={'status':True,'messgae':"FutureEvent got Successfully ",'data':[dataSerializer.data]}
        return HttpResponse(json.dumps(realData),content_type="application/json")
            
    except:
        msg = {"result":"Fail","msg":"FutureEvent Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def getAllMember(Request):
    try:
        data = Member.objects.all().order_by('id').reverse()
        dataSerializer = MemberSerializer(data,many=True)
        realData={'status':True,'messgae':"Member got Successfully ",'data':[dataSerializer.data]}
        return HttpResponse(json.dumps(realData),content_type="application/json")
            
    except:
        msg = {"result":"Fail","msg":"Member Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

