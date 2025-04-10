from django.urls import path, include


from . import views

app_name = 'core'
urlpatterns = [
   
    path('', views.index,  name='index'),
    path('register/cricket/', views.register_cricket, name='register_cricket'), 
    path("team-list/cricket/", views.cricket_team_list, name="cricket_team_list"),
    path('cricket/update/<int:player_id>/', views.update_cricket_player, name='update_cricket'),
    path('cricket/delete/<int:player_id>/', views.delete_cricket_player, name='delete_cricket'),

    path('register/football/', views.register_football, name='register_football'),  
    path("team-list/football/<str:team_name>/", views.football_team_list, name="football_team_list"),
    path("football/update/<int:player_id>/", views.update_football_player, name="update_cricket"),
    path("football/delete/<int:player_id>/", views.delete_football_player, name="delete_cricket"),

    path('schedule-match/', views.schedule_match, name='schedule_match'),
    path('match-list/', views.match_list, name='match_list'),
    path('match/edit/<int:match_id>/', views.edit_match, name='edit_match'),
    path('match/delete/<int:match_id>/', views.delete_match, name='delete_match'),
    path('schedule-match/cricket/', views.schedule_cricket_match, name='ScheduledMatch'),

    path('player-stats/', views.player_stats, name='player_stats'),

    path('live-matches/', views.live_matches, name='live_matches'),

    path('schedule/', views.match_schedule, name='match_schedule'),




















    path('sports/', views.sports, name='sports'),
    path('about/', views.about, name='about'),
    path('sports/<int:sport_id>/', views.sport, name='sport'),
    path('categories/', views.index, name='categories'),
    path('details/<int:detail_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),

    
     
]