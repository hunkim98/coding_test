non_fraud_codes = "approved,invalid_pin,expired_card"
fraud_codes = "do_not_honor,stolen_card,lost_card"
mcc_thresholds = ["retail,5", "airline,2", "restaurant,10", "venue,3"]
merchant_mcc_map = ["acct_1,airline", "acct_2,venue", "acct_3,retail"]
min_charges = "0"
charges = [
    "CHARGE,ch_1,acct_1,100,do_not_honor",
    "CHARGE,ch_2,acct_1,200,approved",
    "CHARGE,ch_3,acct_1,300,do_not_honor",
    "CHARGE,ch_4,acct_2,100,lost_card",
    "CHARGE,ch_5,acct_2,200,lost_card",
    "CHARGE,ch_6,acct_2,300,lost_card",
    "CHARGE,ch_7,acct_3,100,lost_card",
    "CHARGE,ch_8,acct_2,200,stolen_card",
    "CHARGE,ch_9,acct_3,100,approved",
]
