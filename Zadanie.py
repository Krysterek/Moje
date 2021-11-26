print("Lista zakupów")

shopping = {"piekarnia": "chleb, bułki, pączek", "warzywniak": "marchew, seler, rukola"}
shopping_dict = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
    }

for key in shopping:
    list = shopping[key]
    print("Idę do:", key.capitalize(),"i kupuję tu następujące rzeczy", list.title())

counter = 0
for value in shopping_dict:
    value_list = shopping_dict[value]
    total = len(value_list)  
    counter += total
print ("W sumie kupuję", counter, "produktów")