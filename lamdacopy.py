import json
import boto3
import urllib 
import logging
import os
logger = logging.getLogger()
logger.setLevel(logging.INFO)
 
s3 = boto3.client('s3')
def lambda_handler(event, context):
    
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = str(urllib.unquote_plus(event['Records'][0]['s3']['object']['key']))
    #key = decodeURIComponent(keys.replace(/\+/g, " "))
    #key = str(event['Records'][0]['s3']['object']['key'])
    target_bucket = 'capalds'
    copy_source = {'Bucket':source_bucket, 'Key':key}
    
    s3.copy_object(Bucket=target_bucket, Key=key, CopySource = copy_source)
    #s3.meta.client.copy(copy_source,target_bucket,key)
    