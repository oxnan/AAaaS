FROM python:3.8-slim-buster
RUN pip install quart hypercorn requests bs4 duckduckgo-images-api pillow
WORKDIR /
COPY ./server.py .
COPY ./index.html /templates/index.html
COPY ./failed.html .
COPY ./ddgapi.py .
COPY ./ascify.py .
COPY ./README.md .
CMD ["hypercorn", "--bind", "0.0.0.0:80", "server:app"]
