from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.views.generic import View
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from .utils import TokenGenerator, generate_token
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth import authenticate,login,logout

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Create your views here.


def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        c_password=request.POST['cpassword']
        if password != c_password:
            messages.warning(request,"Password doesn't match")
            return render(request, 'signup.html')
        try:
            if User.objects.get(username=email):
                messages.info(request,"Email is already exists")
                return render(request, 'signup.html')
        except Exception as identifier:
            pass

        
        user=User.objects.create_user(email,email,password)
        user.is_active=False  
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)
        current_site = get_current_site(request)
        activation_link = f"http://{current_site.domain}/activate/{uid}/{token}/"
        print(activation_link)
        messages.success(request,f"Activate Your Account by clicking the link { activation_link}")
        return render(request, 'signup.html')
    return render(request, 'signup.html')






def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_user_model().objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Successfully Activated")
        return redirect('/auth/login')
    else:
       messages.error(request, "Activation link is invalid or has expired.")
       return redirect('/auth/signup')



def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        userpassword=request.POST['password']
        myuser=authenticate(username=username, password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request, "Login Successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('/auth/login')
    return render(request, 'login.html')

def handlelogout(request):
    logout(request)
    messages.info(request,"Logout Successfully")
    return redirect('/auth/login')