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
            my_answer = "Correct! "+ old_num1 + "+" + old_num2 + " = " + str(correct_answer) + "."
            color = "success"
        else:
            my_answer = "Incorrect! "+ old_num1 + "+" + old_num2 + " is not " + answer + ". It is " + str(correct_answer) + "."
            color = "danger"

        return render(request, 'add.html', { "answer": answer, "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

    return render(request, 'add.html', { "num1": num1, "num2": num2, })

def subtract(request):
    from random import randint
    num1 = randint(1,50)
    num2 = randint(1,50)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct_answer = int(old_num1) - int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! "+ old_num1 + "-" + old_num2 + " = " + str(correct_answer) + "."
            color = "success"
        else:
            my_answer = "Incorrect! "+ old_num1 + "-" + old_num2 + " is not " + answer + ". It is " + str(correct_answer) + "."
            color = "danger"

        return render(request, 'subtract.html', { "answer": answer, "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

    return render(request, 'subtract.html', { "num1": num1, "num2": num2, })
def multiply(request):
    from random import randint
    num1 = randint(1,10)
    num2 = randint(1,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct_answer = int(old_num1) * int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! "+ old_num1 + "x" + old_num2 + " = " + str(correct_answer) + "."
            color = "success"
        else:
            my_answer = "Incorrect! "+ old_num1 + "x" + old_num2 + " is not " + answer + ". It is " + str(correct_answer) + "."
            color = "danger"

        return render(request, 'multiply.html', { "answer": answer, "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

    return render(request, 'multiply.html', { "num1": num1, "num2": num2, })
def divide(request):
    from random import randint
    num1 = randint(1,10)
    num2 = randint(1,10)
    if request.method == "POST":
        answer = request.POST['answer']
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct_answer = int(old_num1) / int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! "+ old_num1 + "/" + old_num2 + " = " + str(correct_answer) + "."
            color = "success"
        else:
            my_answer = "Incorrect! "+ old_num1 + "/" + old_num2 + " is not " + answer + ". It is " + str(correct_answer) + "."
            color = "danger"

        return render(request, 'divide.html', { "answer": answer, "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

    return render(request, 'divide.html', { "num1": num1, "num2": num2, })
