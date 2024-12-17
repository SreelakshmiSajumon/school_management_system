from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Office Staff'),
        ('librarian', 'Librarian'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return self.username

class Student(models.Model):
    name = models.CharField(max_length=255)
    roll_number = models.CharField(max_length=50, unique=True)
    class_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LibraryHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='library_records')
    book_name = models.CharField(max_length=255)
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.book_name} - {self.status}"
    
class FeesHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees_records')
    fee_type = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    remarks = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.fee_type} - {self.amount}"


class LibraryRecord(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Issued', 'Issued'),
    ]

    book_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return self.book_name

