from django.conf import settings
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


def email_confirm_redirect(request, key):
    return HttpResponseRedirect(
        f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{key}/"
    )


def password_reset_confirm_redirect(request, uidb64, token):
    return HttpResponseRedirect(
        f"{settings.PASSWORD_RESET_CONFIRM_REDIRECT_BASE_URL}{uidb64}/{token}/"
    )


from django.core.mail import EmailMessage


@api_view(('GET',))
def send_email(request):
    try:
        # email = EmailMessage(
        #     'Title',  # 이메일 제목
        #     'Content',  # 내용
        #     to=['gh06095@naver.com'],  # 받는 이메일
        # )
        # email.send()
        subject = "test"  # 타이틀
        to = ["gh06095@naver.com"]  # 수신할 이메일 주소
        from_email = "gh06095@naver.com"  # 발신할 이메일 주소
        message = "메세지 테스트"  # 본문 내용
        EmailMessage(subject=subject, body=message, to=to, from_email=from_email).send()
    except Exception as e:
        print(e)
        return Response(status=200, data=e)
    return Response(status=200)
