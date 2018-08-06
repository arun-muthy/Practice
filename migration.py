import logging
import os
#import cloudstorage
#import webapp2
from google.cloud import storage


def authentication_credentials():

    # service account credentials
    storage_client = storage.Client.from_service_account_json('arun1-208313-dac17292ba06.json')

    def create_bucket(bucket_name):
        bucket = storage_client.create_bucket(bucket_name)
        print('Bucket {} created'.format(bucket.name))

    #create_bucket()

    def upload_blob(bucket_name, source_file_name, destination_blob_name):

        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('file {} uploaded to {}.'.format(source_file_name, destination_blob_name))

    upload_blob('twitterbucket1', 'tweet.csv', 'tweet1.csv')

    #authenticated AP1 request
    buckets = list(storage_client.list_buckets())
    print(buckets)

authentication_credentials()



# clients x
# buckets x
# json key x
# assign role to user x
# storage admin
# roles/storage.admin
# json to shell
# ccreate storage client pass it key
# stopping stream / timed session
# emoji issues



