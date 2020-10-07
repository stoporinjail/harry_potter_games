FROM python:3.8



# Install app dependencies
RUN "pip install requests"


CMD [ "python", "launcher.py" ]
