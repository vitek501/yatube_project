from django.http import HttpResponse


# Главная страница.
def index(request):
    return HttpResponse('Главная страница')


def groups_posts(request, slug):
    return HttpResponse(f'Группа {slug}')
