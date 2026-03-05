
import pandas as pd 

data = {
    "word":[
        "love","successfull","laughing","joy","happiness",
        "suffer","killed","rape","terrorist","virus",
        "fucked","shots","omfg","oprah","christ",
        "ipod","taxes","usa","saddam","rainbow"
    ],

    "category": [
        "positive","positive","positive","positive","positive",
        "negative","negative","negative","negative","negative",
        "contested","contested","contested","contested","contested",
        "culturally_loaded","culturally_loaded","culturally_loaded","culturally_loaded","culturally_loaded"
    ],

    "happiness_average": [
        8.42,8.16,8.20,8.16,8.44,
        2.08,1.56,1.44,1.30,2.08,
        3.56,3.32,4.52,5.42,6.16,
        6.56,2.70,6.58,2.48,8.10
    ],

    "happiness_standard_deviation": [
        1.1082,1.0859,1.066,1.0568,0.9723,
        1.3827,1.2316,0.7866,0.9091,1.3377,
        2.7117,2.0146,2.0726,2.0513,2.3067,
        1.7515,1.5286,1.8416,1.5680,0.9949
    ]
}

table = pd.DataFrame(data)

print(table) 

table.to_csv("/Users/ricardakarallus/Desktop/coding-humanities/group-5/tables /3_1_table.csv")