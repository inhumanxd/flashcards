from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})
def add(request):
    from random import randint
    num1 = randint(1,50)
    num2 = randint(1,50)
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'add.html', { "answer": answer })

    return render(request, 'add.html', {})
def subtract(request):
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'subtract.html', { "answer": answer })
    
    return render(request, 'subtract.html', {})
def multiply(request):
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'multiply.html', { "answer": answer })
    
    return render(request, 'multiply.html', {})
def divide(request):
    if request.method == "POST":
        answer = request.POST['answer']
        return render(request, 'divide.html', { "answer": answer })
    
    return render(request, 'divide.html', {})
                    