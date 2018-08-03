# Profile's REST api

rest api providing basic functionality for managing user profiles.

##  Django REST Api project with Udemy
1- How to use vagrant?
 - navigatge to the project folder. then say:    vagrant init.
- then we copy this custom vagrant file and paste it in the default vagrant file being made by the previous step.
this file can be used for any django project. this is the link:
 https://raw.githubusercontent.com/LondonAppDev/course-rest-api/master/Vagrantfile
- this version of ubuntu :
config.vm.box = "ubuntu/xenial64"
is the same version this guy uses on his production linux server and he uses the same thing for development server in order to have a smooth push to live.
- config.vm.provision section of the vagrant file contains all we need to be done at the first run of the server.
- vagrant up    ===> will run the server installed on the project directory.
- then in order to connect to the linux server made by vagrant we just need to say:  vagrant ssh
- also in order to exit the server we say: exit
- when we connect to the server, we ca see all our files being copies to a folder called /vagrant.  we can cd /vagrant
and then ls shows all our project files. if we say ls -a it shows all files including hidden files.
- all the changes on the computer will be connected live to the vagrant server and we can see the changes in vagrant.
- for example we can run any py file from vagrant by simply typing: python <file_name>.py
- now in order to be able to have different projects on our vagrant box, we need to make virtual environment for each project.
- we need to run this on our vagrant: mkvirtualenv profiles_api --python=python3
- (profiles_api) vagrant@ubuntu-xenial:~$     --> this is the environment we connect to, (profiles_api is the name of the
virtual env we made) so all the packages we install, would be only installed for this project.
- in order to turn it off, we say deactivate. then we get out of the current virtual env.
- if we need to get back to the vartual env, we say : workon <virtualenv_name>
sometimes workon doesnt work. we need to run thiscd .. before it:
source /usr/local/bin/virtualenvwrapper.sh

------------------------------
## creating a django app
let's install python libraries needed:
- pip install django==1.11
-  pip installdjangorestframework==3.6.2
now we make a src folder in project root and navigate to it (cd /vagrant/src) then run:
django-admin.py startproject <project_name>
- now we navigate to the project folder and run:  python manage.py startapp <app_name>
now we have to navigate to setting and under installed_apps add 3 lines:
'rest_framework',
    'rest_framework.authotoken',
    'profiles_api',
-- it is a good idea to add a requirements.txt file that explains all requriements with their versions for future use.
for mking this requirements file we can do this:
    *  pip freeze: shows all packages installed so far.
 in order to make that file we just say : pip freeze > requirements.txt
   now we can run the server:  python manage.py runserver 0.0.0.0:8080   we have to be inside the project folder under src.
0.0.0.0 means any ip.
so it all worked and we are ready for the next part.
------------------------------------------
Django:
-------------------------
##  Django REST Api project with Udemy
## part 7: Set up Django admin

-------------------------
# Profile's REST api

rest api providing basic functionality for managing user profiles.

##  Django REST Api project with Udemy
1- How to use vagrant?
 - navigatge to the project folder. then say:    vagrant init.
- then we copy this custom vagrant file and paste it in the default vagrant file being made by the previous step.
this file can be used for any django project. this is the link:
 https://raw.githubusercontent.com/LondonAppDev/course-rest-api/master/Vagrantfile
- this version of ubuntu :
config.vm.box = "ubuntu/xenial64"
is the same version this guy uses on his production linux server and he uses the same thing for development server in order to have a smooth push to live.
- config.vm.provision section of the vagrant file contains all we need to be done at the first run of the server.
- vagrant up    ===> will run the server installed on the project directory.
- then in order to connect to the linux server made by vagrant we just need to say:  vagrant ssh
- also in order to exit the server we say: exit
- when we connect to the server, we ca see all our files being copies to a folder called /vagrant.  we can cd /vagrant
and then ls shows all our project files. if we say ls -a it shows all files including hidden files.
- all the changes on the computer will be connected live to the vagrant server and we can see the changes in vagrant.
- for example we can run any py file from vagrant by simply typing: python <file_name>.py
- now in order to be able to have different projects on our vagrant box, we need to make virtual environment for each project.
- we need to run this on our vagrant: mkvirtualenv profiles_api --python=python3
- (profiles_api) vagrant@ubuntu-xenial:~$     --> this is the environment we connect to, (profiles_api is the name of the
virtual env we made) so all the packages we install, would be only installed for this project.
- in order to turn it off, we say deactivate. then we get out of the current virtual env.
- if we need to get back to the vartual env, we say : workon <virtualenv_name>
sometimes workon doesnt work. we need to run this before it:
source /usr/local/bin/virtualenvwrapper.sh

