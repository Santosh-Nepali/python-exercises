"""
This class represents stores the kind of items 
"""
class WasteItem:
    # A single piece of waste with its correct bin category
    def __init__(self, name, category, fact):
        self.name=name
        self.category=category
        self.fact=fact
    
    def __str__(self):
        return f"{self.name}, {self.category}, {self.fact}"
    
waste_items_database=[
    {"name": "banana peel", "category": "Bio", "fact":"Bio waste like fruit peel can be composted or turned into biogas."},
    {"name": "apple core", "category": "Bio", "fact":"Food scraps deccompose naturally and idle for composting."},
    {"name": "used tea bag", "category": "Bio", "fact":"Tea bag without plastic linings break down easily as bio waste"},
    {"name": "newspaper", "category": "Paper", "fact":"Paper can be recycled up 5-7 times before its fibers become too short to reuse."},
    {"name": "cardboard box", "category": "Paper", "fact":"Clean, dry cardboard is one of the most recyclable materials available."},
    {"name": "newspaper", "category": "Paper", "fact":"Paper can be recycled up 5-7 times before its fibers become too short to reuse."},
    {"name": "notebook", "category": "Paper", "fact": "Paper recycling saves significant water and energy compared to making new paper."},
    {"name": "broken light bulb", "category": "Energy", "fact": "Some light bulbs need special recycling to recover energy or hazardous elements."},
    {"name": "old batteries", "category": "Energy",  "fact": "Batteries can be processed to recover metals and energy instead of polluting landfills."},
    {"name": "used cooking oil", "category": "Energy", "fact": "Used cooking oil can be converted into biodiesel, making it valuable energy waste."},
    {"name": "plastic bottle", "category": "Plastic", "fact": "A plastic bottle can take up to 450 years to decompose in a landfill."},
    {"name": "yogurt container", "category": "Plastic", "fact": "Most rigid plastic containers can be recycled if rinsed clean first."},
    {"name": "plastic bag", "category": "Plastic", "fact": "Thin plastic bags often need special drop-off points instead of regular recycling."},
    {"name": "broken ceramic mug", "category": "Mixed Waste", "fact": "Ceramics don't melt like glass, so they usually can't be recycled with regular glass."},
    {"name": "used tissue", "category": "Mixed Waste", "fact": "Used tissues count as general waste due to contamination."},
    {"name": "greasy pizza box", "category": "Mixed Waste", "fact": "Grease-soaked cardboard usually can't be recycled since the oil contaminates the fibers."},    
]

waste_items=[]
for item in waste_items_database:
    waste_item=WasteItem(
        item["name"],
        item["category"],
        item["fact"]
    )
    waste_items.append(waste_item)