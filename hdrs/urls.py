from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-login/',views.adminLogin),
    path('register-member/',views.registerMember),
    path('member-login/',views.memberLogin),
    path('update-member-status/',views.updateMemberStatus),
    path('add-story/',views.addStory),
    path('view-story/',views.viewStory),
    path('update-member-story/<int:id>/',views.updateMemberStory),
    path('delete-member-story/<int:id>/',views.deleteMemberStory),
    path('add-admin-story/',views.addAdminStory),
    path('view-admin-story/',views.viewAdminStory),
    path('update-admin-story/<int:id>/',views.updateAdminStory),
    path('delete-admin-story/<int:id>/',views.deleteAdminStory),
    path('add-donation/',views.addDonation),
    path('view-donation/',views.viewDonation),
    path('add-slider/',views.addSlider),
    path('view-slider/',views.viewSlider),
    path('delete-slider/<int:id>/',views.deleteSlider),
    path('add-future-event/',views.addFutureEvent),
    path('view-future-event/',views.viewFutureEvent),
    path('get-all-member/',views.getAllMember),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    