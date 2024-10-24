from auth import auth

def upload_file(object_key, filename):
    s3_resource, s3_bucket = auth("../config.ini") 

    try:
        bucket = s3_resource.Bucket(s3_bucket)
        bucket.upload_file(f'{filename}',object_key)
        return True
    except Exception as e:
        print(f'Error uploading file to s3: {str(e)}')
        return False
    

upload_file("transaction_data.csv","transaction_data.csv")