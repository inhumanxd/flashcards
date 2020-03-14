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
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct answer!"
        else:
            my_answer = "Incorrect! "+old_num1+"+"+old_num2+"=" + str(correct_answer) + "."
        return render(request, 'add.html', { "answer": answer, "my_answer": my_answer, "num1": num1, "num2": num2, })

    return render(request, 'add.html', { "num1": num1, "num2": num2, })
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
                    