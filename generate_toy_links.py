import pandas as pd
from datetime import datetime


def save_as_parquet(table_dict):
    for title, table in table_dict.items():
        table.to_parquet(f'toy_data/links/{title}.parquet')

######################
## PERSON -> PERSON ##
######################

common_columns = [
    "from",
    "to",
    "link_dt"
]
has_father = pd.DataFrame([[
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_father:\n", has_father.to_markdown())

has_mother = pd.DataFrame([[
    "1".zfill(40),
    "3".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_mother:\n", has_mother.to_markdown())

has_siblings = pd.DataFrame([[
    "1".zfill(40),
    "4".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_siblings:\n", has_siblings.to_markdown())

has_spouse = pd.DataFrame([[
    "1".zfill(40),
    "5".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_spouse:\n", has_spouse.to_markdown())


has_parents_in_law = pd.DataFrame([[
    "1".zfill(40),
    "6".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_parents_in_law:\n", has_parents_in_law.to_markdown())

has_maternal_grandparents = pd.DataFrame([[
    "1".zfill(40),
    "7".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_maternal_grandparents:\n", has_maternal_grandparents.to_markdown())

has_paternal_grandparents = pd.DataFrame([[
    "1".zfill(40),
    "8".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_paternal_grandparents:\n", has_paternal_grandparents.to_markdown())

is_fa_of = pd.DataFrame([[
    "1".zfill(40),
    "8".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("is_fa_of:\n", is_fa_of.to_markdown())

id_change = pd.DataFrame([[
    "1".zfill(40),
    "9".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("id_change:\n", id_change.to_markdown())

has_spouse_siblings = pd.DataFrame([[
    "1".zfill(40),
    "a".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_spouse_siblings:\n", has_spouse_siblings.to_markdown())


#######################
## PERSON -> COMPANY ##
#######################

works_for = pd.DataFrame([[
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("works_for:\n", works_for.to_markdown())

in_charge = pd.DataFrame([[
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("in_charge:\n", in_charge.to_markdown())

######################
# COMPANY -> COMPANY #
######################

supply = pd.DataFrame([[
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("supply:\n", supply.to_markdown())

invest = pd.DataFrame([[
    "2".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("invest:\n", invest.to_markdown())


#####################
# PERSON -> ACCOUNT #
#####################

has_account = pd.DataFrame([[
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 3)
]], columns=common_columns)

print("has_account:\n", has_account.to_markdown())

######################
# COMPANY -> ACCOUNT #
######################

company_has_account = pd.DataFrame([[
    "2".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 3)
]], columns=common_columns)

print("company_has_account:\n", company_has_account.to_markdown())


###################
# PERSON -> PHONE #
###################

has_phone = pd.DataFrame([[
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("has_phone:\n", has_phone.to_markdown())


######################
# ACCOUNT -> ACCOUNT #
######################

register = pd.DataFrame([[
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 2)
],
    [
    "2".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 2)
]
], columns=common_columns)

print("register:\n", register.to_markdown())

transaction = pd.DataFrame([[
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 3, 10, 10, 10),
    5000
],
    [
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 4, 10, 10, 10),
    10000
]
], columns=common_columns + ['twd_amt'])

print("transaction:\n", transaction.to_markdown())


##################
# PERSON -> SHOP #
##################

buy_at = pd.DataFrame([[
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 3, 10, 10, 10),
    500
],
    [
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 4, 10, 10, 10),
    1000
]
], columns=common_columns + ['twd_amt'])

print("buy_at:\n", buy_at.to_markdown())