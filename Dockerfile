FROM python:3.10.6
ADD apps/ .
RUN pip install boto3 requests
CMD ["python", "-u", "store_data.py"]