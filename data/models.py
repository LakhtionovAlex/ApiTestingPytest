import csv

from api.categories import categories_api
from api.admin import kazi_admin_api
from api.products import products_api


def extract_all_ids(data):
    ids = []
    for item in data:
        ids.append(item['id'])
        if 'nested_categories' in item and item['nested_categories']:
            ids.extend(extract_all_ids(item['nested_categories']))
    return ids


def get_all_id_categories():
    res = categories_api.categories_list()
    res_body = res.json()
    all_ids = extract_all_ids(res_body)
    return all_ids


def road_csv_file_create_category(file_path):
    with open(file_path, 'r') as csvfile:
        read = csv.DictReader(csvfile)
        for row in read:
            yield row['title'], row['parent_id'], row['description']


def road_csv_file_update_category(file_path):
    with open(file_path, 'r') as csvfile:
        read = csv.DictReader(csvfile)
        for row in read:
            yield row['title'], row['description']


def get_all_id_tags(token):
    res = kazi_admin_api.kazi_admin_tags_list(token).json()
    all_ids = []
    for item in res:
        all_ids.append(item['id'])
    return all_ids


def get_all_id_product():
    res = products_api.products_list().json()
    ids = [item['id'] for item in res['results']]
    return ids
