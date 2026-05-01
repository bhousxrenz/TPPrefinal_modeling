# 🏥 Patient Wait Time Distribution Analysis

A **Modeling and Simulation** project that visualizes and analyzes the statistical distribution of patient wait times across five different hospital and clinic scenarios using Python.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Distribution Scenarios](#distribution-scenarios)
- [Output](#output)
- [Technologies Used](#technologies-used)

---

## 📌 Overview

This project simulates and analyzes patient wait times (in minutes) across five distinct hospital scenarios, each representing a different statistical distribution shape. By visualizing these distributions, the project demonstrates how real-world healthcare systems produce different patterns of patient flow — a core concept in **Modeling and Simulation**.

Each scenario contains **300 simulated data points** ranging from **0 to 120 minutes**.

---

## ✨ Features

- Reads patient wait time data directly from an external Excel file
- Generates histograms with **KDE (Kernel Density Estimate)** curves for each scenario
- Displays **mean** and **median** reference lines on every chart
- Compares all 5 distributions side by side in a single figure
- Clean, color-coded subplots for easy visual comparison

---

## 📁 Project Structure

```
📦 project-folder/
 ┣ 📄 patient_wait_time_distributions.py   ← Main Python script
 ┣ 📊 patient_wait_times.xlsx              ← External data file (required)
 ┗ 📄 README.md                            ← Project documentation
```

> ⚠️ Both the `.py` script and the `.xlsx` data file **must be in the same folder** for the script to run correctly.

---

## 🛠 Requirements

- Python 3.7 or higher
- The following Python libraries:

| Library | Purpose |
|---|---|
| `pandas` | Reading and handling Excel data |
| `seaborn` | Drawing histograms and KDE curves |
| `matplotlib` | Figure layout and displaying charts |
| `openpyxl` | Excel file support for pandas |

---

## ⚙️ Installation

**1. Clone or download this repository**

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

**2. Install the required libraries**

```bash
pip install pandas seaborn matplotlib openpyxl
```

---

## ▶️ Usage

Make sure both files are in the same folder, then run:

```bash
python patient_wait_time_distributions.py
```

The terminal will display:

```
Loading Excel file...
Data loaded: 300 rows, 5 columns
Code execution complete.
```

The charts will then appear in a pop-up window on your screen.

---

## 📊 Distribution Scenarios

| # | Distribution | Scenario | Description |
|---|---|---|---|
| 1 | **Normal** | Balanced Clinic | Wait times cluster symmetrically around the average — typical of a well-staffed, predictable clinic |
| 2 | **Bimodal** | Two Patient Streams | Two distinct peaks reflecting scheduled appointments and emergency walk-ins sharing the same facility |
| 3 | **Right-Skewed** | Emergency Department | Most patients are seen quickly, but a long tail captures severe cases that require extended waiting |
| 4 | **Left-Skewed** | Priority Care | Fast-track triage pushes most waits toward the upper bound; few patients experience short waits |
| 5 | **Uniform** | Scheduled Visits | All wait durations are equally probable — characteristic of rigid appointment-block systems |

---

## 📤 Output

Running the script produces a **5-panel figure** displayed on screen:

- Each panel shows a **histogram** (bars) and a **KDE curve** (smooth line)
- A **dashed black line** marks the mean
- A **dotted gray line** marks the median
- Each distribution has its own distinct color for easy identification

---

## 🧰 Technologies Used

- **Python 3** — Core programming language
- **pandas** — Data loading and manipulation
- **seaborn** — Statistical data visualization
- **matplotlib** — Plot rendering and display

---

*This project is for academic purposes only. All data is simulated and does not represent real patient records.*
