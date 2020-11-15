import requests, json, os, csv, xlrd
import pandas as pd
from pathlib import Path
import psycopg2

GISPA_TOKEN = "53fb9daa-7f06-481f-aad6-c6a7a58ec0bb"
URL_QUERY = "https://address.pochta.ru/validate/api/v7_1"
HEADERS = {'Content-type': 'application/json',  # Определение типа данных
               'AuthCode': '53fb9daa-7f06-481f-aad6-c6a7a58ec0bb',
               'Content-Encoding': 'utf-8'}


ROOT_DIR = Path(Path(__file__).resolve().parent.parent, 'media')

def get_file_path():
    # path to file - list
    conn = psycopg2.connect(dbname='pochta', user='django',
                            password='password', host='localhost')
    paths_to_files = []
    with conn.cursor() as cursor:
        cursor.execute('SELECT file_path, id FROM public.pochta_main_fileparse WHERE result = false')
        for row in cursor:
            paths_to_files.append(row)
    return paths_to_files


def get_req_tmpl():
    return {
        "version": "1.0.0",
        "addr": [
            {
                "val": ""
            }
        ]
    }


def save_info_file(file_path):
    excel_data_file = xlrd.open_workbook(Path(ROOT_DIR,file_path))
    sheet = excel_data_file.sheet_by_index(0)
    row_number = sheet.nrows
    conn = psycopg2.connect(dbname='pochta', user='django',
                            password='password', host='localhost')
    with conn.cursor() as cursor:
        res = cursor.execute('UPDATE public.pochta_main_fileparse SET all_record=%s WHERE all_record=0 AND file_path=%s', (row_number, file_path))
        conn.commit()
    return row_number

def save_current_record(file_path, cur_record):
    conn = psycopg2.connect(dbname='pochta', user='django',
                            password='password', host='localhost')
    with conn.cursor() as cursor:
        res = cursor.execute(
            'UPDATE public.pochta_main_fileparse SET current_record=%s WHERE file_path=%s', (cur_record, file_path))
        conn.commit()
    return None

def get_not_normal_address(file_path):
    # (nn_addr - str - not normalize addr, pos - int - position in file)

    excel_data_file = xlrd.open_workbook(Path(ROOT_DIR,file_path))
    sheet = excel_data_file.sheet_by_index(0)  # обращение к нулевой странице

    all_sheets = []
    row_number = sheet.nrows  # количество строк на странице

    if row_number > 0:  # если есть то входим
        for row in range(1, row_number):
            all_sheets.append(str(sheet.row(row)[0]).replace("text:", "").replace("'", ""))

    for i, row_str in enumerate(all_sheets):  # Перебираем адреса из excel
        yield (i, row_str)

def update_addr(nn_addr):
    return nn_addr

def send_api_request(nn_addr):
    # (n_addr - str - normalize addr, state - int )
    data = get_req_tmpl()
    data['addr'][0]["val"] = nn_addr
    answer = requests.post(URL_QUERY, data=json.dumps(data), headers=HEADERS)
    response = answer.json()
    return response

def save_to_db(nn_addr, n_addr, state, file_id):
    conn = psycopg2.connect(dbname='pochta', user='django',
                            password='password', host='localhost')
    with conn.cursor() as cursor:
        res = cursor.execute('INSERT into public.pochta_main_fileresult (source_addr, get_addr, state, file_source_id)\
         VALUES (%s, %s, %s, %s)',  (nn_addr, n_addr, state, file_id))
        conn.commit()
    return 0

if __name__ == "__main__":
    file_list = get_file_path()
    for file in file_list:
        print('Начата обработка файла {}'.format(file[0]))
        num_rows = save_info_file(file[0])
        for row_num, row in get_not_normal_address(file[0]):
            # save_current_record(file[0], row_num)
            print('Отправляется запрос по адресу: {}'.format(row))
            ans = send_api_request(row)
            outaddr = ans.get('addr').get("outaddr")
            state = ans.get('state')
            inaddr = ans.get('addr').get('inaddr')
            print('Сохраняется ответ в базу данных')
            save_to_db(inaddr, outaddr, state, file[1])