# # For more information, please refer to https://aka.ms/vscode-docker-python
# FROM python:3.11.4-slim

# # Keeps Python from generating .pyc files in the container
# ENV PYTHONDONTWRITEBYTECODE=1

# # Turns off buffering for easier container logging
# ENV PYTHONUNBUFFERED=1

# # Install pip requirements
# COPY requirements.txt .

# ARG UID=100001

# RUN python -m pip install -r requirements.txt

# WORKDIR /app
# COPY . /app

# # Creates a non-root user with an explicit UID and adds permission to access the /app folder
# # For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app --uid "${UID}"
# USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python3", "main.py"]
FROM python:3.11.4-slim

ENV DVMN_TOKEN='36f751df1db82af2dec8405cdac049ac40586d4e'\
    TG_TOKEN='6476060098:AAHmNLVOYzTqpDTD58NCmvvMPbmaKdFwOF8'\
    CHAT_ID='669076138'

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser


RUN --mount=type=cache,target=/root/.cache/pip  \
    --mount=type=bind,source=requirements.txt,target=requirements.txt  \
    python -m pip install -r requirements.txt

USER appuser

COPY . /app

# adding port
EXPOSE 3000

CMD ["python3", "main.py"]