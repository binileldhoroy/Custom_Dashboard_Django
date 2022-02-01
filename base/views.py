from django.shortcuts import render,redirect
from django.views.decorators.cache import never_cache
from .models import BaseUser, Ebook
# Create your views here.


@never_cache
def loginUser(request):
    if request.session.has_key('uname'):
        return redirect('home')
    elif request.method == 'POST':
        c_username = request.POST['username']
        c_password = request.POST['password']
        

        try:
            user = BaseUser.objects.get(username = c_username,password = c_password)

            if user is not None:
                request.session['uname'] = c_username
                return redirect('home')
        except:
            text = 'Invalid Username/password'
            return render(request,'base/login.html',{'text':text})

    return render(request,'base/login.html')


@never_cache
def registerUser(request):
    if request.session.has_key('uname'):
        cur_user = request.session['uname']
        return render(request,'base/home.html',{'cur_user':cur_user})
    elif request.method == 'POST':
        cusername = request.POST['username']
        cemail = request.POST['email']
        fname = request.POST['fullname']
        cpassword = request.POST['password']
        cpassword1 = request.POST['password1']
        if len(cusername) < 3 or cusername == '':
            text = "Must be 3 letters"
            return render(request,'base/register.html',{'utext':text})
        elif len(fname) < 3 or fname == '':
            text = "Must be 3 letters"
            return render(request,'base/register.html',{'etext':text})
        if len(cpassword) < 6:
            text = "Must be 6 letters"
            return render(request,'base/register.html',{'ptext':text})
        elif cpassword != cpassword1:
            text = "Password Miss Match"
            return render(request,'base/register.html',{'ptext':text})
        else:

            uname = None
            uemail = None
            try:
                uname = BaseUser.objects.get(username = cusername)

            except:
                pass
            try:
                uemail = BaseUser.objects.get(email = cemail)

            except:
                pass
            
            if uname is not None:
                text = 'Username Allready taken'
                return render(request,'base/register.html',{'utext':text})
            elif uemail is not None:
                text = 'Username Allready taken'
                return render(request,'base/register.html',{'etext':text})
            else:
                user = BaseUser.objects.create(
                    username = cusername,
                    email = cemail,
                    password = cpassword,
                    name = fname
                )
                user.save()
                text = "Successfully Created"
                return render(request,'base/register.html',{'stext':text})



    return render(request,'base/register.html')



@never_cache
def home(request):
    if request.session.has_key('uname'):
        cur_user = request.session['uname']
        ebooks = Ebook.objects.all()
        return render(request,'base/home.html',{'cur_user':cur_user,'ebooks':ebooks})
    else:
        return redirect('login')



@never_cache
def logoutUser(request):
    try:
        del request.session['uname']
    except:
        return redirect('login')
    return redirect('login')