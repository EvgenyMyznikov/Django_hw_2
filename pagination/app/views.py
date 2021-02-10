from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    bus_station = []
    with open('data-398-2018-08-30.csv', 'r', encoding='cp1251') as file:
        reader = csv.DictReader(file)
        for row in reader:
            station = {'Name': row['Name'], 'Street': row['Street'], 'District': row['District']}
            bus_station.append(station)
            # print(row)
    paginator = Paginator(bus_station, settings.POSTS_PER_PAGE)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    prev_page = None
    next_page = None
    if page.has_previous():
        prev_page = page.previous_page_number()
    if page.has_next():
        next_page = page.next_page_number()
    context = {
        'bus_stations': page,
        'current_page': page.number,
        'prev_page_url': prev_page,
        'next_page_url': next_page
    }
    return render(request, 'index.html', context=context)

