from object_packaging.field import Field,StringField,IntegerField
from object_packaging.orm import Model


class Goods(Model):
    computer_part_name = StringField("computer_part_name")
    computer_info = StringField("computer_info")


# goods = Goods()
# goods.insert(["computer_part_name", "computer_info"], ["我的主体", "我的电脑"])


goods = Goods()
r = goods.select(["computer_part_name", "computer_info"],["computer_part_name='我的主体'"])
print(r)

