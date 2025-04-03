from django.contrib import admin

# Register your models here.
from .models import Sport, Category, Post,Detail, Author, Team, CricketTeamMember,FootballTeamMember, Match,ScheduledMatch, Stadium

admin.site.register(Sport)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Detail)
admin.site.register(Author)
admin.site.register(Team)
admin.site.register(CricketTeamMember)
admin.site.register(FootballTeamMember)
admin.site.register(Match)
admin.site.register(ScheduledMatch)
admin.site.register(Stadium)
