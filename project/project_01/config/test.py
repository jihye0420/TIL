# Build paths inside the project like this: BASE_DIR / 'subdir'.
import os
from pathlib import Path

import environ

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

'''
2. 각 호출자가 기본 매개변수를 전달할 필요가 없도록 환경 변수의 체계 기반 조회를 제공합니다.
라고 번역하니 나와있는데, 무슨말인지 생각해보니 환경변수를 불러올 수 있는 상태로 세팅한다고
이해했다. 
'''
env = environ.Env(DEBUG=(bool, True))

'''
3. 환경변수를 읽어올 준비는 마쳤고, 어떤 파일에서 불러올건지 정해줘야 하기 때문에
나는 '.env'에서 가져올거라고 설정해줬다.
'''
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

SECRET_KEY = env('SECRET_KEY')
print(BASE_DIR)
print(SECRET_KEY)