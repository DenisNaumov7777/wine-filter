
---

# Wine Data Processor & Filter 🍷

A robust ETL (Extract, Transform, Load) utility designed to process wine rating datasets. Built with **Python** and **Pandas**, this tool automates the cleaning of raw CSV data and extracts premium wine selections into structured JSON formats.

## 🌟 Key Features

* **Dynamic CLI Interface:** No hardcoded paths. Process any file by passing its path as a terminal argument.
* **Automated Data Cleaning:** - Removes completely empty columns.
* Drops records with missing critical values (Ratings/Variety).
* Fills metadata gaps with "Not Specified" placeholders.


* **Advanced Filtering:** Specifically targets **Red Wine** with a **90+ rating**.
* **Performance Optimized:** Uses Pandas vectorization for fast sorting and filtering.
* **Cross-Platform:** Built using `pathlib` to ensure compatibility across Windows, macOS, and Linux.

## 🛠 Prerequisites

* **Python:** 3.8 or higher
* **Pandas:** 2.0+

## 📥 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/DenisNaumov7777/wine-filter.git
cd wine-filter

```


2. **Install dependencies:**
```bash
pip install pandas

```



## 🚀 Usage

The script requires the path to your CSV file as a positional argument.

### Basic Command

```bash
python wine_processor.py wine-ratings-small.csv

```

### Custom Output Name

Use the `--output` flag to define a specific filename for your results:

```bash
python wine_processor.py data/input.csv --output premium_reds.json

```

## 📊 Data Transformation Logic

1. **Extraction:** Loads raw CSV data using `pathlib` for safe path handling.
2. **Cleaning:** Identifies and removes rows where `rating` is `NaN`.
3. **Transformation:** Filters for `variety == "Red Wine"` and `rating >= 90`.
4. **Loading:** Sorts the data and exports it as an array of objects in JSON.

## 📝 Example Output Structure

The generated `filtered_wines.json` will follow this schema:

```json
[
    {
        "name": "Estate Reserve Cabernet",
        "variety": "Red Wine",
        "rating": 95,
        "region": "Napa Valley",
        "price": 85.0
    }
]

```

## 👤 Author

**Denis Naumov** Cologne, Germany

---

