# -*- coding:utf-8 -*-
import json
import os
import random
from uitls import format_text
from tqdm import tqdm


# data = json.load(open('data/raw/症状属性值.json', encoding='utf8'))
# data = data['RECORDS']
# train_list = []
# for item in tqdm(data):
#     if item['property_name'] not in ['中文名称', '英文名称', '发病部位']:
#         text = item['entity_name'] + '的' + item['property_name'] + '是' + item['property_value']
#         train_list.append(format_text(text))
#
# random.shuffle(train_list)
# train_writer = open('data/processed/train.txt', 'w', encoding='utf8')
# val_writer = open('data/processed/eval.txt', 'w', encoding='utf8')
# for idx, s in enumerate(train_list):
#     if idx < int(len(train_list) * 0.8):
#         train_writer.write(s + '\n')
#     else:
#         val_writer.write(s + '\n')




# data = json.load(open('data/raw/症状属性值.json', encoding='utf8'))
# data = data['RECORDS']
#
# demo_train = open('data/processed/demo_train.txt', 'w', encoding='utf8')
# demo_val = open('data/processed/demo_eval.txt', 'w', encoding='utf8')
# train_list = []
# for item in data:
#     if 256 < len(format_text(item['property_value'])) < 510:
#         train_list.append(format_text(item['property_value']))
#
# # print(len(train_list))
# random.shuffle(train_list)
# for idx, s in enumerate(train_list):
#     if idx < 8650:
#         demo_train.write(s + '\n')
#     else:
#         demo_val.write(s + '\n')


train_writer = open('data/processed/train.txt', 'w', encoding='utf8')
val_writer = open('data/processed/eval.txt', 'w', encoding='utf8')
file_names = os.listdir('data/raw')
count = 0
train_list = []
for file in file_names:
    data = json.load(open(os.path.join('data/raw', file), encoding='utf8'))
    data = data['RECORDS']
    for item in tqdm(data):
        if any(property in item['property_name'] for property in ['概述', '简介', '总述']) and 64 < len(format_text(item['property_value'])):
            count += 1
            # print(item['property_value'])
            text = format_text(item['property_value'])
            # print(text)
            # if '<img' in text:
            #     print('****'+text)
            train_list.append(text)

random.shuffle(train_list)
for idx, s in enumerate(train_list):
    if idx < 36000:
        train_writer.write(s + '\n')
    else:
        val_writer.write(s + '\n')
print(count)