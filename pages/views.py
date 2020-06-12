from django.shortcuts import render

# Create your views here.
def loop(request):
    nums=[]
    for data in range(10):
        nums.append(data)
    context={
        'nums':nums
    }
    return render(request,'loop.html',context)

def throw(request):
    return render(request,'throw.html')