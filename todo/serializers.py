from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from todo.models import Todo, TodoDay


# class TodoDaySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TodoDay
#         fields = ['day']


# class TodoDaySerializer(serializers.ListSerializer):
#     day = serializers.CharField(max_length=3)
#
#     def create(self, validated_data):
#         return TodoDay.objects.create(**validated_data)


# class TodoDaySerializer(serializers.ListField):
#     child = serializers.CharField()



class TodoSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()
    # user_id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    # family_code = serializers.SerializerMethodField()
    # temporary_family_code = serializers.SerializerMethodField()
    test = serializers.SerializerMethodField()
    # day = TodoDaySerializer()
    # day = serializers.SerializerMethodField()
    day = serializers.ListField(required=False, child=serializers.CharField())
    # day = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def validate(self, attrs):
        # OrderedDict([('user_id', <User: gh06095@naver.com>), ('category', 'OF'), ('title', 'problem solving'), ('goal', 'Increase your problem-solving skills'), ('is_alarm', True)])
        # print(attrs)
        if 'test' not in attrs['title']:
            raise ValidationError('test가 없다 임마!')
        return attrs

    class Meta:
        model = Todo
        # fields = '__all__'
        fields = ['todo_id', 'user_id', 'category', 'title', 'goal', 'is_alarm', 'is_deleted', 'created_at',
                  'modified_at', 'test', 'name', 'day']
        # exclude = ('day', )

    def get_name(self, obj):
        print(obj)
        return obj.user_id.name

    def get_test(self, obj):
        print(obj)
        return 'test다 임마'

    # def get_day(self, obj):
    #     customer_account_query = TodoDay.objects.filter(todo_id=obj.todo_id)
    #     serializer = TodoDaySerializer(customer_account_query, many=True)
    #     return serializer.data

    def create(self, validated_data):
        print(validated_data)
        # print(**validated_data)
        days = validated_data.pop('day')
        print(days)
        todo = Todo.objects.create(**validated_data)
        print(todo)
        # TodoDay.objects.create(todo_id=todo, day=day)
        for day in days:
            TodoDay.objects.create(todo_id=todo, day=day)
        return todo

    # todo: update 구현해보기
