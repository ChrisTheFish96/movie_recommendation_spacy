FROM pypy:latest
COPY movies.txt movies.txt
RUN pip3 install requests spacy
WORKDIR /app
COPY . /app
CMD python watch_next.py