# Pet Store Inventory to Excel Converter

## Objective
This project provides a Python script to manage a pet store inventory and export it to an Excel file.  
It demonstrates working with dictionaries, data transformation using **pandas**, and exporting structured data to Excel with **openpyxl**.  
The script also calculates useful summary statistics (price range, average price) and previews the first few rows of the dataset.

### Skills Learned
- Practical use of **Python dictionaries** to structure large datasets.
- Data manipulation and organization with **pandas**.
- Exporting tabular data into **Excel spreadsheets**.
- Error handling and dependency management in Python scripts.
- Basic descriptive statistics (min, max, average price).

### Tools Used
- **Python** for data handling and logic.
- **pandas** for dataframe creation, sorting, and manipulation.
- **openpyxl** as the engine for writing Excel files.

## Steps
1. Clone or download this repository.  
   ```bash
   git clone https://github.com/username/pet-store-inventory.git
   cd pet-store-inventory
   ````

2. Install the required dependencies:

   ```bash
   pip install pandas openpyxl
   ```

3. Run the script:

   ```bash
   python pet_store_inventory.py
   ```

4. The script will:

   * Convert the dictionary of items and prices into an Excel file (`pet_store_inventory.xlsx`).
   * Display total items, price range, and average price (for numeric values).
   * Print the first 10 rows of the inventory as a preview.

---

*Ref 1: Example Console Output*

```
Pet Store Inventory to Excel Converter
========================================
Excel file 'pet_store_inventory.xlsx' created successfully!
Total items: 300+
Price range (single-priced items): ₦2,000 - ₦300,000
Average price (single-priced items): ₦47,500.25

First 10 items:
               Items  Pricing
 3 in 1 grooming kit    20000
 2 in 1 conditioning shampoo 10000
 2 in 1 plate (b)       12000
 2 in 1 plate (s)       10000
 ...
```

## Future Enhancements

* Add a **search functionality** to quickly find items by name or price range.
* Implement a **database backend** (SQLite/PostgreSQL) to store inventory and allow updates without editing the Python dictionary.
* Add **category filters** (e.g., Dry Food, Accessories, Wet Food) in the Excel output for easier navigation.
* Include **graphs and charts** in Excel showing inventory distribution, price trends, or category breakdown.
* Implement **automated data validation** to detect missing or incorrect prices.
* Create a **web interface** for interactive inventory management and Excel export.

