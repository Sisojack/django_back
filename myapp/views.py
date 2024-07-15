from django.shortcuts import render
from . models import People

# Create your views here.
def index(request):
    if request.method=='POST':
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        age = request.POST.get('age')

        #create an object
        new_person= People(first_name= first_name, last_name= last_name, email=email, age=age)
        new_person.save()

        #get all Persons
    people= People.objects.all()
    return render(request, 'index.html', {'people':people})