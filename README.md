# Farm Information Management System

## Overview
The **Farm Information Management System** is a web application built using **Django** that allows users to manage agricultural fields, crops, and activities. It provides a user-friendly interface for adding, viewing, and managing farm-related data without requiring access to the admin panel. This system is designed to help farmers and agricultural experts efficiently organize and track their farming operations.

---

## Features
1. **Field Management**: Add and manage agricultural fields with details like name, area, soil type, and planting date.
2. **Crop Management**: Add and manage crops with details like name, planting date, harvest date, and yield amount.
3. **Activity Management**: Add and manage activities such as irrigation, fertilization, and spraying.
4. **User-Friendly Forms**: Allow users to add fields, crops, and activities through simple forms.
5. **Data Visualization**: View lists of fields, crops, and activities in an organized manner.

---

## Technologies Used
- **Python**: Primary programming language.
- **Django**: Web framework for backend development.
- **SQLite/PostgreSQL**: Database for storing farm data.
- **HTML/CSS**: Frontend templates for user interface.

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/farm-management-system.git
cd farm-management-system
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
- For SQLite (default): No additional setup is required.
- For PostgreSQL: Update the `settings.py` file with your database credentials:
  ```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'your_db_name',
          'USER': 'your_db_user',
          'PASSWORD': 'your_db_password',
          'HOST': 'localhost',
          'PORT': '5432',
      }
  }
  ```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser (Admin)
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

### 8. Access the Application
- Open your browser and go to `http://127.0.0.1:8000/`.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage data.

---

## Usage

### 1. Adding Fields
- Navigate to `http://127.0.0.1:8000/add-field/`.
- Fill out the form to add a new field.

### 2. Adding Crops
- Navigate to `http://127.0.0.1:8000/add-crop/`.
- Fill out the form to add a new crop.

### 3. Adding Activities
- Navigate to `http://127.0.0.1:8000/add-activity/`.
- Fill out the form to add a new activity.

### 4. Viewing Data
- View all fields at `http://127.0.0.1:8000/fields/`.
- Click on a field to view its crops and activities.

---

## Project Structure
```
farm-management-system/
├── manage.py
├── requirements.txt
├── farm_management/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── farm/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── templates/
│   │   ├── field_list.html
│   │   ├── crop_list.html
│   │   ├── activity_list.html
│   │   ├── add_field.html
│   │   ├── add_crop.html
│   │   └── add_activity.html
│   └── ...
```

---

## Code Examples

### Models
```python
from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100)
    area = models.FloatField(help_text="Area in hectares")
    soil_type = models.CharField(max_length=100, help_text="Soil type")
    planting_date = models.DateField(help_text="Planting date")

    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=100)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='crops')
    planting_date = models.DateField()
    harvest_date = models.DateField()
    yield_amount = models.FloatField(help_text="Yield in tons")

    def __str__(self):
        return f"{self.name} ({self.field.name})"

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('IR', 'Irrigation'),
        ('FE', 'Fertilization'),
        ('SP', 'Spraying'),
    ]
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=2, choices=ACTIVITY_TYPES)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.get_activity_type_display()} on {self.field.name} ({self.date})"
```

### Forms
```python
from django import forms
from .models import Field, Crop, Activity

class FieldForm(forms.ModelForm):
    class Meta:
        model = Field
        fields = ['name', 'area', 'soil_type', 'planting_date']
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'field', 'planting_date', 'harvest_date', 'yield_amount']
        widgets = {
            'planting_date': forms.DateInput(attrs={'type': 'date'}),
            'harvest_date': forms.DateInput(attrs={'type': 'date'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['field', 'activity_type', 'date', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
```

### Views
```python
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
```

---

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact
For any questions or suggestions, feel free to reach out:
- **Email**: mah.kzmi21@gmail.com
- **GitHub**: [mahkzmi](https://github.com/mahkzmi)

---

Thank you for checking out the **Farm Information Management System**! 🌱🚜
