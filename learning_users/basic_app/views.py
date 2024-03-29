from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm
# Create your views here.
def index(request):
    return render(request,'basic_app/index.html')

def register(request):

    registerd = False

    if regist.method == 'POST':
        user_form = UserForm(date=request.POST)
        prifile_form = UserProfileInfo(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registerd = True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/register.html',{'user_form':user_form,'prifile_form':profile_form,'registerd':registerd})
