from django.shortcuts import render, redirect
from .models import Field, Crop, Activity
from .forms import FieldForm, CropForm, ActivityForm


def field_list(request):
    fields = Field.objects.all()
    return render(request, 'farm/field_list.html', {'fields': fields})

def crop_list(request, field_id):
    field = Field.objects.get(id=field_id)
    crops = field.crops.all()
    return render(request, 'farm/crop_list.html', {'field': field, 'crops': crops})

def activity_list(request, field_id):
    field = Field.objects.get(id=field_id)
    activities = field.activities.all()
    return render(request, 'farm/activity_list.html', {'field': field, 'activities': activities})

def add_field(request):
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_list')
    else:
        form = FieldForm()
    return render(request, 'farm/add_field.html', {'form': form})

def add_crop(request):
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_list')
    else:
        form = CropForm()
    return render(request, 'farm/add_crop.html', {'form': form})

def add_activity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field_list')
    else:
        form = ActivityForm()
    return render(request, 'farm/add_activity.html', {'form': form})

def home(request):
    return render(request, 'farm/home.html')