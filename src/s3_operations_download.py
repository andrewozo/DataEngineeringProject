from auth import auth

def download_file(object_key, new_filename):
    s3_resource,s3_bucket = auth("../config.ini") 

    try:
        bucket = s3_resource.Bucket(s3_bucket)
        bucket.download_file(object_key,new_filename)
        return True
    except Exception as e:
        print(f'Error uploading file to s3: {str(e)}')
        return False
    

download_file('downloaded-data','downloaded.data.csv')