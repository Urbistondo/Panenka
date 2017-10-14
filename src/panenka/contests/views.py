from django.shortcuts import render
from .models import Contest


def contests_list(request):
    print("CONTEST ACCESSED")
    current_user = request.user
    all_contests = Contest.objects.all()
    print('LENGTH: ', len(all_contests))
    return render(request, 'users/dashboard.html', {'contests': all_contests, 'user': current_user})