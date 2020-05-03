from django.shortcuts import get_object_or_404, render
import csv

from kalori.models import Food


def index(request):
    food_list = Food.objects.order_by('-id')[:5]
    context = {
        'food_list': food_list,
    }
    return render(request, 'kalori/index.html', context)


def detail(request, food_id):
    food = get_object_or_404(Food, pk=food_id)
    return render(request, 'kalori/detail.html', {'food': food})


def upload_csv():
    with open('DataKalori.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            _, created = Food.objects.update_or_create(
                name=row[0],
                calories=float(row[1]),
                carbs=float(row[4]),
                cholestrol=float(row[7]),
                fat=float(row[2]),
                fiber=float(row[6]),
                protein=float(row[3]),
                sat_fat=float(row[8]),
                sugar=float(row[5])
            )
