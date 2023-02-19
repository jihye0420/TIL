from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()
    # user_id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    # family_code = serializers.SerializerMethodField()
    # temporary_family_code = serializers.SerializerMethodField()
    test = serializers.SerializerMethodField()

    def validate(self, attrs):
        # OrderedDict([('user_id', <User: gh06095@naver.com>), ('category', 'OF'), ('title', 'problem solving'), ('goal', 'Increase your problem-solving skills'), ('is_alarm', True)])
        print(attrs)
        if 'test' not in attrs['title']:
            raise ValidationError('test가 없다 임마!')
        return attrs

    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['todo_id', 'user_id', 'category', 'title', 'goal', 'is_alarm', 'test', 'name']

    # def get_token(self, obj):
    #     # 튜플
    #     token, created = Token.objects.get_or_create(user=obj.user)
    #     return token.key

    def get_name(self, obj):
        print(obj)
        return obj.user_id.name

    # def get_family_code(self, obj):
    #     return obj.family.code if obj.family is not None else None
    #
    # def get_temporary_family_code(self, obj):
    #     return obj.temporary_family_code.code if obj.temporary_family_code is not None else None

    def get_test(self, obj):
        print(obj)
        return 'test다 임마'
