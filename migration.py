import logging
import os
#import cloudstorage as gcs
#import webapp2
from google.cloud import storage




storage_client = storage.Client.from_service_account_json('C:/Users/709229/PycharmProjects/Cloudpy/Arun1-02c764d57145.json')



def authentication_credentials():


    #service account credentials
    storage_client = storage.Client.from_service_account_json('C:/Users/709229/PycharmProjects/Cloudpy/Arun1-02c764d57145.json')

    # def create_bucket(bucket_name):
    #      storage_client = storage.Client()
    #      bucket = storage_client.create_bucket(bucket_name)
    #      print('Bucket {} created '.format(bucket.name))
    #
    # create_bucket('new_twitter_bucket')


    def upload_blob(bucket_name, source_file_name, destination_blob_name):
        #storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('file {} uploaded to {}.'.format(source_file_name, destination_blob_name))

    upload_blob('twitterbucket1', 'tweet.csv', 'tweet.csv')

    #authenticated AP1 request
    buckets = list(storage_client.list_buckets())
    print(buckets)

    def upload_blob(bucket_name, source_file_name, destination_blob_name):
        #storage_client = storage.Client()
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print('file {} uploaded to {}.'.format(source_file_name, destination_blob_name))

    upload_blob('twitterbucket1', 'tweet.csv', 'tweet.csv')

authentication_credentials()

# def upload_blob(bucket_name,source_file_name,destination_blob_name):
#
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)
#
#     blob.upload_from_filename(source_file_name)
#
#     print('file {} uploaded to {}.'.format(source_file_name,destination_blob_name))
#
#
# upload_blob('twitterbucket1','tweet.csv','https://console.cloud.google.com/storage/browser/twitterbucket1')


#     clients
# buckets
# json key
# assign role to user
# storage admin
# roles/storage.admin
# json to shell
# ccreate storage client pass it key
# stopping stream / timed session
# emoji issues



