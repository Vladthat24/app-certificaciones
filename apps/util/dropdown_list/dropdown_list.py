from django.shortcuts import render


def dropdown_list(request, list):
    return render(request, '../templates/dropdown_list.html',
                  {'objects_list': list})
