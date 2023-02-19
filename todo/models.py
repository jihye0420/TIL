from django.db import models

from users.models import User


class Todo(models.Model):
    CATEGORIES = (
        ('OF', 'OFFICE'),
        ('ST', 'STUDY'),
        ('IP', 'IMPORTANT'),
    )
    todo_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE, related_name='todo_user')
    category = models.CharField(max_length=10, choices=CATEGORIES)
    title = models.TextField(default='', null=True)
    goal = models.TextField(default='', null=True)
    is_alarm = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'Todo'
