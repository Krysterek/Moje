print("Lista Zakupów:")

shopping = {"piekarnia": "chleb, bułki, pączek", "warzywniak": "marchew, seler, rukola"}
shopping_dict = dict(shopping)
for key in shopping:
    lista_d = shopping[key]
    print("Idę do:", key.capitalize(),"i kupuję tu następujące rzeczy", lista_d.title())


counter = 0
for value in shopping_dict:
    value_list = shopping_dict[value]
    total = len(value_list)  
    counter += total
print ("W sumie kupuję", counter, "produktów")

    