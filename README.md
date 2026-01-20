# TOPSIS Project – Multi-Criteria Decision Making

This repository contains a complete implementation of the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) method, developed as part of Project-1. The project demonstrates command-line, package-based, and web-based implementations of the TOPSIS algorithm.

---

## Project Information

| Field | Details |
|------|--------|
| Course | Project-1 |
| Student Name | Raghav Chhabra |
| Roll Number | 102303580 |
| Group | 3C42 |
| Method | TOPSIS (MCDM) |

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

## Part-I: Command Line TOPSIS Program

### Description
Part-I contains a Python script that implements the TOPSIS algorithm and executes via the command line. It reads a CSV file, applies the TOPSIS method using user-defined weights and impacts, and produces a ranked output CSV file.

### Usage
```bash
python topsis.py <input_file.csv> <weights> <impacts> <output_file.csv>
```
---

## Part-II: Python Package (PyPI)

### Description
In Part-II, the TOPSIS implementation is packaged as a Python module and uploaded to PyPI, allowing installation via pip and execution using a CLI command.

## Installation
```bash
pip install topsis-raghav-102303580
```

---

## Pypi Link
```bash
https://pypi.org/project/topsis-raghav-102303580/
```

---

## Part-III: Web Application (Streamlit)

## Description
Part-III provides a web-based interface using Streamlit, enabling users to upload CSV files, specify weights and impacts, and obtain ranked results interactively.

---

## 👉 Streamlit App Link:
```bash
https://topsis-web.streamlit.app
```








