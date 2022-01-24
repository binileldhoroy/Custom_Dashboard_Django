from django.shortcuts import render,redirect
from base.models import User
from base.forms import UserForm
from django.views.decorators.cache import never_cache

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
        userView = User.objects.all()
        context = {'users':userView}
        return render(request,'dashboard/home.html',context)
    else:
        return redirect('admin-login')


def delete(request,pkey):
    if request.session.has_key('ses_admin'):
        request.session['ses_admin']
        user = User.objects.get(id=pkey)

        if request.method == 'POST':
            user.delete()
            return redirect('admin-home')
        context = {'user':user}
        return render(request,'dashboard/delete.html',context)
    else:
         return redirect('admin-login')

def update(request,pkey):
    if request.session.has_key('ses_admin'):
        request.session['ses_admin']
        user = User.objects.get(id=pkey)
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
def logout(request):
    try:
        del request.session['ses_admin']
    except:
        return redirect('admin-login')
    return redirect('admin-login')