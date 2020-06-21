import os


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled6.settings")
    import django
    django.setup()

    from app01 import models
    from django.db.models import Avg

    ret=models.UserInfo.objects.values('de_nid').annotate(a=Avg('ada')).values('de_nid','a')
    print(ret)