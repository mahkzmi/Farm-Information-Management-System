from django.db import models

class Field(models.Model):
    name = models.CharField(max_length=100)
    area = models.FloatField(help_text="مساحت زمین به هکتار")
    soil_type = models.CharField(max_length=100, help_text="نوع خاک")
    planting_date = models.DateField(help_text="تاریخ کشت")

    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=100)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='crops')
    planting_date = models.DateField()
    harvest_date = models.DateField()
    yield_amount = models.FloatField(help_text="مقدار تولید به تن")

    def __str__(self):
        return f"{self.name} ({self.field.name})"

class Activity(models.Model):
    ACTIVITY_TYPES = [
        ('IR', 'آبیاری'),
        ('FE', 'کوددهی'),
        ('SP', 'سمپاشی'),
    ]
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=2, choices=ACTIVITY_TYPES)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"{self.get_activity_type_display()} on {self.field.name} ({self.date})"