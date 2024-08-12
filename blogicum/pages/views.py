from django.shortcuts import render


def about(request):
    return render(request, 'pages/about.html')  # Страница "О нас"

def rules(request):
    return render(request, 'pages/rules.html')  # Страница "Правила"
