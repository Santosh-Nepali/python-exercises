import random
from waste_item import waste_items_database 

#item=WasteItem()

#print(random.choice(waste_items_database))

item=random.choice(waste_items_database)
for i in item:
    print(f'{item[i]}\n')

#obj=WasteItem(item)
#print(item.name)