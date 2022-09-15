Good Evening Sir,

thanks for the giving this opportunity and for reviewing my assignment.

As the requirements given are so clear,

so my  first step is to analyse the flow for that i used a flow chart,what are the methods need to implement.

Then i come up the three methods.

1.login

2.logout

3.weatherapi

as clearly mentioned i have to use authorization mode for 2 and 3 method.

For that i refered token authentication in django.

And some basic validations.

So first api is now over

in logout api we need to delete the generated and assigned token here only validaion is to check the token.

So the final api which is weather information api.

We need to create a model to store those information and a serializers for convering objects into readable formats.

For that we need around 30 city names for that i fetched a json data from openweathermap.org.

With that json extracted only the required fields using indexing.

Then using the city names which i extrated from json i made a api call to weatherapi and recored all   obervations in the respective models.

Then the next requirement is to paginate those fetched weather information.

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
