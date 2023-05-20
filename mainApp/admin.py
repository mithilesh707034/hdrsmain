from django.contrib import admin
from .models import *

admin.site.register((Member,member_Story,admin_Story,Donation,Slider,FutureEvent,Comment_Section,Comment_SectionMember,Pustika,Member_Login_Notification,Notification_For_Member))
