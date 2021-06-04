from .tests import NewMeetingForm
from django.shortcuts import render, get_object_or_404
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, MeetingMinutesForm, ResourceForm, EventForm

# Create your views here.
def index(request):
    return render(request, 'club/index.html')

def resources(request):
    resource_list=Resource.objects.all()
    return render(request, 'club/resources.html', {'resource_list' : resource_list})

def meetings(request):
    meeting_list=Meeting.objects.all()
    return render(request, 'club/meetings.html', {'meeting_list' : meeting_list})
def meetingDetail(request, id):
    meeting=get_object_or_404(Meeting, pk=id)
    return render(request, 'club/meetingdetail.html', {'meeting' : meeting})

def newMeeting(request):
    form=MeetingForm

    if request.method=='POST':
        form=MeetingForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingForm()
    else:
        form=MeetingForm()
    return render(request, 'club/newmeeting.html', {'form': form})

def newMeetingMinutes(request):
    form=MeetingMinutesForm

    if request.method=='POST':
        form=MeetingMinutesForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=MeetingMinutesForm()
    else:
        form=MeetingMinutesForm()
    return render(request, 'club/newmeetingminutes.html', {'form': form})

def newResource(request):
    form=ResourceForm

    if request.method=='POST':
        form=ResourceForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ResourceForm()
    else:
        form=ResourceForm()
    return render(request, 'club/newresource.html', {'form': form})

def newEvent(request):
    form=EventForm

    if request.method=='POST':
        form=EventForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=EventForm()
    else:
        form=EventForm()
    return render(request, 'club/newevent.html', {'form' : form})