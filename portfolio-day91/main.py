import pdfplumber
import boto3
import os
from botocore.config import Config


PDF_FILE_PATH = "./data/sample.pdf"
aws_access_key_id = "AKIA6GBMCNYYNELTL7XC"
aws_secret_access_key = "RKLxjMUKl+hL7KIBPKNGy5D2mV/DSa5BHk9JkES/"

os.environ['AWS_DEFAULT_REGION'] = 'ap-northeast-2'
os.environ['AWS_DEFAULT_REGION'] = aws_access_key_id
os.environ['AWS_DEFAULT_REGION'] = aws_secret_access_key

my_config = Config(
    region_name='ap-northeast-2'
    # signature_version='v4',
    # retries={
    #     'max_attempts': 10,
    #     'mode': 'standard'
    # }
)

s3 = boto3.resource('s3', config=my_config, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
client = boto3.client('polly', config=my_config, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# region=us-east-1

# def synthesize(text, engine, voice, audio_format, lang_code=None):
#     kwargs = {
#         "Engine": engine,
#         "OutputFormat": audio_format,
#         "Text": text,
#         "VoiceId": voice,
#     }
#     if lang_code is not None:
#         kwargs["LanguageCode"] = lang_code
#     response = client.synthesize_speech(**kwargs)
#     # return response
#
#
# synthesize('hello', 'standard', 'Aditi', 'string', 'ko-KR')

# response = client.synthesize_speech(
#     Engine='standard',
#     LanguageCode='ko-KR',
#     # LexiconNames=[
#     #     'example',
#     # ],
#     OutputFormat='mp3',
#     SampleRate='8000',
#     # SpeechMarkTypes=['word'],
#     Text='All Gaul is divided into three parts',
#     TextType='text',
#     VoiceId='Joanna'
# )

response = client.start_speech_synthesis_task(
                VoiceId='Joanna',
                OutputS3BucketName='synth-books-buckets',
                OutputS3KeyPrefix='key',
                OutputFormat='mp3',
                Text='This is a sample text to be synthesized.',
                Engine='neural')

taskId = response['SynthesisTask']['TaskId']

print( "Task id is {} ".format(taskId))

task_status = client.get_speech_synthesis_task(TaskId=taskId)

print(task_status)

# response = client.get_lexicon(
#     Name='',
# )

# response = client.describe_voices(
#     LanguageCode='en-GB',
# )

# print(response)
#
# file = open('speech.mp3', 'wb')
# file.write(response['AudioStream'].read())
# file.close()

# pdf = pdfplumber.open(PDF_FILE_PATH)
# pages = pdf.pages
# text = ""
# for page in pages:
#     sub = page.extract_text()
#     text += sub
# print(text)
