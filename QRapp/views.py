
import qrcode
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
    # Create your views here.\

        
        
def login_page(request):
    if request.method == 'POST':
        u=request.POST.get('username')
        p=request.POST.get('password')
        print(u,p)
        user=authenticate(request,username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('/home')
        else:
            return redirect('/')    

      
    return render(request,'login_page.html')    
    


@login_required(login_url='/')
def index(request):
    if request.method== 'GET':
        data=request.GET.get('data')
        img = qrcode.make(data)
        type(img)  # qrcode.image.pil.PilImage
        img.save("static/images/some_file.png")
       
    
    return render(request,'index.html')


def logout_logg(request):
    logout(request)
    return redirect('/')

