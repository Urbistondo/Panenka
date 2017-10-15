from django.shortcuts import render
from .models import Contest


def contests_list(request):
    print("CONTEST ACCESSED")
    current_user = request.user
    all_contests = Contest.objects.all()
    print('LENGTH: ', len(all_contests))
    return render(request, 'users/dashboard.html', {'contests': all_contests, 'user': current_user})

def contests_create(request):
    if request.method == 'GET':
        return render(request, 'users/contest_form.html')
    elif request.method == 'POST':
        pass

def contests_show(request):
    current_user = request.user
    all_contests = Contest.objects.all()
    print('LENGTH: ', len(all_contests))
    return render(request, 'users/dashboard.html', {'contests': all_contests, 'user': current_user})