# -*- coding: utf-8 -*-
"""Story config.
"""
################################################################
#
# Sample:
#
# 1) PERSONS
#       人物簡易設定
# 2) STAGES
#       舞台基本設定
# 3) DAYS
#       年月日設定
# 4) TIMES
#       時間帯基本設定
# 5) ITEMS
#       小道具設定
# 6) WORDS
#       辞書設定
# 7) RUBIS
#       ルビ設定
# 8) LAYERS
#       レイヤ設定
#
################################################################


PERSONS = (
        # Tag / 氏,名 / 歳 / 誕生日 / 性別 / 職業 / 呼称 / 紹介
        ("yuri", "ユーリィ", "コマロフ,ユーリィ", 24, (1,1), "male", "アーカイバ", "me:ボク"),
        ("kudo", "クド", "クドリャフカ", 5, (1,1), "male", "記録用ドローン", "me:ワタシ"),
        ("jas", "ジャスミン", "チェン,ジャスミン", 20, (1,1), "female", "図書館司書", "me:わたし"),
        ("rina", "リーナ", "", 20, (1,1), "female", "図書館司書", "me:わたし"),
        ("chen", "チェン", "チェン,ジャスミン", 30, (7,7), "female", "宇宙飛行士", "me:私"),
        ("andre", "アンドレ", "ヤン,アンドレ", 40, (1,1), "male", "宇宙飛行士", "me:私"),
        )

AREAS = (
        # Tag / 名前 / x,y / 備考
        ("Jakarta", "ジャカルタ", 10684,-620),
        )

STAGES = (
        # Tag / 名前 / 紹介
        ("library", "図書館"),
        ("highschool", "高校"),
        ("mosque", "モスク"),
        )

DAYS = (
        # Tag / 名前 / 月 / 日 / 年
        ("endday", "月落下事変", 7,7, 2098),
        ("visittown", "シティ訪問日", 11,29, 2108),
        ("voyagetown", "旅立つ日", 12,1, 2108),
        )

TIMES = (
        # Tag / 名前 / 時 / 分
        )

ITEMS = (
        # Tag / 名前 / 紹介
        )

WORDS = (
        # Tag / 名前 / 紹介
        )

RUBIS = (
        # Base / Rubi / Except / Type
        )

LAYERS = (
        # Key / Title / Words
        )

