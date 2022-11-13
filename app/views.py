
from django.shortcuts import render, redirect
from .models import *
from random import randint

# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def SignupPage(request):
    return  render(request,"app/signup.html")

def RegisterUser(request):
    if request.POST['role']=="Candidate":
        role= request.POST['role']
        fname= request.POST['firstname']
        lname= request.POST['lastname']
        email= request.POST['email']
        password= request.POST['password']
        cpassword= request.POST['cpassword']

        user= UserMaster.objects.filter(email= email)
        if user :
            message= "user already Exist"
            return render(request,"app/signup.html",{'msg':message})

        else:
            if password==cpassword:
                otp= randint(100000,999999)
                newuser=UserMaster.objects.create(role=role,otp=otp,email=email,password=password )
                newcand= Candidate.objects.create(user_id=newuser,firstname=fname,lastname= lname)
                return render(request,"app/otpverify.html",{'email':email})

    else:
        print("Company Registration")

def OTPPage(request):
    return render(request,"app/otpverify.html")

def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])


    user = UserMaster.objects.get(email= email)

    if user:
        if user.otp == otp:
            message="Otp verified successfully"
            return render(request,"app/login.html",{'msg':message})

        else:
            message = "Otp is incorrect"
            return render(request,"app/otpverify.html",{'msg':message})

    else:
        return render(request,"app/signup.html")

def LoginPage(request):
    return render(request,"app/login.html")


def LoginUser(request):
    if request.POST['role']=="Candidate":
        email= request.POST['email']
        password = request.POST['password']

        user= UserMaster.objects.get(email=email)
        if user:
            if user.password==password and user.role== "Candidate":
                 can= Candidate.objects.get(user_id= user)
                 request.session['id']= user.id 
                 request.session['role']=user.role
                 request.session['firstname']= can.firstname
                 request.session['lastname']= can.lastname
                 request.session['email']= user.email

                 return redirect('index')

            else:
                message= 'password does not match'
                return render(request, "app/login.html",{'msg':message})

        else:
            message= "User does not exist"
            return render (request,"app/login.html",{'msg':message})


def ProfilePage(request,pk):
    
    user = UserMaster.objects.get(pk=pk)
    can= Candidate.objects.get(user_id= user)
    return render(request, "app/profile.html" , {'user':user,'can':can})
    

def UpdateProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == "Candidate":
        can = Candidate.objects.get(user_id= user)
        can.state = request.POST['state']    # First country is belong to database field and second country belongs to HTML input name
        can.city = request.POST['city']
        can.jobtype = request.POST['jobtype']
        can.jobcategory = request.POST['category']
        can.highestedu = request.POST['education']
        can.experience = request.POST['experience']
        can.website = request.POST['website']
        can.shift = request.POST['shift']
        can.jobdescription = request.POST['description']
        can.min_salary = request.POST['minsalary']
        can.max_salary = request.POST['maxsalary']
        can.contact = request.POST['contact']
        can.gender = request.POST['gender']
        can.profile_pic = request.FILES['image']
        can.save()
        print("DATA SAVED")
        url = f'/profile/{pk}'    # formatting URL
        return redirect(url)
