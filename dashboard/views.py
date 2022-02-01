from django.shortcuts import render,redirect
from base.models import BaseUser
from base.forms import UserForm
from django.views.decorators.cache import never_cache
from django.db.models import Q

# Create your views here.


@never_cache
def loginAdmin(request):
    if request.session.has_key('ses_admin'):
        request.session['ses_admin']
        return redirect('admin-home')
    elif request.method == 'POST':
        user = request.POST["username"]
        pas = request.POST["password"]
        if user == "admin" and pas == "admin123":
            request.session['ses_admin'] = user
            return redirect('admin-home')
        else:
            text = 'invalid username/password'
            return render(request,'dashboard/login.html',{'text':text})
    return render(request,'dashboard/login.html')


@never_cache
def home(request):
    if request.session.has_key('ses_admin'):
        request.session['ses_admin']
        q = request.GET.get('q') if request.GET.get('q') != None else ''
        userView = BaseUser.objects.filter(
            Q(username__icontains=q)|
            Q(email__icontains=q)|
            Q(name__icontains=q)
        )
        context = {'users':userView}
        return render(request,'dashboard/home.html',context)
    else:
        return redirect('admin-login')


@never_cache
def delete(request,pkey):
    if request.session.has_key('ses_admin'):
        request.session['ses_admin']
        user = BaseUser.objects.get(id=pkey)

        if request.method == 'POST':
            user.delete()
            return redirect('admin-home')
        context = {'user':user}
        return render(request,'dashboard/delete.html',context)
    else:
         return redirect('admin-login')

@never_cache
def update(request,pkey):
    if request.session.has_key('ses_admin'):
        request.session['ses_admin']
        user = BaseUser.objects.get(id=pkey)
        form = UserForm(instance=user)
        if request.method == 'POST':
            form = UserForm(request.POST,instance=user)
            if form.is_valid():
                form.save()
                return redirect('admin-home')

        context = {'form':form}
        return render(request,'dashboard/update.html',context)
    else:
        return redirect('admin-login')

@never_cache
def addUser(request):
    if request.session.has_key('ses_admin'):
        request.session['ses_admin']
        if request.method == 'POST':
            cusername = request.POST['username']
            cemail = request.POST['email']
            fname = request.POST['fullname']
            cpassword = request.POST['password']
            cpassword1 = request.POST['password1']
            if len(cusername) < 3 and cusername == '':
                text = "Must be 3 letters"
                return render(request,'dashboard/adduser.html',{'utext':text})
            elif fname == '' and len(fname) < 3:
                text = "Must be 3 letters"
                return render(request,'dashboard/adduser.html',{'etext':text})
            elif len(cpassword) < 6:
                text = "Must be 6 letters"
                return render(request,'dashboard/adduser.html',{'ptext':text})
            elif cpassword != cpassword1:
                text = "Password Miss Match"
                return render(request,'dashboard/adduser.html',{'ptext':text})
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
                    text = 'Username Already taken'
                    return render(request,'dashboard/adduser.html',{'utext':text})
                elif uemail is not None:
                    text = 'Email Already taken'
                    return render(request,'dashboard/adduser.html',{'etext':text})
                else:
                    user = BaseUser.objects.create(
                        username = cusername,
                        email = cemail,
                        password = cpassword,
                        name = fname
                    )
                    user.save()
                    text = "Successfully Created"
                    return render(request,'dashboard/adduser.html',{'stext':text})
        else:
            return render(request,'dashboard/adduser.html')

@never_cache
def logout(request):
    try:
        del request.session['ses_admin']
    except:
        return redirect('admin-login')
    return redirect('admin-login')