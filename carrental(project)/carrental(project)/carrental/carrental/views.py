from django.http import HttpResponse 
from car.models import contactQ
from car.models import postVcl
from car.models import veriform
from car.models import Booking
from django.http import JsonResponse
from urllib.parse import unquote
import razorpay  
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.dateparse import parse_datetime
from django.shortcuts import render,get_object_or_404,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from django.contrib.auth.backends import ModelBackend  
from car.models import CustomUser  # Import your custom user model

def first(request):
    return HttpResponse("hii sam")
def second(request):
    return HttpResponse("hii samraddhi")
def index(request):
    data={'title':'myself',
         'list':['aa','bb'],
    # 'n ':'sam',
    # 'm':'b.tech',
    'dict':[{'n':'sam','m':'b.tech'},{'n':'sami','m':'m.tech'}]
    }
    return render(request,"index.html",data)

#-------------------ALL USER END PAGES (START)------------------------------------

def home(request):
    return render(request,"home.html")


from django.contrib.auth import login, authenticate
from django.contrib import messages

User = get_user_model()  # Get the custom user model

def homelogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        print(f"Login attempt: {email}")  # Debugging

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            print("User authenticated successfully!")  # Debugging
            return render( request,"homelogin.html",{"success": True})  # Rdirect to a protected page
        else:
            return render(request, "homelogin.html",{"error": "Invalid email or password"} )


    return render(request, "homelogin.html")
def layout(request):
    return render(request,"layout.html")


from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model

User = get_user_model()  # Get the custom user model

from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model  # ✅ Import get_user_model()
from django.urls import reverse

User = get_user_model()  # ✅ Use the custom user model

def registration_view(request):
    if request.method == "POST":
        print("POST request received")  # ✅ Debugging

        email = request.POST.get("useremail")
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")

        password = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password != password2:
            print("Passwords do not match")  # ✅ Debugging
            return render(request, "registration.html", {"error": "Passwords do not match"})

        if User.objects.filter(email=email).exists():
            print("Email already registered")  # ✅ Debugging
            return render(request, "registration.html", {"error": "Email already registered"})

        print("Creating user...")  # ✅ Debug before user creation

        # ✅ Fix: Create a user using the correct model
        my_user = CustomUser.objects.create_user(email=email, password=password,full_name=full_name,phone_number=phone_number)
        my_user.save()
        messages.success(request, "✅ Successfully registered!! Redirecting to login Page...")
        return redirect("registration_view")  

    return render(request, "registration.html")

def managereg(request):
    bata=CustomUser.objects.all()
    return render(request,"managereg.html",{'bata':bata})
    
    
def managebk(request):
    bata=Booking.objects.all()
    return render(request,"managebk.html",{'bata':bata})

def contact(request):
    return render(request,"contact.html")



def msgDL(request):
    return render(request,'msgDL.html')

def paystatus(request):
    # show = get_object_or_404(postVcl, id=id)
    # data=get_object_or_404(veriform,id=id)
     return render(request, "paystatus.html")#{'data': data, 'show': show})

def payment(request,id):
    show = get_object_or_404(postVcl, id=id)
    data=get_object_or_404(veriform,id=id)
    return render(request, "payment.html", {'data': data, 'show': show})

from django.shortcuts import render
from car.models import Booking


def verifyform(request):
    return render(request,'verifyform.html')




#-------------------ALL USER END PAGES (END)------------------------------------
#-------------------ALL ADMIN END PAGES (START)-----------------------------------

def admindash(request):
    return render(request,"admindash.html")

# def regdata(request):
#     show=registration.objects.all()
#     return render(request,"regdata.html",{'show':show})

def postvehicle(request):
    return render(request,"postvehicle.html")

from django.shortcuts import render, get_object_or_404

def car(request, car_id):
    car = get_object_or_404(postVcl, id=car_id)
    start = request.session.get("start")
    end = request.session.get("end")
    amount = request.session.get("amount")
    # num_days = request.session.get("num_days", 1)
    # if num_days is None:
    #     num_days = 1  # Default to 1 if not in session



    user_logged_in = request.user.is_authenticated
    user_verified = False  # Default

    if user_logged_in:
        print("Logged-in user email:", request.user.email)  # Debugging
        
        verification = veriform.objects.filter(email__iexact=request.user.email).first()
        
        if verification:
            print("Verification record found:", verification)
            user_verified = verification.is_verified  # Fetch verification status

    context = {
        'car': car,
        'user_logged_in': user_logged_in,
        'user_verified': user_verified,
        'start': start,
        'end': end,
        'amount': amount,
       
    }

    return render(request, 'car.html', context)

