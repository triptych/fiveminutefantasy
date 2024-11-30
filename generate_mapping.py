import json

def generate_base_mapping():
    mapping = {
        "metadata": {
            "total_rows": 95,
            "total_columns": 64,
            "total_tiles": 6080,
            "tile_size": "32x32 pixels"
        },
        "sections": {}
    }

    # Row sections with their ranges and descriptions
    sections = {
        "terrain": {
            "range": (0, 4),
            "subsections": {
                "grass": (0, 15),
                "water": (16, 31),
                "dirt": (32, 47),
                "stone": (48, 63)
            }
        },
        "buildings": {
            "range": (5, 14),
            "subsections": {
                "walls": (0, 15),
                "doors": (16, 31),
                "windows": (32, 47),
                "roofs": (48, 63)
            }
        },
        "characters": {
            "range": (15, 34),
            "subsections": {
                "warrior": (0, 7),
                "mage": (8, 15),
                "rogue": (16, 23),
                "archer": (24, 31),
                "priest": (32, 39),
                "merchant": (40, 47),
                "villager": (48, 55),
                "guard": (56, 63)
            }
        },
        "monsters": {
            "range": (35, 54),
            "subsections": {
                "slimes": (0, 7),
                "undead": (8, 15),
                "demons": (16, 23),
                "beasts": (24, 31),
                "dragons": (32, 39),
                "elementals": (40, 47),
                "bosses": (48, 55),
                "minions": (56, 63)
            }
        },
        "items": {
            "range": (55, 74),
            "subsections": {
                "weapons": (0, 15),
                "armor": (16, 31),
                "potions": (32, 47),
                "treasures": (48, 63)
            }
        },
        "effects": {
            "range": (75, 84),
            "subsections": {
                "magic": (0, 15),
                "elemental": (16, 31),
                "status": (32, 47),
                "environmental": (48, 63)
            }
        },
        "ui": {
            "range": (85, 94),
            "subsections": {
                "buttons": (0, 15),
                "icons": (16, 31),
                "frames": (32, 47),
                "indicators": (48, 63)
            }
        }
    }

    # Generate complete mapping
    for section_name, section_data in sections.items():
        start_row, end_row = section_data["range"]
        mapping["sections"][section_name] = {
            "description": f"Rows {start_row}-{end_row}: {section_name.capitalize()} section",
            "row_range": list(section_data["range"]),
            "subsections": {}
        }

        # Add subsections
        for subsection_name, (start_col, end_col) in section_data["subsections"].items():
            subsection = {
                "description": f"{subsection_name.capitalize()} tiles and variations",
                "column_range": [start_col, end_col],
                "tiles": {}
            }

            # Generate entries for each tile in this subsection
            for row in range(start_row, end_row + 1):
                for col in range(start_col, end_col + 1):
                    tile_name = f"tile_r{row:03d}_c{col:03d}.png"
                    category_name = f"{subsection_name}_{(row-start_row):02d}_{(col-start_col):02d}"
                    subsection["tiles"][category_name] = {
                        "file": tile_name,
                        "description": f"{subsection_name.capitalize()} variant {(row-start_row):02d}-{(col-start_col):02d}"
                    }

            mapping["sections"][section_name]["subsections"][subsection_name] = subsection

    return mapping

# Generate and save the mapping
mapping = generate_base_mapping()
with open('complete_tileset_mapping.json', 'w', encoding='utf-8') as f:
    json.dump(mapping, f, indent=2)

print("Generated complete mapping for all 6080 tiles")
