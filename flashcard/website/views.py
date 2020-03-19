from django.shortcuts import render,redirect
from django.conf import settings
from isodate import parse_duration
import requests
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
    while num1<num2:
        num1 = randint(1,100)
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

        if not answer.replace('.', '', 1).isdigit():
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
        defs = ud.define(word)
        
        return render(request, 'dictionary.html', {"word":word, "output":defs})
    return render(request, 'dictionary.html', {})

def youtube(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'
    videos = []

    if request.method == "POST":
        search_params = {
            'part': 'snippet',
            'q' : request.POST['search'],
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 9,
            'type' : 'video'
        }
        
        req = requests.get(search_url, params=search_params)
        results = req.json()['items']
        
        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect('https://www.youtube.com/watch?v='+video_ids[0])

        video_params = {
            'part' : 'snippet, contentDetails',
            'key' : settings.YOUTUBE_DATA_API_KEY,
            'id' : ','.join(video_ids),
            'maxResults' : 9,
        }
        
        req = requests.get(video_url, params=video_params)
        results = req.json()['items']
        
        for result in results:
            # print(result)
            
            video_data = {
                'title' : result['snippet']['title'],
                'id' : result['id'],
                'url' : 'https://www.youtube.com/watch?v='+result['id'],
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail' : result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)
        
    context = {
        'videos' : videos
    }
    
    return render(request, 'youtube.html', context)     