from django.shortcuts import render
from .forms import MyForm
# Create your views here.
def login(request):
    if request.method == 'POST':
        my_form = MyForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        if my_form.is_valid():
            print("Dữ liệu hợp lệ:", my_form.cleaned_data)
        else:
            print("Lỗi:", my_form.errors)  # ✅ Hiển thị lỗi validation
        print(f'Tài khoản {username} \nMật khẩu {password}')
        
        context = {'form':my_form}


        
        return render(request=request,template_name='login.html',context=context)
    else:
        my_form = MyForm()
        context = {'form':my_form}
        print(my_form)
        print(context)
        return render(request=request,template_name='login.html',context=context)