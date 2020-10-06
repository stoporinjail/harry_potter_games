FROM python:3
ADD launcher.py
RUN pip install requests
CMD [ "python", "launcher.py" ]
