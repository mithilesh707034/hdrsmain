from django.contrib import admin
from .models import *

admin.site.register((Member,member_Story,admin_Story,Donation,Slider,FutureEvent))
