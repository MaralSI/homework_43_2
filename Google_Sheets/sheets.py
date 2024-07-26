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
        
    except Exception as e:
        print(f'Ошибка при добавлении в таблицу - {e}')
        
        
def get_google_sheet_data():
    try:
        range_name = 'Sheet1!A:G'
        
        result = service.spreadsheets().values().get(
        spreadsheetId=google_sheet_id_users,
        range=range_name
        ).execute()
    
        rows = result.get('values', [])
    
        return rows

    except Exception as e:
        print(f' Error getting from Google Sheets - {e}')
        return[]
        
async def send_data(message: types.Message):
    data = get_google_sheet_data()
    
    if not data:
        await message.reply('Таблица пуста!')
        
    else:
        headers = data[0]
        response = 'Данные из Google Таблиц: \n\n'
        for row in data[1:]:
            for header, value in zip(headers,row):
                response += f"{header}: {value}\n"
            response += "\n"
            await message.reply(response)

def register_google_sheets(dp: Dispatcher):
    dp.register_message_handler(send_data, commands=['data_sheets'])        