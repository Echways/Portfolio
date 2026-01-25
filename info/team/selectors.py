from info.models import TeamMember


def team_members_active():
    return TeamMember.objects.filter(is_active=True)
