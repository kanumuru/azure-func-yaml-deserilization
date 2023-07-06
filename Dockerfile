FROM mcr.microsoft.com/azure-functions/python:4-python3.8
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    AzureFunctionsJobHost__Logging__Console__IsEnabled=true
COPY . /HttpExample
WORKDIR /HttpExample
RUN pip install -r requirements.txt

COPY . /home/site/wwwroot