------------------------------
## creating a django app
let's install python libraries needed:
- pip install django==1.11
-  pip installdjangorestframework==3.6.2
now we make a src folder in project root and navigate to it (cd /vagrant/src) then run:
django-admin.py startproject <project_name>
- now we navigate to the project folder and run:  python manage.py startapp <app_name>
now we have to navigate to setting and under installed_apps add 3 lines:
'rest_framework',
    'rest_framework.authotoken',
    'profiles_api',
-- it is a good idea to add a requirements.txt file that explains all requriements with their versions for future use.
for mking this requirements file we can do this:
    *  pip freeze: shows all packages installed so far.
 in order to make that file we just say : pip freeze > requirements.txt
   now we can run the server:  python manage.py runserver 0.0.0.0:8080   we have to be inside the project folder under src.
0.0.0.0 means any ip.
so it all worked and we are ready for the next part.

------------------------------------------
## 6- database setup:
making user model:
- in models.py we import:  
from django.contrlib.auth.models import AbstractBaseUser
from django.contrlib.auth.models import PermissionsMixin
- then we make UserProfile class and inherit it from both libraries we imported. 
- then we need to define the fields.
after defining all fields. we add this:  object = UserProfileManager()
then we need to define the following":
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = ['name']     ==> becuase email is chosen as username filed, it doesnt need to be mentioned here. 
then we use some helper functions such as :   get_full_name() and get_short_name() and __str__(self) which is used to define the string representation of the object.
------
now we need to define user profile manager behavior. 
first import : from django.contrlib.auth.models import BaseUserManager
then we define a class called UserProfileManager(BaseUserManager)  and inherits from BaseUserManager
- then we define this function to write the logic of creating a new user:  create_user()
in this function we say if there is no email prvided, go ahead and send an error message. 
and also normalize the email (make all letters into lowercase)
 then it defines a user, sets the password and saves the user in the predefined database for this model. 
- another function we need to have is to create the super user. and we just need to change 2 fields (is_staff, and is_superuser to True) and then save it and return it.
- in order to override the default user model, with custom user model we need to add this: AUTH_USER_MODEL = 'profiles_api.UserProfile'  to the end of
setting.py under the main root. 
- now we are all set to connect to the vagrant box and the virtual env we work on. then run : python manage.py makemigrations 
also python manage.py migrate

-----------------------------------------
## part 7: Set up Django admin
now we need to create a superuser. again we connect to vagrant virtualbox and navigate to /vagrant/src/profiles_project  and type: python manage.py createsuperuser.
then it asks for credentials. after doing this we need to register models in admin.py like this:
from . import models
admin.site.register(models.<model_name>)  <model_name> = UserProfile
then we are ready to login to the admin panel. we just run: profiles_project$ python manage.py runserver 0.0.0.0:8080

------------------------------------------
## part 8: Intro to API views
django has 2 methods of making api endpoints. 
1) APIView
2) Viewset
we work on APIView
what is the api view?  an api view allows us to define functions that matches the standard HTTP methods.
GET: to view thw item
POST: to add items
PUT: to edit items
PATCH: to partially edit items
DELETE: to delete items
When we use APIView:
- we need the full control over the logic.
- processing files and rendering a synchronous response.
- calling other apis/services.
- accessing local files or data.
----
now we can start. we get to the app folder(profiles_api) and open views.py
we can make the logic that django runs when the visitor sends a request to the api endpoint.
- from rest_framework we should import 2 libraries. 
from rest_framework.views import APIView
from rest_framework.response import Response
- now inside view.py we should define a class and inherit from self, request, format=None)
and then we need to define get method in it. inside the get method we define a list with some items. 
and return the response that returns the list we made. 

----
now we made the view and we need to map a url to it to be able to send get requests to it. 
for this we go to <main_project_folder>/urls.py and import this: from django.conf.urls import include
- now we add this url :  url(r'^api/', include('profiles_api.urls'))
this technlogy is called django url dispatcher. https://docs.djangoproject.com/en/2.0/topics/http/urls/
now we need to make the app's url.py file. which is 'profiles_api.urls.
in the new file we import url and views and define url patterns to say which view loads when the sepcific url is called. 
from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^hello-view/', views.HelloApiView.as_view()),
]

now when we go to this url:   /api/hello-view it fetches the list we defined in our HelloApiView class.

---
serailzer object: it is an object in django rest framework that we can use to describe the data that we need to return or retrive from our api.
it converts json data to python objects and vice versa.
we need to make a new file for all serializers called serializers.py and iside it we can define the serializers as different classes. 
from rest_framework import serializers
class HelloSerializer(serializers.Serializer)
    """Serializes a name field for testing ou APIView"""
    name = serializers.CharField(max_length=10)

---
 now we need to add the serializer we made to the view. 
