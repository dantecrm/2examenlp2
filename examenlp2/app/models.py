from django.db import models
from django.contrib.auth.models import User

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

                    # TAREA

# 1.- Agregar el campo Description
# 2.- Registro de usuarios
# 3.- Estilos de Bootstrap3
# 4.- Agregar url view logout
