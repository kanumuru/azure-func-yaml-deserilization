import logging
from flask import Flask, request, render_template_string, render_template, redirect
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import azure.functions as func
import os, uuid
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the compromising of Azure functions and Storage Accounts!'


@app.route('/create')
@app.route('/create/<name>', methods=['POST', 'GET'])
def create(name=None):
    try:
        # Connect to Azure Storage
        connect_str = os.getenv("AzureWebJobsStorage")
        service_client = BlobServiceClient.from_connection_string(connect_str)
        container_name = "ase-sg-container"
        local_file_name = str(uuid.uuid4()) + ".txt"
        container_client = service_client.get_container_client(container=container_name)
        container_client.upload_blob(local_file_name,name)
        
        # logging.info('data inserted into blob container', container_name)
        return render_template_string(name+" data insertion  is successful")
    except Exception as e:
        logging.info('data insertion into blob container is unsuccessful', container_name)
        return render_template_string(name+" data insertion is unsuccessful")

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    page = req.params.get('page')
    logging.info('case 1: page = %s', page)

    with app.test_client() as c:
            doAction = {
                "GET": c.get(page).data,
                "POST": c.post(page).data
            }
            resp = doAction.get(req.method).decode()
            return func.HttpResponse(resp, mimetype='text/html')



