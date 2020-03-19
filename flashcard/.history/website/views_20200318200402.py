from django.shortcuts import render
import urbandictionary as ud

addition = []
times = 0
# Create your views here.
def home(request):
    return render(request, 'home.html', {})
def add(request):
    times = 0
    from random import randint
    num1 = randint(1,1000)
    num2 = randint(1,1000)
    
    if request.method == "POST":
        answer = request.POST['answer']

        if not answer:
            my_answer = "Hey you forgot to enter your answer!"
            color = "danger"
            return render(request, 'add.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})
            
        if not answer.isdigit():
            my_answer = "You're not supposed to enter characters here :("
            color = "danger"
            return render(request, 'add.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})
            

        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        
        correct_answer = int(old_num1) + int(old_num2)
        if int(answer) == correct_answer:
            my_answer = "Correct! "+ old_num1 + "+" + old_num2 + " = " + str(correct_answer) + "."
            color = "success"
        else:
            my_answer = "Incorrect! "+ old_num1 + "+" + old_num2 + " is not " + answer + ". It is " + str(correct_answer) + "."
            color = "danger"
        addition.append(answer)
        times = times + 1
        return render(request, 'add.html', { "answer": answer, "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color, "add":addition[times:]})

    return render(request, 'add.html', { "num1": num1, "num2": num2, })

def subtract(request):
    from random import randint
    num1 = randint(1,100)
    num2 = randint(1,100)
    if request.method == "POST":
        answer = request.POST['answer']

        if not answer:
            my_answer = "Hey you forgot to enter your answer!"
            color = "danger"
            return render(request, 'subtract.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

        if not answer.isdigit():
            my_answer = "You're not supposed to enter characters here :("
            color = "danger"
            return render(request, 'subtract.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})
            
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
    num1 = randint(1,20)
    num2 = randint(1,10)
    if request.method == "POST":
        answer = request.POST['answer']

        if not answer:
            my_answer = "Hey you forgot to enter your answer!"
            color = "danger"
            return render(request, 'multiply.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

        if not answer.isdigit():
            my_answer = "You're not supposed to enter characters here :("
            color = "danger"
            return render(request, 'multiply.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})
            
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

        if not answer:
            my_answer = "Hey you forgot to enter your answer!"
            color = "danger"
            return render(request, 'divide.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

        if not answer.isdigit():
            my_answer = "You're not supposed to enter characters here :("
            color = "danger"
            return render(request, 'divide.html', { "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})
            
        old_num1 = request.POST['old_num1']
        old_num2 = request.POST['old_num2']
        correct_answer = int(old_num1) / int(old_num2)
        
        if float(answer) == float(correct_answer):
            my_answer = "Correct! "+ old_num1 + "/" + old_num2 + " = " + str(correct_answer) + "."
            color = "success"
        else:
            my_answer = "Incorrect! "+ old_num1 + "/" + old_num2 + " is not " + answer + ". It is " + str(correct_answer) + "."
            color = "danger"

        return render(request, 'divide.html', { "answer": answer, "my_answer": my_answer, "num1": num1, "num2": num2, "color" : color})

    return render(request, 'divide.html', { "num1": num1, "num2": num2, })

def dictionary(request):
    if request.method == "POST":
        word = request.POST['word']
        if word == "Bhavik":
            defs = UrbanDefinition(
                definition['word'], 
                definition['definition'],
                definition['example'],
                int(definition['thumbs_up']),
                int(definition['thumbs_down'])
            )
        else:
            defs = ud.define(word)
        
        return render(request, 'dictionary.html', {"word":word, "output":defs})
    return render(request, 'dictionary.html', {})
    