we should import the serializers file in views  ==> form . import serializers
also we need to import the status codes from rest frame work (404,500,200,etc.)  from rest_framework import status
- then in order to link the view with the serializer we made we add this; serializer_class = serializers.HelloSerializer
it says to django that serializer_class is an instance of HelloSerializer class. 
- now we can make post request to the api view. 
like this:
def post(self, request):
        """create a hello message with our name"""
        serializer = serializers.HelloSerializer(data=request.data)
        # data validation
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

the {0} simply returns:  Hello 'moji'  ==> (if the name is moji)  ==> link: https://docs.python.org/3/library/string.html#formatstrings

-----
we tested POST Api by runnig this url:  http://127.0.0.1:8080/api/hello-view/  and it added a place under the page to post a name on the api. 

-----
now we can add put function. by defining new function in view.py and inheriting selt, request and pk=None (Pk=primary key) and return a simple response saying the name of the method: 
def put(self, request, pk=None):
        """Handles Updating an Object"""
        return Response({'method': 'put'})
we do exactly the same for patch and delete methods.
Now we are all good for part 9.

-------------------------
## part 9:
in this part we learn Viewsets.
Viewsets use common api object actions like:  
List: for getting the list of objects.
Create: for creating an object.
Retrieve: for getting a specific object.
Update: for updating an object.
Partial Update: for updating a part of an object.
Destroy: for deleting an object.
Viewsets take care of typical logic for us:
- perfect for standard database operations.
- fastest way to create database interface.
when we may better use Viewsets?
   - for creating a crud interface.
   - for making a quick and simple api 
   - when we dont need customization on the logic. 
  - when the api works with standard data structure.

----
now we make a basic Hello viewsets app.  
first we need to import it to views.py:     from rest_framework import viewsets
- then we can make the class HelloViewSet() and inherit it from viewsets.ViewSet
then we will make the functions for each action (list, create, etc.)
viewset class has its own router from rest_framework. but the first method viewsapi doesnt have that. 
- in order to use this functionality we need to import the following classes to url.py:
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
and then we instantiate a new DefaultRouter 
and register it.. 
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
- then we include this:  url(r'', include(router.urls))  to the url patterns
now the api page is ready to test and the list function works. (http://127.0.0.1:8080/api/hello-viewset/)

----
we need a serializer also for this method and we can use the same one we made for the prevoious method.


## part 10:
Making the main profiles app:
- we need to make Model Serializers.   Model serializer is similar to what we made before but its meant to be used for models.
- we make a new class in serializers.py named UserProfileSerializer()
and inside of it on the top we make a Meta class.
inside meta class we tell django what model we want to use also which fields we are going to use./
- then we have to say password should be write only. 
then we need to define the create method to add a new user. 
---
- now we need to import all models at views.py
-then we need to get to views.py and add a new class called UserProfileViewSet() and inherit it from viewsets.ModelViewSet that takes care of all logic behind creating, reading and updating users.
- inside it we add serializer we made and also the qurybuilder that pulls all the model records.
----
now we have to register a url for the viewset. we need to register a new router. and since we use the model, we don't need to specify the base_name. django will do it itself.
----
now we have to make permissions for our api because currently anyone can edit data for anyone. 
- we make a new file called permissions.py under profiles_app folder.
- permissions are inside permissions under rest_framework.
so we import it first. then we define a class to return a True/False if the user has permission or not. 
- inside this function we tell django to return a true if the request sent to the api is a Safe method (get or just reading data)
- if the request is not safe it means the user wants to send Post, Put, Patch or Delete methods.
this line:  return obj.id == request.user.id     can check if the object user is trying to change equals the authenticated user id or not. 
so in this function has_object_permission()   we said if the user wants to change any data and they are not authrnticated return false otherwise true.
---
now we should add authentication logic to the views.py
first we import permissions. from . import permissions.
then we need to import this:
from rest_framework.authentication import TokenAuthentication
then at the end of class UserProfileViewSet we add this as a tuple. the , at the end tells django it is a tuple.
authentication_classes = (TokenAuthentication,)
then we add: permission_classes = (permissions.UpdateOwnProfile,)   
the reason we sue tuples is we say that we can have more than one permissions classes in a viewset.
---
in order to have search functionality we can add from rest_framework import filters to the top of views.py
then we add these 2 lines at the very end of UserProfileViewSet
filter_backends = (filters.SearchFilter,)
    search_fields = ('name','email',)
----

## part 10: Create login api
first in view.py we import these:
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
- then we need to define a class called LoginViewSet to view.py that checks the email and generates auth token. 
- then we should add a router for this class.  (urls.py)
router.register('login', views.LoginViewSet, base_name='login')
---
using the api view we can now see on the website that login api has been made and it successfully generates token. 
---









 