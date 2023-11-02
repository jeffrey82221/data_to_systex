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

print("\nhas_father:\n", has_father.to_markdown())

has_mother = pd.DataFrame([[
    "1".zfill(40),
    "3".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_mother:\n", has_mother.to_markdown())

has_siblings = pd.DataFrame([[
    "1".zfill(40),
    "4".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_siblings:\n", has_siblings.to_markdown())

has_spouse = pd.DataFrame([[
    "1".zfill(40),
    "5".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_spouse:\n", has_spouse.to_markdown())


has_parents_in_law = pd.DataFrame([[
    "1".zfill(40),
    "6".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_parents_in_law:\n", has_parents_in_law.to_markdown())

has_maternal_grandparents = pd.DataFrame([[
    "1".zfill(40),
    "7".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_maternal_grandparents:\n", has_maternal_grandparents.to_markdown())

has_paternal_grandparents = pd.DataFrame([[
    "1".zfill(40),
    "8".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_paternal_grandparents:\n", has_paternal_grandparents.to_markdown())

is_fa_of = pd.DataFrame([[
    "1".zfill(40),
    "8".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nis_fa_of:\n", is_fa_of.to_markdown())

id_change = pd.DataFrame([[
    "1".zfill(40),
    "9".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nid_change:\n", id_change.to_markdown())

has_spouse_siblings = pd.DataFrame([[
    "1".zfill(40),
    "a".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_spouse_siblings:\n", has_spouse_siblings.to_markdown())


#######################
## PERSON -> COMPANY ##
#######################

works_for = pd.DataFrame([[
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nworks_for:\n", works_for.to_markdown())

in_charge = pd.DataFrame([[
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nin_charge:\n", in_charge.to_markdown())

######################
# COMPANY -> COMPANY #
######################

supply = pd.DataFrame([[
    "1".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nsupply:\n", supply.to_markdown())

invest = pd.DataFrame([[
    "2".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\ninvest:\n", invest.to_markdown())


#####################
# PERSON -> ACCOUNT #
#####################

has_account = pd.DataFrame([[
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 3)
]], columns=common_columns)

print("\nhas_account:\n", has_account.to_markdown())

######################
# COMPANY -> ACCOUNT #
######################

company_has_account = pd.DataFrame([[
    "2".zfill(40),
    "2".zfill(40),
    datetime(2023, 11, 3)
]], columns=common_columns)

print("\ncompany_has_account:\n", company_has_account.to_markdown())


###################
# PERSON -> PHONE #
###################

has_phone = pd.DataFrame([[
    "1".zfill(40),
    "1".zfill(40),
    datetime(2023, 11, 2)
]], columns=common_columns)

print("\nhas_phone:\n", has_phone.to_markdown())


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

print("\nregister:\n", register.to_markdown())

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

print("\ntransaction:\n", transaction.to_markdown())


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

print("\nbuy_at:\n", buy_at.to_markdown())


if __name__ == '__main__':
    save_as_parquet(
        {
            "has_father": has_father,
            "has_mother": has_mother,
            "has_siblings": has_siblings,
            "has_spouse": has_spouse,
            "has_parents_in_law": has_parents_in_law,
            "has_maternal_grandparents": has_maternal_grandparents,
            "has_paternal_grandparents": has_paternal_grandparents,
            "is_fa_of": is_fa_of,
            "id_change": id_change,
            "has_spouse_siblings": has_spouse_siblings,
            "works_for": works_for,
            "in_charge": in_charge,
            "supply": supply,
            "invest": invest,
            "has_account": has_account,
            "company_has_account": company_has_account,
            "has_phone": has_phone,
            "register": register,
            "transaction": transaction,
            "buy_at": buy_at
        }
    )