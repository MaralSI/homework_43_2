from Google_Sheets.config_sheets import service, google_sheet_id_users
from aiogram import Dispatcher, types

def update_google_sheet_products(fullname, age, address, phone, email):
    try:
        range_name = 'Sheet1!A:G'
        
        row = [fullname, age, address, phone, email]
        
        service.spreadsheets().values().append(
            spreadsheetId=google_sheet_id_users,
            range=range_name,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body={'values': [row]}
        ).execute()
        
        print(f'Данные - {row}')