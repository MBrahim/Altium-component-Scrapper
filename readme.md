# LCSC Component Scraper & Altium Library Generator

A comprehensive toolset for scraping FOJAN brand components (as an example) from LCSC.com and generating Altium Designer component libraries.

## 📋 Overview
This project automates the collection of electronic component data from LCSC.com and converts it into Altium Designer libraries. It consists of two main parts:
1. **Web Scrapers** - Extract component data (resistors & capacitors) from LCSC.com
2. **Library Generators** - Convert scraped data into Altium Designer component libraries

## 📁 Project Structure
├── Resistors Scrape [FOJAN].py     &emsp;&emsp;&emsp;# Scrape FOJAN resistors from LCSC  
├── Capacitors Scrape [FOJAN].py    &emsp;&emsp;&emsp;# Scrape FOJAN capacitors from LCSC  
├── altium scripting [RESs].py       &emsp;&emsp;&emsp;# Generate Altium resistor libraries  
├── altium scripting [CAPs].py       &emsp;&emsp;&emsp;# Generate Altium capacitor libraries  
├── Outputs/                         &emsp;&emsp;&emsp;# Generated files directory  
│   ├── JSONs/                      &emsp;&emsp;&emsp;# Raw scraped data in JSON format  
│   │   ├── Resistors-FOJAN.json  
│   │   └── Capacitors-FOJAN.json  
│   ├── CSVs/                       &emsp;&emsp;&emsp;# Processed data in CSV format  
│   │   ├── Resistors-FOJAN.csv  
│   │   └── Capacitors-FOJAN.csv  
│   ├── Excels/                     &emsp;&emsp;&emsp;# Processed data in Excel format  
│   │   ├── Resistors-FOJAN.xlsx  
│   │   └── Capacitors-FOJAN.xlsx  
│   └── Components/                 &emsp;&emsp;&emsp;# Altium library files (.txt)  
│       ├── Resistors.txt  
│       └── Capacitors.txt  
└── README.md                       &emsp;&emsp;&emsp;# This documentation file  

| File | Purpose | Input | Output |
|------|---------|-------|--------|
| **`Resistors Scrape [FOJAN].py`** | Web scraper for FOJAN resistors | LCSC website | JSON/CSV/Excel files |
| **`Capacitors Scrape [FOJAN].py`** | Web scraper for FOJAN capacitors | LCSC website | JSON/CSV/Excel files |
| **`altium scripting [RESs].py`** | Altium library generator for resistors | JSON data | Altium library (.txt) |
| **`altium scripting [CAPs].py`** | Altium library generator for capacitors | JSON data | Altium library (.txt) |

## Usage Flow
### Step 1: Scrape Components
```bash
# Run resistor scraper
python "Resistors Scrape [FOJAN].py"

# Run capacitor scraper  
python "Capacitors Scrape [FOJAN].py"
```
### Step 2: Generate Altium Scripting file.txt
```bash
# Generate resistor library
python "altium scripting [RESs].py"

# Generate capacitor library
python "altium scripting [CAPs].py"
```


### Step 3: Finally Generating the Altium Libraries
- Run the script found in the **\Altium Scripting Project\\** folder, select the .txt files found in **\Outputs\Components\\**

- Voilà!! you got yourself the symbols.

## ⚠️ Important Notes
- You can edit the looks of you components it's done using the **altium scripting.py** Files.
- you can change the paramters names, what to put what's not.
- I already scrapped latest components found in the **\Outputs\Components\\**.
- Those Scripts only import the symbols, the footprints are must to created manually, I put my owwn files and "add existing" in Altium. remember to add them or create your own.
- It's a little bit laggy, due to large number of components, It's recommended that you copy the component you need to your own project library.
