from django.db import models
from users.models import User


class Routine(models.Model):
    CATEGORIES = (
        ('MC', 'MIRACLE'),
        ('HW', 'HOMEWORK')
    )
    routine_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete=models.CASCADE, related_name='routine_user')
    title = models.TextField(default='', null=True)
    category = models.CharField(max_length=2, choices=CATEGORIES)
    goal = models.TextField(default='', null=True)
    is_alarm = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'Routine'


class RoutineResult(models.Model):
    RESULTS = (
        ('N', 'NOT'),
        ('T', 'TRY'),
        ('D', 'DONE'),
    )
    routine_result_id = models.AutoField(primary_key=True)
    routine_id = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_result')
    result = models.CharField(max_length=1, choices=RESULTS)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'RoutineResult'


class RoutineDay(models.Model):
    DAYS = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    )
    day = models.CharField(max_length=3, choices=DAYS)
    routine_id = models.ForeignKey(Routine, on_delete=models.CASCADE, related_name='routine_day')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'RoutineDay'
