# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('priority', models.PositiveSmallIntegerField(default=5, choices=[(0, b'Low'), (5, b'Normal'), (10, b'High'), (15, b'Urgent')])),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('due_on', models.DateField()),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['due_on'],
                'permissions': (('list_app', 'Can view list ap'), ('view_app', 'Can view ap'), ('add_app', 'Can add ap'), ('change_app', 'Can change ap'), ('delete_app', 'Can delete ap')),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('avatar', models.ImageField(upload_to=b'avatar')),
                ('documento', models.PositiveSmallIntegerField(default=1, choices=[(1, b'DNI'), (2, b'VISA'), (3, b'RUC')])),
                ('departamento', models.CharField(max_length=20, verbose_name=b'Departamento')),
                ('distrito', models.CharField(max_length=20, verbose_name=b'Departamento')),
                ('provincia', models.CharField(max_length=20, verbose_name=b'Provincia')),
                (b'time_zone', timezone_field.fields.TimeZoneField(max_length=63)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
