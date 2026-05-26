FROM python:3.14

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt


# RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y && pip install --no-cache-dir --upgrade -r requirements.txt


COPY ./app /code/app


CMD ["fastapi", "run", "app/main.py", "--port", "80"]