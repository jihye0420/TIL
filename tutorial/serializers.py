from rest_framework import serializers

from tutorial.models import Snippet


# ModelSerializer : 자동으로 결정된 fields
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
# 
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         # Snippet 객체를 리턴 => serializer로 json <-> 파이썬 객체로 직렬화, 역직렬화
#         """
#         print(validated_data)
#         # todo: 왜 **이 붙는지 확인하기
#         return Snippet.objects.create(**validated_data)
# 
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         # 존재하는 Snippet 객체를 validated_data로 리턴
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance
