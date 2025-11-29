from django.db import models

class University(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='universities/', null=True, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Group(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.university.name} - {self.name}"

class Student(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='students_photos/', blank=True, null=True)  # <-- qo'shildi

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
