from blocks import *
# items and blocks share a common id table
# ids of items should be >= ITEM_ID_MIN
ITEM_ID_MIN = 256

# From MinecraftWiki
# Items are objects which do not exist outside of the player's inventory and hands
# i.e., they cannot be placed in the game world.
# Some items simply place blocks or entities into the game world when used.
# Type
# * Materials: iron ingot, gold ingot, etc.
# * Food: found or crafted by the player and eaten to regain hunger points
# * Poitions
# * Tools
# * Informative items: map, compass and clock
# * Weapons
# * Armor

ITEMS_DIR = {}

class Item(object):
    id = None
    max_stack_size = 0
    amount_label_color = 255, 255, 255, 255
    name = "Item"

    def __init__(self):
        ITEMS_DIR[self.id] = self

    def on_right_click(self):
        pass

class ItemStack(object):
    def __init__(self, type = 0, amount = 1, durability = -1, data = 0):
        if amount < 1:
            amount = 1
        self.type = type
        self.amount = amount
        self.durability = durability
        self.data = data
        if type >= ITEM_ID_MIN:
            self.max_stack_size = ITEMS_DIR[type].max_stack_size
        else:
            self.max_stack_size = BLOCKS_DIR[type].max_stack_size

    # for debugging
    def __repr__(self):
        return '{ Item stack with type = ' + str(self.type) + ' }'

    def change_amount(self, change=0):
        overflow = 0
        if change != 0:
            self.amount += change
            if self.amount < 0:
                self.amount = 0
            elif self.amount > self.max_stack_size:
                overflow = self.amount - self.max_stack_size
                self.amount -= overflow

        return overflow

    # compatible with blocks
    @property
    def id(self):
        return self.type

    # compatible with blocks
    @property
    def name(self):
        return self.get_object().name

    def get_object(self):
        if self.id >= ITEM_ID_MIN:
            return ITEMS_DIR[self.id]
        else:
            return BLOCKS_DIR[self.id]

class CoalItem(Item):
    id = 263
    max_stack_size = 64
    name = "Coal"

class LadderItem(Item):
    id = 16
    max_stack_size = 64
    name = "Ladder"

class DiamondItem(Item):
    id = 264
    max_stack_size = 64
    name = "Diamond"

class IronIngotItem(Item):
    id = 265
    max_stack_size = 64
    name = "Iron Ingot"

class GoldIngotItem(Item):
    id = 266
    max_stack_size = 64
    name = "Gold Ingot"

class StickItem(Item):
    id = 280
    max_stack_size = 64
    name = "Stick"

class YellowDyeItem(Item):
    id = 351
    max_stack_size = 64
    name = "Dandelion Yellow Dye"

class CactusGreenDyeItem(Item):
    id = 351.2
    max_stack_size = 64
    name = "Cactus Green Dye"

class Tool(Item):
    material = None
    multiplier = 0
    tool_type = None

    def __init__(self):
        super(Tool, self).__init__()
        self.multiplier = 2 * (self.material + 1)

class WoodAxe(Tool):
    material = WOODEN_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 271
    name = "Wooden Axe"

class StoneAxe(Tool):
    material = STONE_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 275
    name = "Stone Axe"

class IronAxe(Tool):
    material = IRON_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 258
    name = "Iron Axe"

class EmeraldAxe(Tool):
    material = IRON_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 258.1
    name = "Emerald Axe"

class DiamondAxe(Tool):
    material = DIAMOND_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 279
    name = "Diamond Axe"

class GoldenAxe(Tool):
    material = GOLDEN_TOOL
    tool_type = AXE
    max_stack_size = 1
    id = 286
    name = "Golden Axe"

class WoodPickaxe(Tool):
    material = WOODEN_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 270
    name = "Wooden Pickaxe"

class StonePickaxe(Tool):
    material = STONE_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 274
    name = "Stone Pickaxe"

class IronPickaxe(Tool):
    material = IRON_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 257
    name = "Iron Pickaxe"

class EmeraldPickaxe(Tool):
    material = IRON_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 257.1
    name = "Emerald Pickaxe"

class DiamondPickaxe(Tool):
    material = DIAMOND_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 278
    name = "Diamond Pickaxe"

