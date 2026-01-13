import json
import os

def create_component_from_json(item):
    """Create a component entry for the Ultra Librarian file from JSON data."""
    
    # Get values, use empty string if key doesn't exist
    package = item.get('Package', '')
    capacitance = item.get('Capacitance', '')
    voltage_rating = item.get('Voltage Rating', '')
    tolerance = item.get('Tolerance', '').replace('±', '')  # Remove ± if present
    temp_coefficient = item.get('Temperature Coefficient', '')
    supplier_part = item.get('Supplier Part Number', '')
    manufacturer_part = item.get('Manufacturer Part Number', '')
    description = item.get('description', '').replace('±', '')  # Remove ± if present
    
    # Create the component name with all parameters
    name = f"CAP {package} {capacitance} {voltage_rating} {tolerance} {temp_coefficient}".strip()
    
    # Determine the footprint based on package size
    if package == "0201":
        footprint = "CAP Ceramic SMD 0201"
    elif package == "0402":
        footprint = "CAP Ceramic SMD 0402"
    elif package == "0603":
        footprint = "CAP Ceramic SMD 0603"
    elif package == "0805":
        footprint = "CAP Ceramic SMD 0805"
    elif package == "1206":
        footprint = "CAP Ceramic SMD 1206"
    elif package == "1210":
        footprint = "CAP Ceramic SMD 1210"
    elif package == "1812":
        footprint = "CAP Ceramic SMD 1812"
    elif package == "2220":
        footprint = "CAP Ceramic SMD 2220"
    else:
        footprint = f"CAP Ceramic SMD {package}" if package else "CAP Ceramic SMD"
    
    # Create the component entry
    component = f"""Component (Name "{name}") (PartCount 1) (DesPrefix "C?")
Pin (Location 0, 40.94) (Rotation 90) (PinType Passive) (Length 59.06) (Width 0) (Designator Hidden "2") (Name Hidden "2") (PinSwap 1) (PartSwap 1) (PinSeq 2) (Part 1)
Pin (Location 0, -40.94) (Rotation 270) (PinType Passive) (Length 59.06) (Width 0) (Designator Hidden "1") (Name Hidden "1") (PinSwap 1) (PartSwap 1) (PinSeq 1) (Part 1)
Line (Width 8) (Start 0, -18.11) (End 0, -37.8) (Part 1)
Line (Width 8) (Start 0, 21.26) (End 0, 40.94) (Part 1)
Line (Width 8) (Start -78.74, -18.11) (End 78.74, -18.11) (Part 1)
Line (Width 8) (Start -78.74, 21.26) (End 78.74, 21.26) (Part 1)
Parameter (Name "Supplier") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "LCSC") (Part 1)
Parameter (Name "Supplier Part Number") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{supplier_part}") (Part 1)
Parameter (Name "Manufacturer") (Location 0, 0) (Height 50) (Rotation 0) (Justification Center) (Value "FOJAN") (Part 1)
Parameter (Name "Manufacturer Part Number") (Location 0, 0) (Height 50) (Rotation 0) (Justification Center) (Value "{manufacturer_part}") (Part 1)
Description (Value "{description}") (Part 1)
Parameter (Name "Capacitance") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{capacitance}") (Part 1)
Parameter (Name "Tolerance") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{tolerance}") (Part 1)
Parameter (Name "Voltage Rating") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{voltage_rating}") (Part 1)
Parameter (Name "Temperature Coefficient") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{temp_coefficient}") (Part 1)
Comment (Value "=Capacitance") (Part 1)
Footprint (Name "{footprint}")
EndComponent
"""
    return component

def main():
    # Define input and output paths
    input_json_path = os.path.join('Outputs', 'JSONs', 'Capacitors-FOJAN.json')
    output_folder = os.path.join('Outputs', 'Components')
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Check if JSON file exists
    if not os.path.exists(input_json_path):
        print(f"Error: JSON file not found at {input_json_path}")
        print("Please make sure to run the scraper first to generate the JSON file.")
        return

    # Read the JSON file
    with open(input_json_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    # Start building the output file
    output_lines = []
    
    # Add header
    output_lines.append("# Created by Ultra Librarian 8.3.381 Copyright © 1999-2024")
    output_lines.append("# Frank Frank, Accelerated Designs")
    output_lines.append("# Modified By Mohamed A. Ebrahem")
    output_lines.append("")
    output_lines.append("StartComponents")
    output_lines.append("")
    
    # Create components for each item in JSON
    for item in data:
        component_text = create_component_from_json(item)
        output_lines.append(component_text)
    
    # Add footer
    output_lines.append("")
    output_lines.append("EndComponents")
    
    # Write to output file in Outputs folder
    output_path = os.path.join(output_folder, 'Capacitors.txt')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(output_lines))
    
    print(f"Created {len(data)} components in Capacitors.txt")

if __name__ == "__main__":
    main()