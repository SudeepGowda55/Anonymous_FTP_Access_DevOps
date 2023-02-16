# FROM python:3.8-slim

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# WORKDIR /app
# COPY . .
# # RUN python -m pip install -r requirements.txt

# # Creates a non-root user with an explicit UID and adds permission to access the /app folder
# # RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# # USER appuser

# # During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python", "main.py"]

# Multi Staged Dockerfile
FROM rust:latest as builder

WORKDIR /app
COPY . .

RUN cargo build --release

FROM debian:buster-slim

COPY --from=builder ./target/release/guessing_game ./guessing_game

CMD [ "./guessing_game" ]