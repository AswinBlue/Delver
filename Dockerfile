FROM python:3.10-slim-buster
# author
LABEL maintainer="aswindble@gmail.com"
# image가 설치 될 directory 로 이동
WORKDIR /app/server
COPY . .
# 의존성 모듈 설치
RUN pip3 install -r requirements.txt

# container가 구동되면 실행
ENTRYPOINT ["python", "main.py"]