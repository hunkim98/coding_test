# Part 1: Check for Missing Fields
# Expected output:
# VERIFIED: Pawsome Pets Inc.
# NOT VERIFIED: Bean Bliss Coffee
# NOT VERIFIED:
# VERIFIED: Tech Solutions

part = 1

csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,Pawsome Pets Inc.,pawsomepets.com,Pawsome,PAWSOME PETS INC,Premium pet supplies
BIZ002,Bean Bliss Coffee,beanbliss.com,,,Artisan coffee roasters
BIZ003,,,,,
BIZ004,Tech Solutions,techsol.io,Tech,TECH SOLUTIONS,Software consulting"""
