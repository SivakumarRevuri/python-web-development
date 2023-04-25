from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

# rooms = [
#     {'id': 1, 'name': 'Lets learn python'},
#     {'id': 2, 'name': 'Lets learn Django'},
#     {'id': 3, 'name': 'Lets learn Flask'},
#     {'id': 4, 'name': 'Lets learn MongoDB'},
# ]


def login_page(request):
    return render(request, 'base/login_register.html', context= {})


# Create your views here.
def home(request):
    # searching the topics
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    print(q)
    rooms = Room.objects.filter(topic__name=q)
    topics = Topic.objects.all()
    
    context = {'rooms': rooms, 'topics': topics}
    return render(request, 'base/home.html', context = context)

def hello_world(request):
    return render(request, 'base/hello.html')


def room(request, pk):
    # room = None
    # model_rooms = Room.objects.all()
    # data = {}
    # key = 1
    # for i in model_rooms:
    #     data[key] = i
    #     key += 1
    room = Room.objects.get(id = pk)
    context = {'rooms': room}
    return render(request, 'base/room.html', context=context)

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context= context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room) # gives you a empty form 
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    return render(request, 'base/room_form.html', context = {'form': form})


def delete_room(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', context={'obj': room})
