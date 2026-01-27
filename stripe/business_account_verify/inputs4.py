# Part 4: Match Business Names (50% word overlap required)
# Expected output:
# VERIFIED: land water
# NOT VERIFIED: Acme Global Trading
# VERIFIED: Maple Ridge Bakery
# VERIFIED: Innovation Labs Inc

part = 4

csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,land water,landwater.com,land,land water LLC,Environmental services
BIZ002,Acme Global Trading,acme.com,Acme,XYZ ENTERPRISES,Import export services
BIZ003,Maple Ridge Bakery,maplebakery.com,Maple,MAPLE RIDGE BAKERY LLC,Artisan baked goods
BIZ004,Innovation Labs Inc,innovlabs.com,Labs,INNOVATION RESEARCH,R&D services"""
