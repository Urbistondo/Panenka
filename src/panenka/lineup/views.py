from django.shortcuts import render
from .models import Lineup

# Create your views here.
def lineup_list(request):
    print("LINEUP SAVED")
    current_user = request.user
    starting_players = Lineup.get_starterplayers()
    bench_players = Lineup.get_benchplayers()
    return render(request, '/lineup.html', {'starting_players': starting_players,'bench_players':  bench_players, 'user': current_user})