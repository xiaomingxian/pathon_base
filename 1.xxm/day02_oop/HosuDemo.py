class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[家具%s,占地%.2f]" % (self.name, self.area)


class House:
    def __init__(self, type, area):
        self.type = type
        self.area = area
        # 剩余面积
        self.lastArea = area
        #  家居
        self.list = []

    def addItem(self, HouseItem):
        if self.lastArea < HouseItem.area:
            print("家具太大了 放不下")
            return
        self.list.append(HouseItem.name)
        self.lastArea -= HouseItem.area

    def __str__(self):
        return ("[户型%s,面积%.2f（剩余%.2f），家居%s]" % (self.type, self.area, self.lastArea, self.list))


# test
HI = HouseItem('沙发', 20)
HI2 = HouseItem('床', 40)
HI3 = HouseItem('床2', 100)
house = House('大户型', 140)
house.addItem(HI)
house.addItem(HI2)
house.addItem(HI3)

print(house)
