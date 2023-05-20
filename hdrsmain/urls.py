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
    path('update-member-profile/',views.updateMemberProfile),
    path('update-member-status/',views.updateMemberStatus),
    path('add-story/',views.addStory),
    path('view-story/',views.viewStory),
    path('view-single-member-story/',views.viewSingleMemberStory),
    path('update-member-story/',views.updateMemberStory),
    path('delete-member-story/<int:id>/',views.deleteMemberStory),
    path('add-admin-story/',views.addAdminStory),
    path('view-admin-story/',views.viewAdminStory),
    path('update-admin-story/',views.updateAdminStory),
    path('update-member-story-status/',views.updateMemberStoryStatus),
    path('delete-admin-story/<int:id>/',views.deleteAdminStory),

    path('add-donation/',views.addDonation),
    path('view-donation/',views.viewDonation),
    path('view-single-donation/',views.viewSingleDonation),

    path('add-slider/',views.addSlider),
    path('update-slider/',views.updateSlider),
    path('view-slider/',views.viewSlider),
    path('delete-slider/<int:id>/',views.deleteSlider),
    path('add-future-event/',views.addFutureEvent),
    path('view-future-event/',views.viewFutureEvent),
    path('update-future-event/',views.updateFutureEvent),
    path('delete-future-event/',views.deleteFutureEvent),
    path('get-all-member/',views.getAllMember),
    path('view-member-profile/',views.memberProfile),

    #Admin
    path('add-comment/',views.addComment_Section),
    path('view-comment/',views.viewComment_Section),
    path('update-comment/',views.updateComment_Section),
    path('delete-comment/',views.deleteComment_Section),
    path('plus-like/',views.addLike_Section),
    path('minus-like/',views.minusLike_Section),
    
    #Member
    path('add-member-comment/',views.addComment_SectionMember),
    path('view-member-comment/',views.viewComment_SectionMember),
    path('update-member-comment/',views.updateComment_SectionMember),
    path('delete-member-comment/',views.deleteComment_SectionMember),
    path('plus-member-like/',views.addLike_SectionMember),
    path('minus-member-like/',views.minusLike_SectionMember),

    #Pustika
    path('add-pustika/',views.addPustika),
    path('view-pustika/',views.viewPustika),

    #Member Registered Notification 
    path('member-register-notification/',views.viewAdminNotification),

    #Member Registered Notification 
    path('member-notification/',views.viewMemberNotification),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    