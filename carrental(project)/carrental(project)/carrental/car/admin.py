from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import contactQ    
class contactQmodel(admin.ModelAdmin):
    list_display=('name','useremail','phone_number','date','msg') 
from .models import veriform
class veriformmodel(admin.ModelAdmin):
    list_display=('id','name','email','phone','DLFI','DLBI','Add','IDproof','Addproof','is_verified','status')  
    list_editable = ('is_verified',)  # Allow editing is_verified directly in the admin list view
from .models import postVcl
class postVclmodel(admin.ModelAdmin):
    list_display=('car_id','vehicle_title','brand','PPD','fuel','model_year','setting','VO','img1','img2','img3','is_booked')   
from .models import Booking
class Bookingmodel(admin.ModelAdmin):
        list_display=('car','start','end','user','razorpay_payment_id','payment_status','amount','created_at','razorpay_order_id')   

# Register your models here.
admin.site.register(contactQ)
admin.site.register(postVcl) 
admin.site.register(Booking)  
admin.site.register(veriform, veriformmodel)

from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    # Specify the fields to display in the admin
    list_display = ('email', 'full_name','phone_number', 'is_staff')
    search_fields = ('email', 'full_name' , 'phone_number')
    ordering = ('email',)

    # Customize the fieldsets for the add/edit user pages
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('full_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number','full_name'),
        }),
    )

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)