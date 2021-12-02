# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 08:39:12 2021

@author: ayano
"""

import random

import ipywidgets as widgets

# ボタンが押されたときの処理
def on_button_clicked(b):
    birthvalue = birthdate.value
    constella = calc_constellation(birthvalue)
    print('今日の' + constella + 'の運勢は' + fortune_result())

# 入力された日付の星座を判定する
def calc_constellation(x):
    constellation = {1 : 'やぎ座', 2 : 'みずがめ座', 3 : 'うお座', 4 : 'おひつじ座',
                     5 : 'おうし座', 6 : 'ふたご座', 7 : 'かに座', 8 : 'しし座',
                     9 : 'おとめ座', 10 : 'てんびん座', 11 : 'さそり座', 12 : 'いて座'}
    if x.day > 22:
        if x.month == 12:
            return constellation[1]
        else:
            return constellation[x.month + 1]
    else:
        return constellation[x.month]
    
# 運勢結果を出す
def fortune_result():
    num = random.randint(1, 12)
    if num < 5:
        return '最悪です…。外食は控えた方が吉。'
    elif num < 9:
        return '可もなく不可もなし。たくさん運動しよう！'
    else:
        return '最高です！いいことがあるかも！'
        
# 誕生日
birthdate = widgets.DatePicker(
    disabled=False
)

# 占うボタン
button = widgets.Button(description="占う") 
# ボタンが押されたときの処理
button.on_click(on_button_clicked)

print('誕生日を入力してください。')
display(birthdate)
display(button)