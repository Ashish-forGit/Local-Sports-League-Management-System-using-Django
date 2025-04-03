from django import forms
from .models import CricketTeamMember,FootballTeamMember

class CricketTeamMemberForm(forms.ModelForm):
    class Meta:
        model = CricketTeamMember
        fields = ['name', 'email', 'phone', 'position', 'image']

class FootballTeamMemberForm(forms.ModelForm):
    class Meta:
        model = FootballTeamMember
        fields = ['name', 'team', 'position', 'email', 'phone', 'image']


from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['sport', 'team_a', 'team_b', 'match_date', 'match_time', 'stadium']
        widgets = {
            'match_date': forms.DateInput(attrs={'type': 'date'}),
            'match_time': forms.TimeInput(attrs={'type': 'time'}),
        }

from django import forms
from .models import ScheduledMatch

class CricketMatchForm(forms.ModelForm):
    class Meta:
        model = ScheduledMatch
        fields = ["team_a", "team_b", "match_date", "match_time", "venue"]

from django import forms
from .models import ScheduledMatch

