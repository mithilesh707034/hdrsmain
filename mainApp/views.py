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
    #      msg = {"result":"Fail","message":"Phone Number Already Exist!!!"}
    #    else:
    #       empSerializer = MemberSerializer(data=pythonData)
    #       if(empSerializer.is_valid()):
    #           empSerializer.save()
    #           msg = {"result":"Done","message":"Member Added Successfuly !!!"}
    #       else:
    #          msg = {"result":"Fail","message":"Record is Invalid !!!"}
    # except:
    #     msg = {"result":"Fail","message":"Record is Invalid or User Already Exist!!!"}

    # responseMessage = JSONRenderer().render(msg)
    # return HttpResponse(responseMessage,content_type="application/json")


    if (Request.method=="POST"):
        p=Request.POST.get('phone')
        p1=Member.objects.filter(phone=p)
        if(p1):
             msg = {"result":"Fail","message":"Phone Number Already Exist!!!"}
        else:
              m=Member()
              n=Member_Login_Notification()
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
              n.message="Dear Admin "+m.name +" is Registered Successfully"+" Please Verify Him"
              n.save()

              msg = {"result":"Done","message":"Member Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def updateMemberProfile(Request):
    if (Request.method=="POST"):
        p=Request.POST.get('phone')
        m=Member.objects.get(phone=p)
        m.name=Request.POST.get('name')
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

        msg = {"result":True,"message":"Member Updated Successfuly !!!"}
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
          realData={'result':True,'message':"Authentication Completed",'data':[dataSerializer.data]}
          return HttpResponse(json.dumps(realData),content_type="application/json")

        else:
            msg = {"result":False,"message":"You Are Not Eligible To Login"}
    except:
        msg = {"result":False,"message":"Record Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def memberProfile(Request):
    try:
       if(Request.method=="POST"):
         phone=Request.POST.get('phone')
      
         data = Member.objects.get(phone=phone)
         if(data.status=="Active"):
           dataSerializer = MemberSerializer(data,many=False)
           realData={'result':True,'messgae':"Profile Got Succcessfully",'data':[dataSerializer.data]}
           return HttpResponse(json.dumps(realData),content_type="application/json")
  
       else:
            msg = {"result":False,"message":"You Are Not Eligible To Login"}
    except:
        msg = {"result":False,"message":"Record Not Found"}
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
            # subject = 'Login Successfully : Team Eshop'
            # message = "Helllo "+Request.user.first_name+"\nThanks For Login\ Eshop"
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [Request.user.email ]
            # send_mail( subject, message, email_from, recipient_list )

            # first_name=Request.user.first_name
            msg = {"result":"Done","message":"Login Successfully!!!"}
        else:
            msg = {"result":"Fail","message":"Invalid username and password!!!"}

    except:
        msg = {"result":"Fail","message":"Record Not Found"}
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
            msg = {"result":"Done","message":"Record is Upated!!!"}
        else:
            msg = {"result":"Fail","message":"Record is Not Valid!!!"}
    except:
        msg = {"result":"Fail","message":"Record Not Fond!!!"}
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
    #           msg = {"result":"Done","message":"Story Added Successfuly !!!"}
    #       else:
    #          msg = {"result":"Fail","message":"Record is Invalid !!!"}
    # except:
    #     msg = {"result":"Fail","message":"Record is Invalid Exception !!!"}

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
        msg = {"result":"Done","message":"Story Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewStory(Request):
    try:
        data = member_Story.objects.all().order_by('id').reverse()
        dataSerializer = member_StorySerializer(data,many=True)
        realData={'status':True,'messgae':"Story got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Story Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def viewSingleMemberStory(Request):
    if(Request.method=="POST"):
        user_name=Request.POST.get('user_name')
        data = member_Story.objects.filter(user_name=user_name)
        if(data):
           dataSerializer = member_StorySerializer(data,many=True)
           realData={'status':True,'message':"Story got Successfully ",'data':dataSerializer.data}
           return HttpResponse(json.dumps(realData),content_type="application/json")

        else:
            msg = {"result":"Fail","message":"Story Not Found"}
            jsonData = JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def updateMemberStory(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        s=member_Story.objects.get(id=id)
        if(s):
           s.user_name=Request.POST.get('user_name')
           s.user_image=Request.FILES.get('user_image')
           s.content=Request.POST.get('content')
           s.image=Request.FILES.get('image')
           s.file=Request.FILES.get('file')
           s.date=Request.POST.get('date')
           s.save()
        msg = {"result":"Done","message":"Story Updated Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def updateMemberStoryStatus(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        s=member_Story.objects.get(id=id)
        if(s):
          s.status=Request.POST.get('status')
          s.save()
        msg = {"result":"Done","message":"Story Status Updated Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def deleteMemberStory(Request,id):
        s=member_Story.objects.get(id=id)
        s.delete()
        msg = {"result":"Done","message":"Story deleted Successfuly !!!"}
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
        msg = {"result":"Done","message":"Donation Added Successfuly !!!"}
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
    #           msg = {"result":"Done","message":"Story Added Successfuly !!!"}
    #       else:
    #          msg = {"result":"Fail","message":"Record is Invalid !!!"}
    # except:
    #     msg = {"result":"Fail","message":"Record is Invalid Exception !!!"}

    # responseMessage = JSONRenderer().render(msg)
    # return HttpResponse(responseMessage,content_type="application/json")
    if Request.method=="POST":
        s=admin_Story()
        s.content=Request.POST.get('content')
        s.image=Request.FILES.get('image')
        s.file=Request.FILES.get('file')
        s.date=Request.POST.get('date')
        s.save()
        msg = {"result":"Done","message":"Story Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewAdminStory(Request):
    try:
        data = admin_Story.objects.all().order_by('id').reverse()
        dataSerializer = admin_StorySerializer(data,many=True)
        realData={'status':True,'message':"Story got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Story Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def updateAdminStory(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        s=admin_Story.objects.get(id=id)
        if(s):
            s.content=Request.POST.get('content')
            s.image=Request.FILES.get('image')
            s.file=Request.FILES.get('file')
            s.date=Request.POST.get('date')
            s.save()
        msg = {"result":"Done","message":"Story Updated Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def deleteAdminStory(Request,id):
        s=admin_Story.objects.get(id=id)
        s.delete()
        msg = {"result":"Done","message":"Story deleted Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def addDonation(Request):
    if Request.method=="POST":
        d=Donation()
        d.name=Request.POST.get('name')
        d.phone=Request.POST.get('phone')
        d.amount=Request.POST.get('amount')
        d.description=Request.POST.get('description')
        d.date=Request.POST.get('date')
        d.save()
        msg = {"result":"Done","message":"Donation Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")



@csrf_exempt
def viewDonation(Request):
    try:
        data = Donation.objects.all().order_by('id').reverse()
        dataSerializer = DonationSerializer(data,many=True)
        realData={'status':True,'message':"Donation got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Donation Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")



@csrf_exempt
def viewSingleDonation(Request):
        if(Request.method=="POST"):
            phone=Request.POST.get('phone')
            data = Donation.objects.filter(phone=phone)
            if(data):
                 dataSerializer = DonationSerializer(data,many=True)
                 realData={'status':True,'message':"Donation got Successfully ",'data':dataSerializer.data}
                 return HttpResponse(json.dumps(realData),content_type="application/json")
    
            else:
                 msg = {"result":False,"message":"Donation Not Found"}
                 jsonData = JSONRenderer().render(msg)
                 return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def addSlider(Request):
    if Request.method=="POST":
        s=Slider()
        s.image=Request.FILES.get('image')
        if(s.image):
           s.save()
           msg = {"result":"Done","message":"Slider Added Successfuly !!!"}
        else:
            msg = {"result":"Fail","message":"Please Select an Image !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")
    
@csrf_exempt
def updateSlider(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        s=Slider.objects.get(id=id)
        s.image=Request.FILES.get('image')
        if(s.image):
           s.save()
           msg = {"result":"Done","message":"Slider Updated Successfuly !!!"}
        else:
            msg = {"result":"Fail","message":"Please Select an Image !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewSlider(Request):
    try:
        data = Slider.objects.all().order_by('id').reverse()
        dataSerializer = SliderSerializer(data,many=True)
        realData={'status':True,'message':"Slider got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Slider Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def deleteSlider(Request,id):
    s=Slider.objects.get(id=id)
    s.delete()
    msg={'result':'Done','message':"Slider Deleted Successfully"}
    jsonData=JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def addFutureEvent(Request):
    if Request.method=="POST":
        f=FutureEvent()
        n=Notification_For_Member()
        f.title=Request.POST.get('title')
        f.image=Request.FILES.get('image')
        f.description=Request.POST.get('description')
        f.location=Request.POST.get('location')
        f.date=Request.POST.get('date')
        f.save()
        n.message="Dear Member Future Event is Published Please Check it Now !!!"
        n.save()
        msg = {"result":"Done","message":"FutureEvent Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewFutureEvent(Request):
    try:
        data = FutureEvent.objects.all().order_by('id').reverse()
        dataSerializer = FutureEventSerializer(data,many=True)
        realData={'status':True,'message':"FutureEvent got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"FutureEvent Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def updateFutureEvent(Request):
    if Request.method=="POST":

        id=Request.POST.get('id')
        s=FutureEvent.objects.get(id=id)
        s.title=Request.POST.get('title')
        s.image=Request.FILES.get('image')
        s.description=Request.POST.get('description')
        s.location=Request.POST.get('location')
        s.date=Request.POST.get('date')
        s.save()

        msg = {"result":"Done","message":"FutureEvent Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def deleteFutureEvent(Request):
    if(Request.method=="POST"):
        id=Request.POST.get('id')
        s=FutureEvent.objects.get(id=id)
        s.delete()
        msg={'status':True,'message':"FutureEvent Deleted Successfully"}
        jsonData=JSONRenderer().render(msg)
        return HttpResponse(jsonData,content_type="application/json")


@csrf_exempt
def getAllMember(Request):
    try:
        data = Member.objects.all().order_by('id').reverse()
        dataSerializer = MemberSerializer(data,many=True)
        realData={'status':True,'message':"Member got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Member Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")



#Comment Sections of Admin
@csrf_exempt
def addComment_Section(Request):
    if Request.method=="POST":
        c=Comment_Section()
        c.post_id=Request.POST.get('post_id')
        c.user_name=Request.POST.get('user_name')
        c.user_image=Request.FILES.get('user_image')
        c.comment=Request.POST.get('comment')
        c.save()

        msg = {"result":"Done","message":"Comment Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewComment_Section(Request):
    try:
        data = Comment_Section.objects.all().order_by('id').reverse()
        dataSerializer = Comment_SectionSerializer(data,many=True)
        realData={'status':True,'message':"Comments got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Comment Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def updateComment_Section(Request):
    if Request.method=="POST":

        id=Request.POST.get('id')
        c=Comment_Section.objects.get(id=id)
        c.comment=Request.POST.get('comment')
        c.save()

        msg = {"result":"Done","message":"Comment Updated Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def deleteComment_Section(Request):
        if(Request.method=="POST"):
            id=Request.POST.get('id')
            s=Comment_Section.objects.get(id=id)
            s.delete()
            msg={'status':True,'message':"Comment Deleted Successfully"}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")


#Like Sections of Amin
@csrf_exempt
def addLike_Section(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        l=admin_Story.objects.get(id=id)
        l.like_count+=1
        l.save()

        msg = {"result":"Done","message":"Like Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def minusLike_Section(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        l=admin_Story.objects.get(id=id)
        if(l.like_count>0):
           l.like_count-=1
           l.save()
           msg = {"result":"Done","message":"Dislike Added Successfuly !!!"}
        else:
            msg = {"result":"Fail","message":"Total Like is 0"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")
    

#Comment Sections Member
@csrf_exempt
def addComment_SectionMember(Request):
    if Request.method=="POST":
        c=Comment_SectionMember()
        c.post_id=Request.POST.get('post_id')
        c.user_name=Request.POST.get('user_name')
        c.user_image=Request.FILES.get('user_image')
        c.comment=Request.POST.get('comment')
        c.save()

        msg = {"result":"Done","message":"Comment Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def viewComment_SectionMember(Request):
    try:
        data = Comment_SectionMember.objects.all().order_by('id').reverse()
        dataSerializer = Comment_SectionMemberSerializer(data,many=True)
        realData={'status':True,'message':"Comments got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Comment Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")

@csrf_exempt
def updateComment_SectionMember(Request):
    if Request.method=="POST":

        id=Request.POST.get('id')
        c=Comment_SectionMember.objects.get(id=id)
        c.comment=Request.POST.get('comment')
        c.save()

        msg = {"result":"Done","message":"Comment Updated Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def deleteComment_SectionMember(Request):
        if(Request.method=="POST"):
            id=Request.POST.get('id')
            s=Comment_SectionMember.objects.get(id=id)
            s.delete()
            msg={'status':True,'message':"Comment Deleted Successfully"}
            jsonData=JSONRenderer().render(msg)
            return HttpResponse(jsonData,content_type="application/json")


#Like Sections
@csrf_exempt
def addLike_SectionMember(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        l=member_Story.objects.get(id=id)
        l.like_count+=1
        l.save()

        msg = {"result":"Done","message":"Like Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")


@csrf_exempt
def minusLike_SectionMember(Request):
    if Request.method=="POST":
        id=Request.POST.get('id')
        l=member_Story.objects.get(id=id)
        l.like_count-=1
        l.save()

        msg = {"result":"Done","message":"Like Added Successfuly !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")

@csrf_exempt
def addPustika(Request):
    if Request.method=="POST":
        s=Pustika()
        s.file=Request.FILES.get('file')
        if(s.file):
           s.save()
           msg = {"result":"Done","message":"Pustika Added Successfuly !!!"}
        else:
            msg = {"result":"Fail","message":"Please Select a Pustika !!!"}
        responseMessage = JSONRenderer().render(msg)
        return HttpResponse(responseMessage,content_type="application/json")
 

@csrf_exempt
def viewPustika(Request):
    try:
        data = Pustika.objects.all().order_by('id').reverse()
        dataSerializer = PustikaSerializer(data,many=True)
        realData={'status':True,'message':"Pustika got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":"Fail","message":"Pustika Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")



@csrf_exempt
def viewAdminNotification(Request):
    try:
        data = Member_Login_Notification.objects.all().order_by('id').reverse()
        dataSerializer = Member_Login_NotificationSerializer(data,many=True)
        realData={'status':True,'message':"Member Login Notification got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":False,"message":"Member Login Notification Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")



@csrf_exempt
def viewMemberNotification(Request):
    try:
        data = Notification_For_Member.objects.all().order_by('id').reverse()
        dataSerializer = Notification_For_MemberSerializer(data,many=True)
        realData={'status':True,'message':"Member Notification got Successfully ",'data':dataSerializer.data}
        return HttpResponse(json.dumps(realData),content_type="application/json")

    except:
        msg = {"result":False,"message":"Member Notification Not Found"}
    jsonData = JSONRenderer().render(msg)
    return HttpResponse(jsonData,content_type="application/json")
