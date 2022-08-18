[프로젝트 구성]
- 프로젝트명: conversation
- python 버전: 3.8.10
- 가상환경 명령어
 . python -m venv conv
 . 가상환경 활성화: conv\Scripts\activate 
 . 활성화 후 실행해야 동일한 환경에서 진행 가능
- backend 생성
 . python -m django startproject backend
 . python manage.py migrate
 . python manage.py createsuperuser (chryred/1)
 . pip install -r requirements/dev.txt
- yarn 설치
 . npm install --global yarn
- react설치
 . yarn create react-app fronend
 . yarn start
- 그외 장고 실행 명령어
 . 서버 기동: python manage.py runserver
 . 모델 객체 생성: python manage.py makemigrations 앱이름 or 전체시 공란
 . 모델 객체 생성 적용: python manage.py migrate 앱이름 or 전체시 공란
 

