from django.shortcuts import get_object_or_404, render

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
