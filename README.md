# mixpeek

<div align="center">

Package for using the Mixpeek api: file search for your software

</div>

## Quick start

### Install and import

1. Install the library

```bash
pip install mixpeek
```

2. Request an API key

[On the website](https://mixpeek.com)

### Write your code

1. Import your modules

```python
from mixpeek import mixpeek
```

2. Instantiate the module:

```python
mix = Mixpeek(
    api_key="my-api-key"
)
```

3. Upload a file:

```python
mix.upload(file_name="my-file-name.pdf", file_path="/tmp/my-file-name.pdf")
```

4. Now search:

```python
mix.search(query="my search query")
```

### Integrations

#### S3

```python
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
```

### Articles:

- [Add search to your S3 bucket’s non-text files](https://medium.com/@mixpeek/add-search-to-your-s3-buckets-non-text-files-9a676452b4fd)

### 🚀 Features

- Supports for `Python 3.8` and higher.
- Full text search
- AWS S3 Integration
- Fuzzy text matching
