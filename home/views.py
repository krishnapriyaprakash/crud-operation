from django.shortcuts import render, redirect,HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import tour  


def index(request):
    return render(request, 'index.html')
def edit1(request):
    data ={
        'data' :tour.objects.all()

    }    
    return render(request,'contact.html',data)  

  
def insert(request):
    if request.method == 'POST':
        
        print("Form data received:", request.POST)
        name = request.POST.get('name')
        age = request.POST.get('age')
        place = request.POST.get('place')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        food_option = request.POST.get('food_option')

        query = tour(
                name=name,
                age=age,
                place=place,
                amount=amount,
                date=date,
                contact=contact,
                email=email,
                food_option=food_option
            )
        query.save() 
        return HttpResponse(f'<script>alert("File Added successfully!"); window.location.href = "/";</script>')
        return redirect("/") 
def view(request):
    data={
        "data":tour.objects.all()
        }
    return render(request,'view.html',data)

def delete(request,id):
    dlt=tour.objects.get(id=id)
    dlt.delete()
    return HttpResponse(f'<script>alert("File Deleted successfully!"); window.location.href = "/";</script>')
    return redirect("/")  


def edit2(request, id):
    data = get_object_or_404(tour, id=id)  # Safely retrieve the employee or return 404
    return render(request, 'update.html', {'data': data}) 

def contact(request):
    return render(request, 'contact.html')

def update(request, id):

    data = get_object_or_404(tour, id=id)

    if request.method == "POST":
        # Retrieve the data from the form
        name = request.POST.get('name')
        age = request.POST.get('age')
        place = request.POST.get('place')
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        food_option = request.POST.get('food_option')

        # Get the tour object by id and update the fields
        edit = tour.objects.get(id=id)
        edit.name = name
        edit.age = age
        edit.place = place
        edit.amount = amount
        edit.date = date
        edit.contact = contact
        edit.email = email
        edit.food_option = food_option

        # Save the updated object
        edit.save()
        return HttpResponse(f'<script>alert("File Edited successfully!"); window.location.href = "/";</script>')
        # Redirect to home page after saving
        return redirect("/")
    return render(request, 'update.html', {'data': data})

