
from google_oauth2 import service_account
from googleapiclient.discovery import build



SERVICE_ACCOUNT_FILE = 'homework_43_2_7.json'

cred = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE,
    scopes=['https://www.googleapis.com/auth/spreadsheets']
)


google_sheet_id_users = '1CvXLIMUVnvlZiW3_tnt7FwmbTZxUKxZE-MxJkSTgpEQ'

service = build('sheets', 'v4', credentials=creds)