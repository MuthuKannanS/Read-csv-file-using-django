from django.shortcuts import render,redirect
import pandas as pd
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def view(request):
    if request.method == 'POST':
        file1 = request.FILES['file']
        data = pd.read_csv(file1)
        return render(request,'view.html',{'data':data})
    else:
        return redirect(index)