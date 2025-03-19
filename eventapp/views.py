from django.shortcuts import redirect, render
from .models import Event
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request, 'booking.html', dict_form)

def events(request):
    dict_eve ={
        'eve': Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)