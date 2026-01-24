non_fraud_codes = "approved,invalid_pin,expired_card"
fraud_codes = "do_not_honor,stolen_card,lost_card"
mcc_thresholds = ["retail,0.8", "venue,0.25"]
merchant_mcc_map = ["acct_1,retail", "acct_2,retail"]
min_charges = "2"
charges = [
    "CHARGE,ch_1,acct_1,100,do_not_honor",
    "CHARGE,ch_2,acct_1,200,lost_card",
    "CHARGE,ch_3,acct_1,300,do_not_honor",
    "DISPUTE,ch_2",
    "CHARGE,ch_4,acct_2,400,lost_card",
    "CHARGE,ch_5,acct_2,500,lost_card",
    "CHARGE,ch_6,acct_1,600,lost_card",
    "CHARGE,ch_7,acct_2,700,lost_card",
    "CHARGE,ch_8,acct_2,800,do_not_honor",
]
