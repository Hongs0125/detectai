# Python 3 이미지를 기반으로 합니다.
FROM python:3.11.5

# /app 디렉토리를 Docker 컨테이너의 작업 디렉토리로 설정합니다.
WORKDIR /app

# 로컬 시스템의 requirements.txt 파일을 Docker 컨테이너의 현재 디렉토리(./)로 복사합니다.
COPY requirements.txt ./

# pip를 사용하여 requirements.txt에 명시된 Python 패키지들을 설치합니다.
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# 로컬 시스템의 나머지 소스 코드 파일들을 Docker 컨테이너의 현재 디렉토리로 복사합니다.
COPY . .

# Docker 컨테이너의 8000번 포트를 개방합니다.
EXPOSE 8000

# Docker 컨테이너가 시작될 때 Django 애플리케이션을 실행하는 명령어를 지정합니다.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]