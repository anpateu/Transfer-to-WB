from config import Config
from api_ozon import OzonAPI
import pandas as pd
import openpyxl


def change_name_for_WB(name):
    full_name = ''
    name = name.split(' ')
    for element in name:
        if len(full_name) + len(element) + 4 < 40:
            full_name += element + ' '
        else:
            break
    full_name += 'МТЗ'

    return full_name.replace('МТЗ МТЗ', 'МТЗ')

def create_file_for_import(api):
    offer_ids = []
    last_id = ''
    total = api.load_products('', 1, offer_ids)
    for k in range(total // 1000):
        offer_ids, last_id = api.load_products(last_id, 1000, offer_ids)
    offer_ids, last_id = api.load_products(last_id, 1000, offer_ids)

    wb = openpyxl.Workbook()
    wb.create_sheet(title='Upload', index=0)
    sheet = wb['Upload']
    sheet.append(['Номер карточки', 'Категория', 'Цвет', 'Бренд', 'Пол', 'Название', 'Артикул товара', 'Баркод товара',
                  'Цена', 'Состав', 'Описание', 'Высота упаковки', 'Артикул производителя', 'Ширина упаковки',
                  'Длина упаковки', 'Медиафайлы'])

    for i in range(len(offer_ids)):
        info = (api.check_info(offer_ids[i]))
        attributes = (api.check_attributes(offer_ids[i]))[0]

        media = ''
        images = attributes['images']
        for image in images:
            media += str(image['file_name']) + ','

        attributes_list = attributes['attributes']
        for attribute in attributes_list:
            if attribute['attribute_id'] == 7236:
                partnum = attribute['values'][0]['value']
            if attribute['attribute_id'] == 85:
                brand = attribute['values'][0]['value']

        offer_id = info['offer_id']
        price = int(float(info['price']) * 1.2)
        full_name = info['name']
        name = change_name_for_WB(full_name)
        height = round((float(attributes['height']) / 10) * 1.35, 2)
        width = round((float(attributes['width']) / 10) * 1.35, 2)
        depth = round((float(attributes['depth']) / 10) * 1.35, 2)

        sheet.append([i, 'Автозапчасти', '', brand, '', name, offer_id, '', price, '', full_name, height, partnum,
                         width, depth, media[:-1]])

    wb.save(f'wb_import.xlsx')


if __name__ == '__main__':
    api = OzonAPI(client_id=Config.OZON_CLIENT_ID, api_key=Config.OZON_API_KEY)
    create_file_for_import(api)