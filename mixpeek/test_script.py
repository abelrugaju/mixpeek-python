from mixpeek import Mixpeek, S3
from config import mixpeek_api_key, aws

def main():
    # aws test
    s3 = S3(
        aws_access_key_id=aws['aws_access_key_id'],
        aws_secret_access_key=aws['aws_secret_access_key'],
        region_name='us-east-2',
        mixpeek_api_key=mixpeek_api_key
    )
    # upload all
    s3.upload_all(bucket_name="mixpeek-demo")
    # upload one
    s3.upload_one(s3_file_name="prescription.pdf", bucket_name="mixpeek-demo")

    # -------

    # mixpeek api direct
    mix = Mixpeek(
        api_key=mixpeek_api_key
    )
    # search
    result = mix.search(query="ivermectin")
    print(result)

if __name__ == '__main__':
    main()
