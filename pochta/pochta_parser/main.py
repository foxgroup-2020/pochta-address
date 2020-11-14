from pochta_api.request import Request
from pochta_api.addr import Addr
import requests, json, os, csv
import pandas as pd
from pathlib import Path

GISPA_TOKEN = "53fb9daa-7f06-481f-aad6-c6a7a58ec0bb"
URL_QUERY = "https://address.pochta.ru/validate/api/v7_1"

ROOT_DIR = Path(__file__).resolve().parent.parent

EXAMPLE_PATH1 = Path(ROOT_DIR, 'files', 'input1.xls')
EXAMPLE_PATH2 = Path(ROOT_DIR, 'files', 'input2.csv')


def get_str_from_file(file_path, chunk_size):
    ext = Path(file_path).suffix[1:4]
    data = 's'
    if ext == 'csv':
        data = pd.read_csv(file_path, chunksize=chunk_size, encoding="utf-8", engine='python')
    elif ext == 'xls':
        data = pd.read_excel(file_path)
    return data


if __name__ == "__main__":
#     req = Request()
#     addr = Addr()
#
#     s = requests.session()
#     s.headers.update({'Content-Type': 'application/json'})
#     s.headers.update({'AuthCode': GISPA_TOKEN})
#     req = """{
# "version": "1.0.0",
# "fio": "Ivanov Ivan Ivanovich",
# "addr": [
# {
# "val": " ",
# "content": "C"
# },
# {
# "val": " ()",
# "stname": ".",
# "content": "R"
# },
# {
# "val": "-",
# "stname": "",
# "content": "A"
# },
# {
# "val": "",
# "stname": ".",
# "content": "P"
# },
# {
# "val": "",
# "stname": ".",
# "content": "S"
# },
# {
# "val": "28",
# "content": "N"
# }
# ]
# }"""
#     # ans = s.post(URL_QUERY, data=req)
#     print(ans)
#     print(ans.content.decode())
    d = get_str_from_file(EXAMPLE_PATH1, 100)
    print(pd.DataFrame(d))
