from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Student


@receiver(post_save, sender=Student)
def post_save(created, **kwargs):
    instance = kwargs["instance"]
    if created:
        print(f"Ученик {instance.name} создан")
    else:
        print(f"ученик {instance.name} обновлен")
