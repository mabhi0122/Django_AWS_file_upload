# Django File Upload with AWS S3 Integration
This project is a file upload system built using Django, where users can upload files that are stored in an AWS S3 bucket. The system also retrieves and displays files from S3 directly in the browser.

## Key Features:
File Upload: Users can upload various file types, which are securely stored in an AWS S3 bucket.
AWS S3 Configuration: Integrated Django with AWS S3 using boto3 and Django’s storages package.(boto3 and django-storages)
File Retrieval & Display: Uploaded files are retrieved from S3 and displayed in the browser using their S3 URLs.
Scalability & Security: AWS S3 provides scalable storage, and access control policies ensure secure file access.

## aws s3 configurations
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

AWS_STORAGE_BUCKET_NAME = 'djangofile-s3-bkt'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

AWS_S3_REGION_NAME = 'us-west-2'
AWS_S3_FILE_OVERWRITE = False


STORAGES = {

    # Media file (image) management   
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
    
    # CSS and JS file management
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
    },
}

This project improves efficiency by offloading file storage to AWS S3, reducing server load, and ensuring files are securely stored and accessible globally.
