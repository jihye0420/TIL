from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.db import models


# Django에서는 기본적으로 사용자 모델인 User 모델을 제공
# -> 임의로 원하는 필드를 가진 사용자 모델을 사용하기 위해서 Custom User 모델 구현
class UserManager(BaseUserManager):  # 헬퍼 클래스
    # use_in_migrations = True

    def create_user(self, email, name, password):
        """
        주어진 이메일, 비밀번호 등 개인정보로 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have password')
        user = self.model(
            email=email,
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        superuser = self.create_user(
            email=email,
            name=name,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):  # 실제 모델을 상속받아 생성하는 클래스
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    name = models.CharField(max_length=30, null=False, unique=True)
    # firstName = models.CharField(max_length=30, null=False)
    # lastName = models.CharField(max_length=30, null=False)
    # country = models.CharField(max_length=30, null=True, default='', blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)

    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 nickname으로 설정
    USERNAME_FIELD = 'email'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'User'
