from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from about.models import WorshipTeam
from cms.models import HomepageInfo

def worship(request):
    team = WorshipTeam.objects.get(pk=1)
    members = get_users_by_group(["Worship Team",])
    members = list(members)
    members.sort(key=lambda x: x.last_name)
    guest_members = get_users_by_group(["Guest Band Members",])
    guest_members = list(guest_members)
    guest_members.sort(key=lambda x: x.last_name)
    info = HomepageInfo.objects.get(pk=1)
    return render_to_response(
            'about/worship.html',
            {
                'request': request,
                'team': team,
                'members': members,
                'guest_members': guest_members,
                'info': info,
            },
            RequestContext(request)
    )

def get_users_by_group(groups):
    user_set = set()
    for group in groups:
        users = User.objects.filter(groups__name=group)
        for user in users:
            user_set.add(user)
    return user_set
