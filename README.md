# 🚖 Uber ETL Pipeline

### Modern Data Engineering Project — Mage AI · Azure · Delta Lake · Power BI

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Mage AI](https://img.shields.io/badge/Mage%20AI-ETL-purple)
![Azure](https://img.shields.io/badge/Azure-Blob%20Storage-0078D4)
![Delta Lake](https://img.shields.io/badge/Delta%20Lake-Storage-00ADD8)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Introduction

This project demonstrates an **end-to-end ETL (Extract, Transform, Load) data engineering pipeline** built using **Mage AI**. The pipeline extracts Uber trip data from a CSV dataset, performs data cleaning and transformation using **Python and Pandas**, stores the processed data in **Azure Blob Storage** as a **Delta Lake** table, and visualizes business insights using **Power BI**.

The project follows a modern cloud-based data engineering workflow by integrating ETL automation, cloud storage, and business intelligence tools — reflecting real-world data platform design.

---

## 🏗️ Project Architecture

```
┌───────────────────────┐
│      Uber Dataset      │
│       (CSV File)       │
└───────────┬─────────────┘
            │
            ▼
┌───────────────────────┐
│        Mage AI         │
│  Extract · Transform   │
│      · Load (ETL)      │
└───────────┬─────────────┘
            │
            ▼
┌───────────────────────┐
│      Delta Lake        │
│ (Azure Blob Storage)   │
└───────────┬─────────────┘
            │
            ▼
┌───────────────────────┐
│       Power BI          │
│  Analytics Dashboard    │
└───────────────────────┘
```

---

## 🔄 Project Workflow

| Step | Description |
|:----:|-------------|
| 1 | Load the Uber trip dataset into Mage AI |
| 2 | Clean and transform the raw data using Python and Pandas |
| 3 | Create dimension and fact tables for analytics |
| 4 | Store the processed data in Delta Lake on Azure Blob Storage |
| 5 | Connect Azure Blob Storage with Power BI |
| 6 | Build interactive dashboards to analyze Uber trip data |

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Data processing |
| **Pandas** | Data cleaning & transformation |
| **Mage AI** | ETL pipeline orchestration |
| **Azure Blob Storage** | Cloud data storage |
| **Delta Lake** | Reliable data lake storage |
| **Power BI** | Data visualization |
| **Git & GitHub** | Version control |

---

## 📂 Dataset

The project uses the **NYC Uber Trip Dataset**, containing:

- Vendor ID
- Pickup & Dropoff DateTime
- Passenger Count
- Trip Distance
- Payment Type
- Fare Amount
- Tip Amount
- Total Amount

---

## 📊 Dashboard

The Power BI dashboard provides insights such as:

- 🚕 Total Trips
- 💰 Total Revenue
- 💵 Average Fare
- 📏 Average Trip Distance
- 💳 Payment Type Distribution
- 🏢 Vendor-wise Trips
- 📈 Revenue Analysis

> `![Dashboard Preview](<img width="1001" height="691" alt="power bi dashboard" src="https://github.com/user-attachments/assets/466c8acb-cfd4-41cf-907b-db5a3308619b" />)`

---

## 📁 Project Structure

```
Uber-ETL-Pipeline/
│
├── data/                # Raw and processed datasets
├── data_loaders/        # Mage AI data loading blocks
├── transformers/         # Data cleaning & transformation logic
├── data_exporters/       # Export blocks (Azure Blob / Delta Lake)
├── pipelines/            # Mage AI pipeline definitions
├── notebooks/             # Exploratory analysis notebooks
├── images/                # Dashboard screenshots & diagrams
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/uber-etl-pipeline.git
cd uber-etl-pipeline
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Start Mage AI**
```bash
mage start
```

**4. Run the ETL pipeline**
Open the Mage AI UI (usually at `http://localhost:6789`) and trigger the pipeline.

**5. Connect Power BI**
Link Power BI to your Azure Blob Storage container to load the transformed Delta Lake data and build dashboards.

---

## 📌 Future Improvements

- [ ] Automate daily data ingestion
- [ ] Add incremental loading
- [ ] Integrate Azure Data Factory for orchestration
- [ ] Deploy the pipeline using Docker
- [ ] Add monitoring and logging

---

## 👨‍💻 Author

**Pranjal Jain**
Computer Science Undergraduate | Data Engineering Enthusiast

[GitHub](https://github.com/pranjaljain0905-wq) · [LinkedIn](https://www.linkedin.com/in/pranjal-jain-08374131a)

---

<p align="center">⭐ If you found this project useful, consider giving it a star!</p>
