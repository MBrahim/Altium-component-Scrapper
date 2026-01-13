import json
import os

def format_resistor_value(resistance_str):
    """
    Format resistor value string according to the rules:
    - Ohms: 10Ω → 10R, 2.5Ω → 2R5
    - Kilohms: 10kΩ → 10k, 3.3kΩ → 3k3
    """
    if not resistance_str:
        return ""
    
    # Remove Ω symbol if present
    value = resistance_str.replace('Ω', '')
    
    # Check if it contains 'k' (kilohms)
    if 'k' in value.lower():
        # Handle kilohm values
        # Remove any trailing 'R' if present
        value = value.replace('R', '').replace('r', '')
        
        # Split numeric part and 'k'
        parts = value.lower().split('k')
        if len(parts) >= 2:
            numeric_part = parts[0]
            
            # Check if it has decimal point
            if '.' in numeric_part:
                # Convert 3.3k → 3k3
                int_part, decimal_part = numeric_part.split('.')
                # Take first digit after decimal
                decimal_digit = decimal_part[0] if decimal_part else '0'
                return f"{int_part}k{decimal_digit}"
            else:
                # Convert 10k → 10k
                return f"{numeric_part}k"
    else:
        # Handle ohm values
        # Remove any trailing 'R' if present
        value = value.replace('R', '').replace('r', '')
        
        # Check if it has decimal point
        if '.' in value:
            # Convert 2.5 → 2R5
            int_part, decimal_part = value.split('.')
            # Take first digit after decimal
            decimal_digit = decimal_part[0] if decimal_part else '0'
            return f"{int_part}R{decimal_digit}"
        else:
            # Convert 10 → 10R
            return f"{value}R"
    
    return value

def create_component_from_json(item):
    """Create a component entry for the Ultra Librarian file from JSON data."""
    
    # Get values, use empty string if key doesn't exist
    package = item.get('Package', '')
    Resistance = format_resistor_value(item.get('Resistance', ''))
    voltage_rating = item.get('Voltage Rating', '')
    tolerance = item.get('Tolerance', '').replace('±', '')  # Remove ± if present
    Power = item.get('Power', '')
    supplier_part = item.get('Supplier Part Number', '')
    manufacturer_part = item.get('Manufacturer Part Number', '')
    description = item.get('description', '').replace('±', '').replace('Ω', 'R')  # Remove ± and spaces if present
    
    # Create the component name with all parameters
    name = f"RES {package} {Resistance} {tolerance}".strip()
    
    # Determine the footprint based on package size
    if package == "0201":
        footprint = "RES SMD 0201"
    elif package == "0402":
        footprint = "RES SMD 0402"
    elif package == "0603":
        footprint = "RES SMD 0603"
    elif package == "0805":
        footprint = "RES SMD 0805"
    elif package == "1206":
        footprint = "RES SMD 1206"
    elif package == "1210":
        footprint = "RES SMD 1210"
    elif package == "1812":
        footprint = "RES SMD 1812"
    elif package == "2220":
        footprint = "RES SMD 2220"
    else:
        footprint = f"RES SMD {package}" if package else "RES SMD"
    
    # Create the component entry
    component = f"""Component (Name "{name}") (PartCount 1) (DesPrefix "C?")
Pin (Location -101.57, 0) (Rotation 180) (PinType Passive) (Length 98.43) (Width 0) (Designator Hidden "2") (Name Hidden "2") (PinSwap 1) (PartSwap 1) (PinSeq 2) (Part 1)
Pin (Location 101.57, 0) (Rotation 0) (PinType Passive) (Length 98.43) (Width 0) (Designator Hidden "1") (Name Hidden "1") (PinSwap 1) (PartSwap 1) (PinSeq 1) (Part 1)
Line (Width 8) (Start 0, 39.37) (End -39.37, -39.37) (Part 1)
Line (Width 8) (Start -39.37, -39.37) (End -78.74, 39.37) (Part 1)
Line (Width 8) (Start -78.74, 39.37) (End -98.42, 0) (Part 1)
Line (Width 8) (Start 0, 39.37) (End 39.37, -39.37) (Part 1)
Line (Width 8) (Start 39.37, -39.37) (End 78.74, 39.37) (Part 1)
Line (Width 8) (Start 78.74, 39.37) (End 98.42, 0) (Part 1)
Parameter (Name "Supplier") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "LCSC") (Part 1)
Parameter (Name "Supplier Part Number") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{supplier_part}") (Part 1)
Parameter (Name "Manufacturer") (Location 0, 0) (Height 50) (Rotation 0) (Justification Center) (Value "FOJAN") (Part 1)
Parameter (Name "Manufacturer Part Number") (Location 0, 0) (Height 50) (Rotation 0) (Justification Center) (Value "{manufacturer_part}") (Part 1)
Description (Value "{description}") (Part 1)
Parameter (Name "Resistance") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{Resistance}") (Part 1)
Parameter (Name "Tolerance") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{tolerance}") (Part 1)
Parameter (Name "Voltage Rating") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{voltage_rating}") (Part 1)
Parameter (Name "Power") (Location 150, -300) (Height 137) (Rotation 0) (Justification Center) (Value "{Power}") (Part 1)
Comment (Value "=Resistance") (Part 1)
Footprint (Name "{footprint}")
EndComponent
"""
    return component

def main():
    # Define input and output paths
    input_json_path = os.path.join('Outputs', 'JSONs', 'Resistors-FOJAN.json')
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
    output_path = os.path.join(output_folder, 'Resistors.txt')
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write('\n'.join(output_lines))
    
    print(f"Created {len(data)} components in Resistors.txt")
if __name__ == "__main__":
    main()