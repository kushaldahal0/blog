from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views
app_name = 'home'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index,name='index'),
    path("contact/", views.contact,name='contact'),
    path("login/", views.plogin,name='login'),
    path("signup/", views.psignup,name='signup'),
    path("logout/", views.plogout, name='logout'),

]
