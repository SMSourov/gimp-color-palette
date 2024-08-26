import csv

def hex_to_rgb(hex_color):
    """Convert a HEX color code to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def process_csv(input_file, output_file):
    """Read the CSV file, transform the data, and write to a new file."""
    with open(input_file, 'r') as csvfile, open(output_file, 'w') as outfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            if len(row) != 2:
                continue  # Skip rows that don't have exactly two columns
            
            color_name = row[0].strip()
            color_code = row[1].strip()
            
            # Convert HEX to RGB
            rgb = hex_to_rgb(color_code)
            rgb_str = f"{rgb[0]} {rgb[1]} {rgb[2]}"
            
            # Format the output line
            output_line = f"{rgb_str} {color_name} ({color_code})\n"
            
            # Write to the output file
            outfile.write(output_line)

# Example usage
input_file = 'colorcapture.csv'
output_file = 'colorcapture.txt'
process_csv(input_file, output_file)
