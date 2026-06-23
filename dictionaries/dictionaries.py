#dictionaries
date = {
    "manya": "4/4/2005",
    "moulya": "30/9/2006",
    "dhanya": "25/2/2006"
}
print(date["manya"])

#get method
print(date.get("moulya"))
print(date.get("divya", "not found"))

#adding new key value pair
date["divya"] = "15/5/2007"
print(date)

#modifying existing key value pair
date["divya"] = "5/4/2005"
print(date)

#deleting key value pair
pop_value = date.pop("divya")
print(pop_value)
print(date)
del date["moulya"]
print(date)

#methods
print(date.keys())
print(date.values())
print(date.items())

new_date = {
    "sneha": "5/5/2005",
    "spoorthi": "15/5/2006"
}
date.update(new_date)
print(date)

item1={
    "bru":1,
    "sunrise":2,
    "levista":3
}
item2={
    "sugar": "1kg",
    "salt": "500g",
    "rice": "10kg",
    "milk": "1L"
}
item=[item1,item2]
print(item)