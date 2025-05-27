from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
  
class contactQ(models.Model):
  name=models.CharField(max_length=50)
  useremail=models.EmailField(max_length=100)
  phone_number = models.IntegerField()
  date=models.DateTimeField()
  msg=models.CharField(max_length=1000)
  
class postVcl(models.Model):
  vehicle_title=models.CharField(max_length=100)
  brand=models.CharField(max_length=50)
  PPD = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Set a default value
  fuel=models.CharField(max_length=15,default="Petrol")
  model_year=models.IntegerField()
  SETTING_CHOICES = [
    (5, '5'),
    (6, '6'),
    (7, '7'),
     ]
  setting = models.IntegerField(choices=SETTING_CHOICES, default=1) 
  VO=models.TextField()
  img1=models.ImageField(upload_to='myfile')
  img2=models.ImageField(upload_to='myfile',blank=True, null=True)
  img3=models.ImageField(upload_to='myfile',blank=True, null=True)
  is_booked = models.BooleanField(default=False)  # Add this field for availability tracking

def __str__(self):
        return f"{self.brand} {self.vehicle_title} ({self.model_year})"



class veriform(models.Model):
  name=models.CharField(max_length=20,null=False)
  email=models.CharField(max_length=50,null=False,unique=True)
  phone=models.IntegerField(null=False)
  Add=models.CharField(max_length=60,null=False)
  DLN=models.IntegerField(null=False)
  DLFI=models.FileField(upload_to='myfile',null= False)
  DLBI=models.FileField(upload_to='myfile', null =False)
  IDproof=models.IntegerField(null=False)
  Addproof=models.FileField(upload_to='myfile',null=False)
  is_verified = models.BooleanField(default=False)
  status = models.CharField(max_length=20, default="Pending")  # Status field

  def save(self, *args, **kwargs):
        if self.is_verified:
            self.status = "Approved"
        else:
            self.status = "Pending"
        super().save(*args, **kwargs)


# class Payment(models.Model):
#     customer = models.ForeignKey(registration, on_delete=models.CASCADE)
#     car = models.ForeignKey(postVcl, on_delete=models.CASCADE)
#     payment_status = models.CharField(max_length=50, choices=[('Paid', 'Paid'), ('Pending', 'Pending')])
#     payment_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.customer.name} - {self.car.vehicle_title} - {self.payment_status}"

# class Bookingtime(models.Model):
#    start=models.DateTimeField(null=False)
#    end=models.DateTimeField(null=False)
   
   
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True  # Ensure the user is active by default
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
class CustomUser(AbstractUser):
    username = None  # Remove username field
    email = models.EmailField(unique=True)  # Use email as the unique identifier
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_verified = models.BooleanField(default=False)  # Add this field

    objects = CustomUserManager() 

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  #


from django.db import models
from django.conf import settings

from django.db import models
from django.conf import settings
from car.models import postVcl  # Import the postVcl model

class Booking(models.Model):
    car = models.ForeignKey(postVcl, on_delete=models.CASCADE)  # Link to the car
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Link to the user
    start = models.DateTimeField()  # Start date of the booking
    end = models.DateTimeField()  # End date of the booking
    razorpay_order_id = models.CharField(max_length=255, unique=True)  # Razorpay order ID
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)  # Razorpay payment ID
    payment_status = models.CharField(max_length=20,default="Pending",)  # Payment status
    amount=models.DecimalField(max_digits=10,decimal_places=2,default=1)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of booking creation

    def __str__(self):
        return f"Booking {self.id} for {self.car.vehicle_title}"
    
    
