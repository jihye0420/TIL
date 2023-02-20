from django.db import models

from users.models import User


class BaseModel(models.Model):
    '''
    수정 시간, 생성 시간 모델
    '''
    created_at = models.DateTimeField(auto_now_add=True)  # 해당 레코드 생성시 현재 시간 자동저장
    modified_at = models.DateTimeField(auto_now=True)  # 해당 레코드 갱신시 현재 시간 자동저장

    class Meta:
        abstract = True  # 상속


# todo : basemodel 구현해서 만들어보기 (https://velog.io/@bjo6300/Django-%EC%83%81%EC%86%8D-model-%EC%A0%81%EC%9A%A9%ED%95%98%EA%B8%B0)
class Todo(models.Model):
    CATEGORIES = (
        ('OFFICE', 'OFFICE'),
        ('STUDY', 'STUDY'),
        ('IMPORTANT', 'IMPORTANT'),
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


class TodoDay(models.Model):
    DAYS = (
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    )
    todo_day_id = models.AutoField(primary_key=True)
    day = models.CharField(max_length=3, choices=DAYS)
    todo_id = models.ForeignKey(Todo, db_column='todo_id', on_delete=models.CASCADE, related_name='routine_day')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'TodoDay'
