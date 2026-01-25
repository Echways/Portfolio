from info.models import Achievement


def achievements_list():
    return Achievement.objects.all()
