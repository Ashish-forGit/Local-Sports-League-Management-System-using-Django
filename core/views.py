from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Sport, Category, Detail,Post
# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def sports(request):
    sports = Sport.objects.all()
    # sports = Sport.objects.filter(owner=request.user).order_by('date_added')
    context = {'sports': sports, 'index':True}
    return render(request, 'core/sports.html', context)

def sport(request, sport_id):
    sport = Sport.objects.get(id=sport_id)
    # if sport.owner != request.user:
    #     raise Http404
    
    details = sport.detail_set.order_by('-date_added')
    context = {'sport':sport, 'details': details, 'index':True}
    return render(request, 'core/sport.html', context)

def index(request):
    sports = Sport.objects.all()
    categories = Category.objects.all()
    details = Detail.objects.order_by('-date_added')
    context = {'sports': sports, 'categories': categories, 'details': details}
    return render(request, 'core/index.html', context)


def detail(request, detail_id):
    detail = get_object_or_404(Detail, id=detail_id)
    context = {'detail': detail}
    return render(request, 'core/detail.html', context)



def about(request):
     return  render(request, 'core/about.html')



# def search(request):
#     query = request.GET.get('query')
#     results = Detail.objects.filter(text__icontains=query)
#     context = {'results': results, 'query': query}
#     return render(request, 'core/search.html', context)

def search(request):
    query = request.GET.get('query')
    results = Post.objects.filter(article__icontains=query)
    context = {'results': results, 'query': query}
    return render(request, 'core/search.html', context)


from django.shortcuts import render, redirect, get_object_or_404
from .models import CricketTeamMember
from .forms import CricketTeamMemberForm

# Create & List Cricket Players
def cricket_team_list(request):
    players = CricketTeamMember.objects.all()
    return render(request, 'core/cricket_team_list.html', {'players': players})

# Create Cricket Player
def register_cricket(request):
    if request.method == "POST":
        form = CricketTeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('core:cricket_team_list')
    else:
        form = CricketTeamMemberForm()

    return render(request, 'core/register_cricket.html', {'form': form})

# Update Cricket Player
def update_cricket_player(request, player_id):
    player = get_object_or_404(CricketTeamMember, id=player_id)
    if request.method == "POST":
        form = CricketTeamMemberForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('core:cricket_team_list')
    else:
        form = CricketTeamMemberForm(instance=player)

    return render(request, 'core/update_cricket.html', {'form': form, 'player': player})

# Delete Cricket Player
def delete_cricket_player(request, player_id):
    player = get_object_or_404(CricketTeamMember, id=player_id)
    if request.method == "POST":
        player.delete()
        return redirect('core:cricket_team_list')

    return render(request, 'core/delete_cricket.html', {'player': player})

from django.shortcuts import render, redirect
from .models import FootballTeamMember
from .forms import FootballTeamMemberForm

def register_football(request):
    form = FootballTeamMemberForm()

    # Get all unique team names
    teams = FootballTeamMember.objects.values_list('team', flat=True).distinct()

    if request.method == "POST":
        form = FootballTeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            team_name = form.cleaned_data.get('team')  # Get the selected team name
            return redirect('core:football_team_list', team_name=team_name)  # Redirect to that team's list

    return render(request, 'core/register_football_player.html', {'form': form, 'teams': teams})


from django.shortcuts import render, get_object_or_404, redirect
from .models import FootballTeamMember
from .forms import FootballTeamMemberForm

# ✅ View to list players based on team name
def football_team_list(request, team_name):
    if team_name == "all":
        players = FootballTeamMember.objects.all()
    else:
        players = FootballTeamMember.objects.filter(team=team_name)

    return render(request, 'core/football_team_list.html', {'players': players})


# ✅ View to update football player details
def update_football_player(request, player_id):
    player = get_object_or_404(FootballTeamMember, id=player_id)
    if request.method == "POST":
        form = FootballTeamMemberForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('core:football_team_list', team_name=player.team)
    else:
        form = FootballTeamMemberForm(instance=player)
    
    return render(request, 'core/update_football_player.html', {'form': form, 'player': player})

# ✅ View to delete a football player
def delete_football_player(request, player_id):
    player = get_object_or_404(FootballTeamMember, id=player_id)
    team_name = player.team  # Get team name before deleting
    if request.method == "POST":
        player.delete()
        return redirect('core:football_team_list', team_name=team_name)

    return render(request, 'core/delete_football_player.html', {'player': player})



from django.shortcuts import render, redirect
from .models import Match
from .forms import MatchForm

def schedule_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm()
    
    return render(request, 'core/schedule_match.html', {'form': form})

from django.shortcuts import render
from .models import ScheduledMatch

def match_list(request):
    matches = ScheduledMatch.objects.all()  # Fetch all matches
    return render(request, "core/match_list.html", {"matches": matches})


from django.shortcuts import render, redirect
from .models import ScheduledMatch
from .forms import CricketMatchForm

def schedule_cricket_match(request):
    if request.method == "POST":
        form = CricketMatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:match_list")  # Redirect to match list page
    else:
        form = CricketMatchForm()
    
    return render(request, "core/schedule_cricket.html", {"form": form})

from django.shortcuts import render, get_object_or_404, redirect
from .models import ScheduledMatch
from .forms import MatchForm  # Make sure you have a form for scheduling matches

def edit_match(request, match_id):
    match = get_object_or_404(ScheduledMatch, id=match_id)
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect("core:match_list")  # Redirect back to match list after editing
    else:
        form = MatchForm(instance=match)

    return render(request, "core/edit_match.html", {"form": form, "match": match})

from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponseNotFound
from .models import ScheduledMatch

def delete_match(request, match_id):
    try:
        match = ScheduledMatch.objects.get(id=match_id)
        match.delete()
        return redirect("core:match_list")  # Redirect to match list after deletion
    except ScheduledMatch.DoesNotExist:
        return HttpResponseNotFound("Match not found.")

# core/views.py
# core/views.py
import json
import requests
import urllib.parse
import urllib3
from django.shortcuts import render
from .forms import PlayerSearchForm

# Disable SSL certificate warnings (for demo API with self-signed cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def player_stats(request):
    player_data = None
    player_name = request.GET.get('player_name')

    if player_name:
        player_name_encoded = urllib.parse.quote(player_name)
        try:
            response = requests.get(
                f"https://cricket-api-demo.up.railway.app/players/{player_name_encoded}",
                verify=False
            )
            if response.status_code == 200:
                player_data = response.json()
                print("API Response:", player_data)
            else:
                player_data = {'error': 'Failed to retrieve player data'}
        except requests.exceptions.RequestException as e:
            player_data = {'error': f'Error fetching data: {e}'}

    # Pass both form and JSON to template
    form = PlayerSearchForm(initial={'player_name': player_name})
    json_data = json.dumps(player_data) if player_data else 'null'

    return render(request, 'core/player_stats.html', {
        'form': form,
        'player_data': json_data
    })


