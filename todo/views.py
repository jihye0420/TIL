from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from todo.serializers import TodoSerializer
from todo.models import Todo

# from .response import response
# todo 조회, 등록, 수정, 삭제

class TodoView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TodoSerializer

    def post(self, request):
        # category = request.data['category']
        # get_user_id_1 = User.objects.get(email=request.user)
        # print(get_user_id_1)
        # get_user_id = get_object_or_404(User, email=request.user)
        # print(get_user_id)
        # print(type(get_user_id))
        # print(type(request.user))
        # # user_todo = Todo.objects.create(user_id=get_user_id, point=1)
        # user_todo = Todo(
        #     user_id=request.user,
        #     title=request.data['title'],
        #     category=request.data['title'],
        #     goal=request.data['goal'],
        #     is_alarm=request.data['is_alarm'],
        # )
        # user_todo.save()
        # return Response({"message": "투두가 생성되었습니다."}, status=status.HTTP_200_OK)

        print(request.user.user_id)
        print(request.data)
        request.data['user_id'] = request.user.user_id
        serializer = self.serializer_class(data=request.data)

        title = request.data['title']
        if Todo.objects.filter(title=title, user_id=request.user.user_id).exists():
            return Response({"message": "이미 존재하는 데이터입니다."}, status=status.HTTP_409_CONFLICT)

        if serializer.is_valid():
            serializer.save()
            res = {
                'status': 200,
                'data': serializer.data
            }
            return Response(
                data=res, status=status.HTTP_200_OK
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
