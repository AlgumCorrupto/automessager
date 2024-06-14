FROM python
LABEL maintaner="ACpaulo"
COPY requirements requirements
COPY hello.py hello.py
COPY isSend isSend
COPY dbMan.py dbMan.py
COPY createDb.py createDb.py
COPY sender.py sender.py
RUN pip3 install -r requirements
RUN python3 createDb.py
CMD ["python3", "hello.py"]