def vehiclemanage(request):
    data=postVcl.objects.all()
    return render(request,"vehiclemanage.html",{'data':data})

def manageCQ(request):
    bata=contactQ.objects.all()
    return render(request,"manageCQ.html",{'bata':bata})
    

def user_verify(request,email):  # Ensure the parameter is named 'id'
    verifing = get_object_or_404(verifing, email=email)
    return render(request, 'user_verify.html',{'verifing':verifing})

@login_required
def verify(request, email):  # Accept email as a parameter
    user = get_object_or_404(veriform, email=email)  # Fetch the user by email
    return render(request, 'verify.html', {'verify': user})  # Pass the user object to the template

def logout(request):
  request.session.flush()
  return redirect('home')    


#-------------------ALL ADMIN END PAGES (END)-----------------------------------

#---------==---------ALL SAVES METHOD(START)--------------------------------------

def savepost_v(request):
    if request.method=="POST":
        id=request.POST.get("id")
        vehicle_title=request.POST.get("vehicle_title")
        brand=request.POST.get("brand")
        ppd=request.POST.get("ppd")
        fuel=request.POST.get("ftype")
        if not fuel:  # If empty, return an error
            return render(request, "postvehicle.html", {"error": "Fuel type is required!"})
        model_year=request.POST.get("myear")
        sitting=request.POST.get("sc")
        vo=request.POST.get("vo")
        img1=request.FILES.get("img1")
        img2=request.FILES.get("img2")
        img3=request.FILES.get("img3")
        b=postVcl.objects.create(id=id,vehicle_title=vehicle_title,brand=brand,PPD=ppd,fuel=fuel,model_year=model_year,setting=sitting,VO=vo,img1=img1,img2=img2,img3=img3)
        b.save()
    return render(request,"postvehicle.html")

def savecontact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        useremail=request.POST.get('useremail')
        phone_number=request.POST.get('phone_number')
        date=request.POST.get('date')
        msg=request.POST.get('msg')
        c=contactQ.objects.create(name=name,useremail=useremail,phone_number=phone_number,date=date,msg=msg)
        c.save()
    return render(request,"contact.html")


# def saveBookingtime(request):
#     if request.method == "POST":
#         start = request.POST.get('start')
#         end = request.POST.get('end')

#         # Validate that fields are not empty
#         if not start or not end:
#             return HttpResponse("Start and end times are required", status=400)

#         # Convert the input strings to datetime objects
#         try:
#             start = parse_datetime(start)
#             end = parse_datetime(end)
#         except (ValueError, TypeError):
#             return HttpResponse("Invalid date/time format", status=400)

#         # Validate that start is before end
#         if start >= end:
#             return HttpResponse("Start time must be before end time", status=400)

#         # Save the data
#         booking = Bookingtime.objects.create(start=start, end=end)
#         booking.save()

#         return HttpResponse("Booking saved successfully", status=200)

#     return HttpResponse("Invalid request method", status=405)
        
                
def saveveriform(request):
    if request.method == "POST":
        # Print all POST data for debugging
        print("POST Data:", request.POST)
        
        # Print all FILES data for debugging
        print("FILES Data:", request.FILES)
        
        # Extract form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        Add = request.POST.get('Add')  # Ensure this field is being extracted
        DLN = request.POST.get('DLN')
        DLFI = request.FILES.get('DLFI')
        DLBI = request.FILES.get('DLBI')
        IDproof = request.POST.get('IDproof')
        Addproof = request.FILES.get('Addproof')  # Corrected: This should be a file field
        
        # is_verified should be set by the admin, not the user
        is_verified = False  # Default to False
        
        # Check if the Add field is missing
        if not Add:
            print("Add field is missing or empty!")
            return HttpResponse("Address (Add) field is required.", status=400)
        
        # Save the data to the database
        try:
            d = veriform.objects.create(
                name=name,
                email=email,
                phone=phone,
                Add=Add,  # Ensure this field is included
                DLN=DLN,
                DLFI=DLFI,
                DLBI=DLBI,
                IDproof=IDproof,
                Addproof=Addproof,
                is_verified=is_verified  # Default to False
            )
            d.save()  # This will trigger the save method in the model
            print("Data saved successfully!")
            messages.success(request, "Your details have been submitted successfully. Please wait until admin approves your request.")

            return render(request, "verifyform.html")
        except Exception as e:
            print(f"Error saving data: {e}")
            return HttpResponse(f"An error occurred: {e}", status=500)
    else:
        return HttpResponse("Invalid request method.", status=405)
