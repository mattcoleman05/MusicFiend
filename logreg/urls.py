from django.urls import path
from .import views
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
 
    path('', views.index),
    path('login', views.login),
    path('signup', views.signup),
    path('signuppage', views.signuppage),
    path('mainpage', views.mainpage),
    path('artistpage/<int:id>', views.artistpage),
    path('editartist/<int:id>', views.editpage),
    path('update_artist', views.update_artist),
    path('create', views.create),
    path('image_upload', views.artist_image_view, name = 'image_upload'), 
    path('success', views.success, name = 'success'), 
    path('logout', views.logout)



]

if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 