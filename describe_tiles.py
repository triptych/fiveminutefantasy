import json
import os

def load_mapping(mapping_file):
    with open(mapping_file, 'r') as f:
        return json.load(f)

def get_tile_description(mapping, tile_filename):
    # Extract row and column from filename
    # Format is tile_r000_c000.png
    row = int(tile_filename[6:9])
    col = int(tile_filename[11:14])

    # Search through sections to find matching tile
    sections = mapping['sections']

    # Terrain (Rows 0-4)
    if 0 <= row <= 4:
        if row == 0:
            if 0 <= col <= 5:
                if col == 0:
                    return "Basic grass tile"
                elif col == 1:
                    return "Grass tile with flowers"
                elif col == 2:
                    return "Tall grass tile"
                else:
                    return "Grass variant tile"
            elif 6 <= col <= 8:
                return "Grass to dirt transition tile"
            elif 9 <= col <= 11:
                return "Grass to water transition tile"
        return f"Terrain tile at row {row}, column {col}"

    # Structures (Rows 5-14)
    elif 5 <= row <= 14:
        if row == 5 and 0 <= col <= 5:
            if col <= 2:
                return "Basic stone wall tile"
            else:
                return "Decorated stone wall tile"
        return f"Structure tile at row {row}, column {col}"

    # Characters (Rows 15-34)
    elif 15 <= row <= 34:
        if row == 15:
            if 0 <= col <= 2:
                return "Warrior idle animation (facing down)"
            elif 3 <= col <= 5:
                return "Warrior idle animation (facing up)"
            elif 6 <= col <= 8:
                return "Warrior idle animation (facing side)"
        elif row == 16:
            if 0 <= col <= 2:
                return "Warrior walk animation (facing down)"
            elif 3 <= col <= 5:
                return "Warrior walk animation (facing up)"
            elif 6 <= col <= 8:
                return "Warrior walk animation (facing side)"
        return f"Character sprite at row {row}, column {col}"

    # Monsters (Rows 35-54)
    elif 35 <= row <= 54:
        if row == 35:
            if 0 <= col <= 2:
                return "Green slime idle animation"
            elif 3 <= col <= 5:
                return "Green slime movement animation"
        return f"Monster sprite at row {row}, column {col}"

    # Items (Rows 55-74)
    elif 55 <= row <= 74:
        if row == 55:
            if col == 0:
                return "Basic sword item"
            elif col == 1:
                return "Iron sword item"
            elif col == 2:
                return "Steel sword item"
            elif col == 3:
                return "Magic sword item"
        return f"Item sprite at row {row}, column {col}"

    # Effects (Rows 75-84)
    elif 75 <= row <= 84:
        if row == 75:
            if 0 <= col <= 2:
                return "Fire spell cast animation"
            elif 3 <= col <= 5:
                return "Fire spell impact animation"
        return f"Magic effect at row {row}, column {col}"

    # UI (Rows 85-94)
    elif 85 <= row <= 94:
        if row == 85:
            if col == 0:
                return "Menu button (normal state)"
            elif col == 1:
                return "Menu button (hover state)"
            elif col == 2:
                return "Menu button (pressed state)"
        return f"UI element at row {row}, column {col}"

    return f"Unknown tile at row {row}, column {col}"

def main():
    mapping = load_mapping('tileset_mapping.json')
    tiles_dir = 'tileset_tiles'

    # Get all tile files
    tile_files = sorted([f for f in os.listdir(tiles_dir) if f.endswith('.png')])

    print(f"Found {len(tile_files)} tiles\n")
    print("Tile Descriptions:")
    print("-----------------")

    for tile_file in tile_files:
        desc = get_tile_description(mapping, tile_file)
        print(f"{tile_file}: {desc}")

if __name__ == '__main__':
    main()
