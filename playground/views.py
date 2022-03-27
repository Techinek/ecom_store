from django.shortcuts import render


def calculate():
    x = 10
    y = 5
    return x + y


def say_hello(request):
    z = calculate()
    context = {
        'greetings': 'Hi there'
    }
    return render(request, 'playground/hello.html', context)
