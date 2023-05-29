# DRF views를 처리하는 방식
```
1. 전체 목록 조회 => GET tutorial/snippets (list)
2. 1개의 정보 등록 => POST tutorial/snippets (create)
3. 1개의 정보 조회 => GET tutorial/snippet/1 (retrieve)
4. 1개의 정보 수정 => PUT tutorial/snippet/1 (update)
5. 1개의 정보 삭제 => DELETE tutorial/snippet/1 (destroy)
```

## FBV : 함수형 뷰

- `@api_view(['GET', 'PUT', 'DELETE'])` : 데코레이터 사용한 방법, if문의 `request.method` 를 통한 분기 방법

```python
@api_view(['GET', 'POST'])
def snippet_list(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
```

## CBV : 클래스형 뷰

- `APIView` : request의 method마다 함수 작성

```python
class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None): # 함수로 요청에 대한 메소드 정의
```

## Mixins : 클래스형 뷰

- `APIView` 에서 중복되게 사용하는 시리얼라이저 코드 작성하는 것을 줄이기 위해 클래스 레벨에서 시리얼라이저 등록함

```python
class SnippetAPIMixins(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):  # mixins.ListModelMixin과 연결
```

```
1. 전체 목록 조회 => GET tutorial/snippets (list) => ListModelMixin
2. 1개의 정보 등록 => POST tutorial/snippets (create) => CreateModelMixin
3. 1개의 정보 조회 => GET tutorial/snippet/1 (retrieve) => RetrieveModelMixin
4. 1개의 정보 수정 => PUT tutorial/snippet/1 (update) => UpdateModelMixin
5. 1개의 정보 삭제 => DELETE tutorial/snippet/1 (destroy) => DestroyModelMixin
```

## Generics : 클래스형 뷰

- `Mixins` 을 조합해서 미리 만들어둔 일종의 mixins 세트

```
1. 전체 목록 => generics.ListAPIView
2. 생성  => generics.CreateAPIView
3. 1개 => generics.RetrieveAPIView
4. 1개 수정 => generics.UpdateAPIView
5. 1개 삭제 => generics.DestroyAPIView
6. 전체 목록 + 생성 => generics.ListCreateAPIView
7. 1개 + 1개 수정 => generics.RetrieveUpdateAPIView
8. 1개 + 1개 삭제 => generics.RetrieveDestroyAPIView
9. 1개 + 1개 수정 + 1개 삭제 => generics.RetrieveUpdateDestroyAPIView
```

- [generics.py](http://generics.py) 안의 내용 ⇒ mixins를 조합하기만 해놓은 코드

```python
class ListCreateAPIView(mixins.ListModelMixin,
                        mixins.CreateModelMixin,
                        GenericAPIView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
```

## Viewset & Router : 클래스형 뷰
- 하나의 클래스가 하나의 URL을 담당하는 방식 → URL마다의 클래스를 만들고 각 클래스에서는 해당 URL로 들어오는 다양한 메소드를 처리
- queryset, serializer_class 부분이 겹침 → 하나의 클래스로 하나의 모델을 전부 처리해 줄 수 있으면 겹치는 부분이 없어질 것
- **Viewset = View의 Set ⇒ 뷰의 집합**

```python
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```

- [viewsets.py](http://viewsets.py) 안의 내용 ⇒ mixin을 기반으로 한 코드
```python
class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    pass
```