# TOPSIS Implementation in Python (CLI Tool)

This repository contains a **Python command-line implementation of the TOPSIS method**
(**Technique for Order Preference by Similarity to Ideal Solution**), a popular
Multi-Criteria Decision Making (MCDM) technique.

The tool ranks alternatives from a CSV file using **user-defined weights and impacts**
and works with datasets having a **dynamic number of criteria**.

---

## 🚀 What This Project Does

- Reads a CSV file containing alternatives and criteria
- Normalizes the criteria values
- Applies user-defined weights
- Determines ideal best and ideal worst solutions
- Calculates TOPSIS scores
- Ranks alternatives accordingly
- Writes the results to an output CSV file

---

## 📌 Features

- Works with **any CSV file**
- Dynamic number of criteria
- First column treated as alternatives (IDs / names)
- Remaining columns treated as numeric criteria
- User-defined weights and impacts (`+` / `-`)
- Command-line interface (CLI)
- Proper input validation and error handling
- Outputs ranked results to CSV

---

## 📌 Sample Input File (IMPORTANT)

Create a file named **`data.csv`** in the same folder as `topsis.py` and paste the following content:

```csv
Fund,P1,P2,P3,P4,P5
M1,0.71,0.50,3.9,33.8,9.73
M2,0.88,0.77,5.2,45.8,13.16
M3,0.78,0.61,3.8,40.1,11.32
M4,0.91,0.83,5.8,43.8,12.84
M5,0.76,0.58,6.4,34.8,10.6
```

---

## 🛠 Requirements

- Python 3.x
- pandas
- numpy

Install dependencies using:
```bash
pip install pandas numpy
```

---

## 🛠 Final Command for Run 

```bash
python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>
```
