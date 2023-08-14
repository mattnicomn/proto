import boto3

s3 = boto3.client('s3')

def lamnda_handler(event, context)

  count = 0
  response =s3.list_objects_v2(bucket=event['bucket'])

  if 'Contents' in response:
    for object in response['Contents']:
      if object['Key'][-1] != '/':
        count += 1
  return("Number of files: ", count)

#https://stackoverflow.com/questions/42673764/boto3-s3-get-files-without-getting-folders
