import streamlit as st
import boto3
from config_file import Config

st.write(f"Checking Bucket: {Config.BUCKET_NAME}")

s3_client = boto3.client('s3')
response = s3_client.list_objects_v2(Bucket=Config.BUCKET_NAME)
st.write(f"Response for: {response['Name']}")

for record in response['Contents']:
    st.write(record['Key'])
