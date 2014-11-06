# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from timezone_field import TimeZoneField
from django.conf import settings

class UserProfile(models.Model):
    DOC = (
        (1, 'DNI'),
        (2, 'VISA'),
        (3, 'RUC'),
    )

    avatar = models.ImageField(upload_to='avatar')  # Pil --> Pillow
    user = models.OneToOneField(User)
    documento = models.PositiveSmallIntegerField(choices=DOC, default=1)
    departamento = models.CharField(max_length=20, verbose_name="Departamento")
    distrito = models.CharField(max_length=20, verbose_name="Departamento")
    provincia = models.CharField(max_length=20, verbose_name="Provincia")
    time_zone = TimeZoneField(default=settings.TIME_ZONE)

    def __unicode__(self):
        return self.user.username


class Todo(models.Model):
    PRIORITY_LIST = (
        (0, 'Low'),
        (5, 'Normal'),
        (10, 'High'),
        (15, 'Urgent'),
    )
    title = models.CharField(max_length=40)
    description = models.TextField()
    owner = models.ForeignKey(User)
    priority = models.PositiveSmallIntegerField(choices=PRIORITY_LIST, default=5)
    added_on = models.DateTimeField(auto_now_add=True)
    due_on = models.DateField()

    class Meta:
        permissions = (
            ('list_app', 'Can view list ap'),
            ('view_app', 'Can view ap'),
            ('add_app', 'Can add ap'),
            ('change_app', 'Can change ap'),
            ('delete_app', 'Can delete ap'),
        )
        ordering = ['due_on']


    def __unicode__(self):
        return u"%s" % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('app_detail', [int(self.pk)])
