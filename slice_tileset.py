from PIL import Image
import os

def slice_tileset(input_path, output_dir, tile_size=32):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the tileset
    with Image.open(input_path) as img:
        # Get the dimensions of the tileset
        width, height = img.size

        # Calculate number of tiles in each dimension
        num_cols = width // tile_size
        num_rows = height // tile_size

        # Iterate through each tile position
        for row in range(num_rows):
            for col in range(num_cols):
                # Calculate tile boundaries
                left = col * tile_size
                upper = row * tile_size
                right = left + tile_size
                lower = upper + tile_size

                # Extract the tile
                tile = img.crop((left, upper, right, lower))

                # Generate filename based on position
                filename = f'tile_r{row:03d}_c{col:03d}.png'

                # Save the tile
                output_path = os.path.join(output_dir, filename)
                tile.save(output_path)

                print(f'Saved {filename}')

if __name__ == '__main__':
    input_path = 'img/ProjectUtumno_full.png'
    output_dir = 'img/tiles'
    slice_tileset(input_path, output_dir)
