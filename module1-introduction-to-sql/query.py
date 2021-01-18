TOTAL_CHARACTERS = """
    SELECT COUNT(name)
    FROM charactercreator_character;
"""

TOTAL_SUBCLASS = """
    SELECT 
        (SELECT COUNT(*)
        FROM charactercreator_cleric
        ) as cleric,
        (SELECT COUNT(*)
        FROM charactercreator_fighter
        ) AS fighter,
        (SELECT COUNT(*)
        FROM charactercreator_mage
        ) AS mage,
        (SELECT COUNT(*)
        FROM charactercreator_necromancer
        ) AS necromancer,
        (SELECT COUNT(*)
        FROM charactercreator_thief
        ) AS theif;
"""
TOTAL_ITEMS = """
    SELECT COUNT(*)
    FROM armory_item;
"""

TOTAL_WEPONS = """
    SELECT COUNT(*)
    FROM armory_weapon;
"""

NON_WEPONS = """
    SELECT item_id, item_ptr_id
    FROM armory_item
    INNER JOIN armory_weapon
    ON armory_item.item_id = armory_weapon.item_ptr_id;
"""

CHARACTER_ITEMS = """
    SELECT character_id, COUNT(character_id)
    FROM charactercreator_character_inventory
    GROUP BY character_id;
"""
