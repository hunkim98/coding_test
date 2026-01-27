# Part 5: Specific Error Codes
# Expected output:
# VERIFIED: Pawsome Pets Inc.
# ERROR_MISSING_FIELDS: Bean Bliss Coffee
# ERROR_INVALID_LENGTH: Short Name
# ERROR_GENERIC_NAME: Generic Store
# ERROR_NAME_MISMATCH: Mismatched Corp

part = 5

csv_data = """col1,col2,col3,col4,col5,col6
BIZ001,Pawsome Pets Inc.,pawsomepets.com,Pawsome,PAWSOME PETS INC,Premium pet supplies
BIZ002,Bean Bliss Coffee,beanbliss.com,,,Artisan coffee roasters
BIZ003,Short Name,short.com,Short,SHRT,Products
BIZ004,Generic Store,generic.com,Store,RETAIL,Various items
BIZ005,Mismatched Corp,mismatch.com,Wrong,DIFFERENT BUSINESS,Services"""

is_input5 = True
