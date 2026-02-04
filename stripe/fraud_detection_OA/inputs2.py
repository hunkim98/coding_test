non_fraud_codes = "approved,invalid_pin,expired_card"
fraud_codes = "do_not_honor,stolen_card,lost_card"
mcc_thresholds = ["retail,0.5", "airline,0.25", "restaurant,0.8", "venue,0.25"]
merchant_mcc_map = ["acct_1,airline", "acct_2,venue", "acct_3,venue"]
min_charges = "3"
charges = [
    "CHARGE,ch_1,acct_1,100,do_not_honor",
    "CHARGE,ch_2,acct_1,200,approved",
    "CHARGE,ch_3,acct_1,300,do_not_honor",
    "CHARGE,ch_4,acct_2,400,approved",
    "CHARGE,ch_5,acct_2,500,approved",
    "CHARGE,ch_6,acct_1,600,lost_card",
    "CHARGE,ch_7,acct_2,700,approved",
    "CHARGE,ch_8,acct_2,800,approved",
    "CHARGE,ch_9,acct_3,800,approved",
    "CHARGE,ch_10,acct_3,700,approved",
    "CHARGE,ch_11,acct_3,600,approved",
    "CHARGE,ch_12,acct_3,500,stolen_card",
    "CHARGE,ch_13,acct_3,500,stolen_card",
    "CHARGE,ch_14,acct_2,400,stolen_card",
]
