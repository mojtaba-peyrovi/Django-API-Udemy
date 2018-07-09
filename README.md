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
