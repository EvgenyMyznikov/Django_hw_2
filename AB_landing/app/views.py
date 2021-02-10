from collections import Counter

from django.shortcuts import render

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    land = request.GET.get('from-landing')
    if land == 'test':
        counter_click['test'] += 1
        return render(request, 'index.html')
    elif land == 'original':
        counter_click['original'] += 1
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов
    land = request.GET.get('ab-test-arg')
    if land == 'original':
        counter_show['original'] += 1
        return render(request, 'landing.html')
    elif land == 'test':
        counter_show['test'] += 1
        return render(request, 'landing_alternate.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Для вывода результат передайте в следующем формате:
    cst = counter_show['test']
    cso = counter_show['original']
    cct = counter_click['test']
    cco = counter_click['original']
    test_conversation = 0
    original_conversation = 0
    try:
        test_conversation = cct / cst
    except ZeroDivisionError:
        print('деление на 0')
    try:
        original_conversation = cco / cso
    except ZeroDivisionError:
        print('деление на 0')
    return render(request, 'stats.html', context={
        'test_conversion': test_conversation,
        'original_conversion': original_conversation,
    })