from django.shortcuts import render, get_object_or_404, redirect


from django.shortcuts import render
from car.models import postVcl


    
def user_verify(request):
    users = veriform.objects.all()  

    context = {
        'verifing': users  # Pass users to the template
    }
    # Update status dynamically based on is_verified field
    # if user.is_verified:
    #     user.status = "Approved"
    # else:
    #     user.status = "Pending"

    # user.save()  # Save updated status to the database
    messages.success(request, "Your details have been submitted successfully. Please wait until admin approves your request.")

    return render(request, "user_verify.html", context)



def verify(request, email):
    email = unquote(email)  # Decode URL-encoded email
    print(f"Received email in URL: {email}")  # Debugging

    user = get_object_or_404(veriform, email=email)  # Fetch user safely
    return render(request, "verify.html", {"verify": user})


# View to handle verification updates via AJAX
def update_verification(request):
    if request.method == "POST":
        email = request.POST.get("user_email")
        is_verified = request.POST.get("is_verified") == "true"

        user = get_object_or_404(veriform, email=email)
        user.is_verified = is_verified
        user.status = "Approved" if is_verified else "Pending"
        user.save()

        return JsonResponse({"success": True, "message": "Verification updated successfully!"})

    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)

#-----------------ALL UPDATES AND DELETE---------------------------------   
    
# def updatedata(request,id):
#   qw=veriform.objects.get(pk=id)
#   return render(request,'{}',{'qw':qw})


def deletecar(request, id):
    # Correct usage: Use the `contactQ` model
    postVcl.objects.filter(id=id).delete()
    return redirect('vehiclemanage')


def deleteCQ(request, id):
    # Correct usage: Use the `contactQ` model
    contactQ.objects.filter(id=id).delete()
    return redirect('manageCQ')

def deletereg(request,useremail):
    CustomUser.objects.filter(useremail=useremail).delete()
    return redirect('managereg')

def deleteuser(request, id):
    # Correct usage: Use the `contactQ` model
    veriform.objects.filter(id=id).delete()
    return redirect('user_verify')


#------------------ALL UPDATES AND DELETE(END)-------------------------------

#--------------------------------------------------------------------------

import razorpay
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime

# Initialize Razorpay client
client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
# from django.views.decorators.http import require_POST


