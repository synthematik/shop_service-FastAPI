import asyncio
from contextlib import asynccontextmanager

from aiobotocore.session import get_session
from src.config import Settings

settings = Settings()


class S3Client:
    def __init__(self, access_key, secret_key, endpoint_url, bucket_name):
        self.config = {
            'aws_access_key_id': access_key,
            'aws_secret_access_key': secret_key,
            'endpoint_url': endpoint_url,
        }

        self.bucket_name = bucket_name

        self.session = get_session()

    @asynccontextmanager
    async def get_client(self):
        async with self.session.create_client('s3', **self.config) as s3_client:
            yield s3_client

    async def upload_file(self, file_path: str):
        object_name = file_path.split('/')[-1]
        async with self.get_client() as s3_client:
            with open(file_path, 'rb') as file:
                await s3_client.put_object(
                    Bucket=self.bucket_name,
                    Key=object_name,
                    Body=file,
                )


async def main():
    s3_client = S3Client(
        access_key=settings.get_access_key(),
        secret_key=settings.get_secret_key(),
        endpoint_url=settings.get_endpoint_url(),
        bucket_name=settings.get_bucket_name(),
    )

    await s3_client.upload_file('D:\\pythonProject\\shop-store\\static\\images\\products\\newbalance9060#1.jpg')


# яндекс:
# YCAJELtc2PqebYnYTx55HzNV2
# YCNfOyKyzvYMmk9on5RGwLsUiiX5NU5SrIMLFtIy

#cloud:
# 'a3d9695d-2616-4cbb-9da9-1cc153fdf611:7f0ecfab4c2edad27fb1548cb6aa4329'
# 'a1b59bf279b96442eb1bedaeba6222d6'

if __name__ == '__main__':
    asyncio.run(main())
