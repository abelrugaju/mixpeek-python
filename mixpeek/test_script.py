from mixpeek import Mixpeek, S3

def main():
    # aws test
    s3 = S3()
    # upload all
    s3.upload_all(bucket_name="mixpeek-demo")
    # upload one
    s3.upload_one(s3_file_name="prescription.pdf", bucket_name="mixpeek-demo")

    mixpeek = Mixpeek()
    # search
    result = mixpeek.search(query="ivermectin")
    print(result)

if __name__ == '__main__':
    main()