from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.utils import timezone
from datetime import datetime
@require_POST
def create_order(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User is not authenticated"}, status=401)

    # Fetch Data from POST Request
    amount = request.POST.get("amount")  # Get amount as string
    if not amount:
        return JsonResponse({"error": "Amount is required"}, status=400)

    try:
        amount = int(float(amount) * 100)  # Convert to paise
    except ValueError:
        return JsonResponse({"error": "Invalid amount"}, status=400)

    # Try to get start and end from POST, fallback to session
    start = request.POST.get("start") or request.session.get("start")
    end = request.POST.get("end") or request.session.get("end")

    if not start or not end:
        return JsonResponse({"error": "Start and end dates are required"}, status=400)

    # Convert start and end strings to datetime objects
    try:
        start = timezone.make_aware(datetime.strptime(start, "%Y-%m-%dT%H:%M"))
        end = timezone.make_aware(datetime.strptime(end, "%Y-%m-%dT%H:%M"))
    except ValueError:
        return JsonResponse({"error": "Invalid date format. Use 'YYYY-MM-DDTHH:MM'."}, status=400)

    car_id = request.POST.get("car_id")
    if not car_id:
        return JsonResponse({"error": "Car ID is required"}, status=400)

    try:
        car = postVcl.objects.get(id=car_id)
    except postVcl.DoesNotExist:
        return JsonResponse({"error": "Car not found"}, status=404)
    order_data={
            "amount": amount,
            "currency": "INR",
            "payment_capture": "1",  # Auto capture payment
    }
    order=client.order.create(data=order_data)
    # Create a new booking with status "Pending"
    booking= Booking.objects.create(
        car=car,
        user=request.user,
        start=start,
        end=end,
        razorpay_order_id=order["id"],  # Temporary value, will be updated after payment
        amount=amount / 100,
        payment_status="Pending",
    )

    context = {
        "car": car,

        "razorpay_api_key": settings.RAZORPAY_API_KEY, 
        "order_id": booking.razorpay_order_id,  # Pass the order ID
        "booking": booking,
    }
    
    return render(request, "paymentD.html", context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def paymentD(request, car_id):
    # Ensure the user is authenticated
    if not request.user.is_authenticated:
        return redirect("login")  # Redirect to login page if not authenticated

    # Fetch the car details
    car = get_object_or_404(postVcl, id=car_id)
    
    # Fetch verification details for the logged-in user
    veriforms = get_object_or_404(veriform, email=request.user.email)

    # Ensure car has PPD attribute
    if not hasattr(car, 'PPD'):
        print("Car missing PPD attribute")
        return JsonResponse({"error": "Car object is missing 'PPD' attribute."}, status=400)

    # Calculate the amount in paise
    amountP = int(car.PPD * 100)
    
    # Fetch start and end dates from session
    start = request.session.get("start")
    end = request.session.get("end")

    # Redirect if session data is missing
    if not start or not end:
        messages.error(request, "Please select booking dates first.")
        return redirect("explore")  # Redirect to explore page instead of booking_page

    # Convert start and end to datetime objects
    try:
        start_dt = timezone.make_aware(datetime.strptime(start, "%Y-%m-%dT%H:%M"))
        end_dt = timezone.make_aware(datetime.strptime(end, "%Y-%m-%dT%H:%M"))
    except ValueError:
        print("Invalid date format")
        return JsonResponse({"error": "Invalid date format. Use 'YYYY-MM-DDTHH:MM'."}, status=400)

    # Create Razorpay order
    try:
        order_data = {
            "amount": amountP,
            "currency": "INR",
            "payment_capture": "1",
        }
        print(f"Creating order with amount: {amountP}")
        order = client.order.create(data=order_data)
        print(f"Order created: {order['id']}")
    except Exception as e:
        print(f"Error creating Razorpay order: {str(e)}")
        return JsonResponse({"error": f"Error creating payment order: {str(e)}"}, status=500)

    # Create a new booking or get existing one
    try:
        # Check if booking already exists
        booking = Booking.objects.filter(
            car=car,
            user=request.user,
            start=start_dt,
            end=end_dt,
            payment_status="Pending"
        ).first()
        
        if not booking:
            # Create new booking
            booking = Booking.objects.create(
                car=car,
                user=request.user,
                start=start_dt,
                end=end_dt,
                razorpay_order_id=order["id"],
                amount=float(car.PPD),
                payment_status="Pending"
            )
        else:
            # Update existing booking with new order ID
            booking.razorpay_order_id = order["id"]
            booking.save()
            
        print(f"Booking created/updated with ID: {booking.id}")
    except Exception as e:
        print(f"Error creating booking: {str(e)}")
        return JsonResponse({"error": f"Error creating booking: {str(e)}"}, status=500)

    context = {
        "car": car,
        "veriforms": veriforms,
        "amountP": amountP,
        "razorpay_api_key": settings.RAZORPAY_API_KEY,
        "start": start_dt,
        "end": end_dt,
        "order_id": order["id"],
        "booking": booking
    }
    
    print(f"Rendering payment template with booking ID: {booking.id}, order ID: {order['id']}")
    return render(request, "paymentD.html", context)

def explore(request):
    data = postVcl.objects.all()
    if request.method == "POST":
        start = request.POST.get("start") or request.session.get("start")
        end = request.POST.get("end") or request.session.get("end")
        
        if not start or not end:
            return JsonResponse({"error": "Start and end dates are required"}, status=400)

        # Convert strings to datetime objects
        # try:
        #     start_date = datetime.strptime(start, '%Y-%m-%d')  # Adjust format as per your input
        #     end_date = datetime.strptime(end, '%Y-%m-%d')
        # except ValueError:
        #     return JsonResponse({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)
        # formatted_start_date = start.strftime('%Y-%m-%d')
        # formatted_end_date = end.strftime('%Y-%m-%d')

        # # Calculate the number of days
        # num_days = (end - start).days

        # if num_days <= 0:
        #     num_days = 1  # At least 1 day

        # Save the start, end, num_days, and amount in session
        request.session["start"] = start
        request.session["end"] = end
        # request.session["num_days"] = num_days
        request.session["amount"] = request.POST.get("amount")  
        request.session.modified = True  # Ensure session updates

        print("Session start date:", request.session.get("start"))  # Debugging
        print("Session end date:", request.session.get("end"))  # Debugging
        # print("Number of days:", num_days)

    return render(request, "explore.html", {'data': data})

from django.views.decorators.csrf import csrf_exempt


import razorpay
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))

