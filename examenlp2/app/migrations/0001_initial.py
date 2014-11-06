# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


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
    ]
