For that pagenumberpagination and serializers are used to paginate and convert objects into json formats.
Deployment:

I prefer ubuntu so my deployment steps to run this assignment

>apt install python3-pip

>apt install git

>pip3 install virtualenv

>mkdir Project_Folder_Name

>cd Project_Folder_Name

>python3.8 -m venv Virtual_Environmet_Name

>source Virtual_Environmet_Name/bin/activate

>git clone https://github.com/Vignesh-PyDev/Assignment_Infilect.git

>cd Assignment_Infilect

>cd Infilect_Weather_API_Assignment/


>pip3 install requirements.txt

>python3 manage.py makemigrations

>python3 manage.py migrate

>python3 manage.py createsuperuser

>python3 manage.py shell < Infilect/scripts.py

>python3 manage.py runserver

Test Api using Postman app 
 https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?hl=en