@csrf_exempt
def update_booking_status(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request body
            print("Received update_booking_status request")
            data = json.loads(request.body)
            print("Request data:", data)
            
            # Fetch data from the parsed JSON
            booking_id = data.get("booking_id")
            payment_id = data.get("payment_id")
            amount = data.get("amount")  # Amount in paise

            # Validate data
            if not booking_id or not payment_id or not amount:
                print("Missing required data:", {"booking_id": booking_id, "payment_id": payment_id, "amount": amount})
                return JsonResponse({"error": "Booking ID, Payment ID, and Amount are required"}, status=400)

            # Convert booking_id to int if it's a string
            try:
                booking_id = int(booking_id)
            except ValueError:
                print(f"Invalid booking ID format: {booking_id}")
                return JsonResponse({"error": "Invalid booking ID format"}, status=400)

            try:
                booking = Booking.objects.get(id=booking_id)
                print(f"Found booking: {booking.id}, Status: {booking.payment_status}")
            except Booking.DoesNotExist:
                print(f"Booking not found with ID: {booking_id}")
                return JsonResponse({"error": "Booking not found"}, status=404)

            # Payment might already be captured by Razorpay, in which case we should just update our records
            try:
                # Try to fetch payment information
                payment_info = client.payment.fetch(payment_id)
                print(f"Payment info: {payment_info}")
                
                if payment_info.get("status") == "captured":
                    print("Payment already captured by Razorpay")
                else:
                    # Try to capture payment if not already captured
                    print(f"Attempting to capture payment: {payment_id} for amount: {amount}")
                    capture_response = client.payment.capture(payment_id, amount)
                    print(f"Payment capture response: {capture_response}")
                    
                # Update the booking status to 'paid' and save the Razorpay payment ID
                booking.payment_status = 'paid'
                booking.razorpay_payment_id = payment_id
                booking.save()
                print(f"Booking Updated Successfully: {booking.id}, Status: {booking.payment_status}, Payment ID: {booking.razorpay_payment_id}")

                return JsonResponse({
                    "success": True,
                    "message": "Booking status updated to paid",
                    "booking_id": booking.id,
                    "razorpay_payment_id": booking.razorpay_payment_id,
                    "payment_status": booking.payment_status
                })
                
            except razorpay.errors.BadRequestError as e:
                print(f"Razorpay error: {str(e)}")
                
                # Even if capture fails, the payment might have been successful
                # Update booking status anyway if this was just a duplicate capture attempt
                if "payment already captured" in str(e).lower():
                    booking.payment_status = 'paid'
                    booking.razorpay_payment_id = payment_id
                    booking.save()
                    print(f"Payment was already captured. Booking updated: {booking.id}")
                    
                    return JsonResponse({
                        "success": True,
                        "message": "Payment was already captured. Booking status updated.",
                        "booking_id": booking.id,
                        "razorpay_payment_id": payment_id
                    })
                    
                return JsonResponse({"error": f"Razorpay error: {str(e)}"}, status=400)

        except json.JSONDecodeError as e:
            print(f"Invalid JSON data: {str(e)}")
            return JsonResponse({"error": "Invalid JSON data"}, status=400)
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
    
    print("Invalid request method!")
    return JsonResponse({"error": "Invalid request method"}, status=405)

def payment_success(request):
    # Get the latest successful booking for the current user
    if request.user.is_authenticated:
        booking = Booking.objects.filter(
            user=request.user,
            payment_status='paid'
        ).order_by('-id').first()
        
        if booking:
            # Get car details
            car = booking.car
            return render(request, "payment_success.html", {
                'booking': booking,
                'car': car
            })
    
    return render(request, "payment_success.html")