class GoldenPickaxe(Tool):
    material = GOLDEN_TOOL
    tool_type = PICKAXE
    max_stack_size = 1
    id = 285
    name = "Golden Pickaxe"

class WoodShovel(Tool):
    material = WOODEN_TOOL
    tool_type = SHOVEL
    max_stack_size = 1
    id = 269
    name = "Wooden Shovel"

class StoneShovel(Tool):
    material = STONE_TOOL
    tool_type = SHOVEL
    max_stack_size = 1
    id = 273
    name = "Stone Shovel"

class IronShovel(Tool):
    material = IRON_TOOL
    tool_type = SHOVEL
    max_stack_size = 1
    id = 256
    name = "Iron Shovel"

class EmeraldShovel(Tool):
    material = IRON_TOOL
    tool_type = SHOVEL
    max_stack_size = 1
    id = 256.1
    name = "Emerald Shovel"

class DiamondShovel(Tool):
    material = DIAMOND_TOOL
    tool_type = SHOVEL
    max_stack_size = 1
    id = 277
    name = "Diamond Shovel"

class GoldenShovel(Tool):
    material = GOLDEN_TOOL
    tool_type = SHOVEL
    max_stack_size = 1
    id = 284
    name = "Golden Shovel"

class Armor(Item):
    material = None
    defense_point = 0
    armor_type = None

    def __init__(self):
        super(Armor, self).__init__()

class IronHelmet(Armor):
    material = IRON_TOOL
    defense_point = 1
    armor_type = HELMET
    id = 306
    name = "Iron Helmet"

class IronChestplate(Armor):
    material = IRON_TOOL
    defense_point = 3
    armor_type = CHESTPLATE
    id = 307
    name = "Iron Chestplate"

class IronLeggings(Armor):
    material = IRON_TOOL
    defense_point = 2.5
    armor_type = LEGGINGS
    id = 308
    name = "Iron Leggings"

class IronBoots(Armor):
    material = IRON_TOOL
    defense_point = 1
    armor_type = BOOTS
    id = 309
    name = "Iron Boots"

##Emerald Armor .. Pretty much re-textured Iron armor (from Tekkit)

#class EmeraldHelmet(Armor):
    #material = IRON_TOOL
    #defense_point = 1
    #armor_type = HELMET
    #id = 306.1
    #name = "Emerald Helmet"

#class EmeraldChestplate(Armor):
    #material = IRON_TOOL
    #defense_point = 3
    #armor_type = CHESTPLATE
    #id = 307.1
    #name = "Emerald Chestplate"

#class EmeraldLeggings(Armor):
    #material = IRON_TOOL
    #defense_point = 2.5
    #armor_type = LEGGINGS
    #id = 308.1
    #name = "Emerald Leggings"

#class EmeraldBoots(Armor):
    #material = IRON_TOOL
    #defense_point = 1
    #armor_type = BOOTS
    #id = 309.1
    #name = "Emerald Boots"

coal_item = CoalItem()
diamond_item = DiamondItem()
stick_item = StickItem()
iron_ingot_item = IronIngotItem()
gold_ingot_item = GoldIngotItem()
wood_axe = WoodAxe()
stone_axe = StoneAxe()
iron_axe = IronAxe()
diamond_axe = DiamondAxe()
golden_axe = GoldenAxe()
emerald_axe = EmeraldAxe()
wood_pickaxe = WoodPickaxe()
stone_pickaxe = StonePickaxe()
iron_pickaxe = IronPickaxe()
diamond_pickaxe = DiamondPickaxe()
golden_pickaxe = GoldenPickaxe()
emerald_pickaxe = EmeraldPickaxe()
wood_shovel = WoodShovel()
stone_shovel = StoneShovel()
iron_shovel = IronShovel()
diamond_shovel = DiamondShovel()
golden_shovel = GoldenShovel()
emerald_shovel = EmeraldShovel()
iron_helmet = IronHelmet()
iron_chestplate = IronChestplate()
iron_leggings = IronLeggings()
iron_boots = IronBoots()
#emerald_helmet = EmeraldHelmet()
#emerald_chestplace = EmeraldChestplate()
#emerald_leggings = EmeraldLeggings()
#emerald_boots = EmeraldBoots()
yellowdye_item = YellowDyeItem()
ladder_item = LadderItem()
