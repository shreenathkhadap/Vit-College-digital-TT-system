from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def tp(request):
    #########################B############################
    ds="https://meet.google.com/pqx-oxnw-pwk?authuser=0"
    
    return render(request, 'tp.html',{'ds':ds})
def notes(request):
    
    return render(request, 'notes.html')
def chats(request):
    return render(request, 'chats.html')