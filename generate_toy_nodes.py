"""
產出樣本節點資料
"""
import pandas as pd
from datetime import datetime


def save_as_parquet(table_dict):
    for title, table in table_dict.items():
        table.to_parquet(f'toy_data/nodes/{title}.parquet')


person = pd.DataFrame([[
    "1".zfill(40),
    "王大明",
    datetime(1993, 3, 3),
    "臺北市",
    "Y",
    "任職"
],
    [
    "2".zfill(40),
    "王老明",
    datetime(1973, 3, 3),
    "臺北市",
    "N",
    "非行員"
],
    [
    "3".zfill(40),
    "李大媽",
    datetime(1973, 3, 3),
    "臺北市",
    "N",
    "非行員"
],
    [
    "4".zfill(40),
    "王大哥",
    datetime(1992, 3, 3),
    "臺北市",
    "N",
    "非行員"
],
    [
    "5".zfill(40),
    "陳小美",
    datetime(1994, 3, 3),
    "臺北市",
    "N",
    "非行員"
],
    [
    "6".zfill(40),
    "陳岳父",
    datetime(1973, 3, 3),
    "臺北市",
    "N",
    "非行員"
],
    [
    "7".zfill(40),
    "李外公",
    datetime(1953, 3, 3),
    "臺北市",
    "N",
    "非行員"
],
    [
    "8".zfill(40),
    "王爺爺",
    datetime(1953, 3, 3),
    "臺北市",
    "N",
    "非行員"
],
    [
    "9".zfill(40),
    "王大明",
    datetime(1993, 3, 3),
    "臺北市",
    "Y",
    "任職"
],
    [
    "a".zfill(40),
    "陳大哥",
    datetime(1992, 3, 3),
    "臺北市",
    "N",
    "非行員"
]
], columns=[
    "node_id",
    "name",
    "birthdate",
    "birth_location",
    "is_customer",
    "esun_employ_status"
])
print("\nperson:\n", person.to_markdown())

company = pd.DataFrame([[
    "1".zfill(40),
    "O山銀行股份有限公司",
    "105",
    "臺灣",
    "TW"
],
    [
    "2".zfill(40),
    "王大明股份有限公司",
    "112",
    "臺灣",
    "TW"
]
], columns=[
    "node_id",
    "name",
    "zip",
    "foreignarea",
    "state"
])
print("\ncompany:\n", company.to_markdown())

phone = pd.DataFrame(
    [[
        "1".zfill(40),
        "0900000001"
    ]],
    columns=["node_id", "number"]
)
print("\nphone:\n", phone.to_markdown())

shop = pd.DataFrame(
    [[
        "1".zfill(40),
        "第一店"
    ]],
    columns=["node_id", "name"]
)
print("\nshop:\n", shop.to_markdown())

account = pd.DataFrame(
    [[
        "1".zfill(40),
        "Y",
        datetime(2023, 3, 3),
    ],
        [
        "2".zfill(40),
        "N",
        datetime(2023, 3, 3),
    ]
    ],
    columns=["node_id", "is_alert", "alert_date"]
)
print("\naccount:\n", account.to_markdown())


if __name__ == '__main__':
    save_as_parquet({
        "person": person,
        "company": company,
        "phone": phone,
        "shop": shop,
        "account": account
    })
