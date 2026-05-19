# 📊 FinSight — World Investment Intelligence System

> 196 countries. One investor. Zero clarity — until now.

Automated the full pipeline from raw IMF data to a ranked investment dashboard — surfacing the safest, highest-potential markets globally.

---

## 🖥️ Dashboard Preview

<img width="881" height="629" alt="image" src="https://github.com/user-attachments/assets/a90732ac-5a79-412f-949e-b129466e06dd" />


---

## 🎯 The Problem

Raw IMF data existed across 196 countries — scattered, unorganized, and impossible to compare. The client needed one system that could automatically consolidate everything and highlight **where to invest and where to avoid**.

---

## ✅ What Was Built

| | |
|---|---|
| ⚙️ **Auto-ingestion** | Google Apps Script pulls `.xlsx` files from Drive, consolidates into one master sheet, and archives originals |
| 📊 **Analytics dashboard** | Excel dashboard with KPIs, charts, and a world map — built on top of the consolidated data |
| 🌍 **Sweet Spot scoring** | Composite score ranking every country by inflation, growth, unemployment, and fiscal health |
| 🚨 **Risk flagging** | Misery Index and Net Lending charts surface dangerous economies automatically |

---

## 📈 Dashboard Highlights

| Visual | What it answers |
|---|---|
| **Sweet Spot World Map** | Which regions are safest to invest in — geographically |
| **Misery Index** | Is the global economy improving or getting worse? |
| **Top 10 Growing Countries** | Where is real GDP growth happening right now? |
| **Worst Net Lending** | Which countries are fiscally dangerous — the avoid list |
| **GDP PPP Donut** | Which economies actually control global output? |

---

## ⚙️ How the Automation Works

```
Drop .xlsx into Drive folder
          │
          ▼
  Script auto-converts + reads
          │
          ▼
  Appends to Master Sheet
  (no duplicate headers)
          │
          ▼
  Original file → archived
  Dashboard → updates
```

---

## 🔑 Key Results

- **194 countries** evaluated across 7+ IMF economic indicators
- **9.15%** global average inflation tracked across 2019–2025
- **Guyana** flagged as the top outlier — 57% GDP growth
- **Ukraine** identified as highest fiscal risk — net lending at -423.77

---

## 🛠️ Stack

`Excel` · `Google Sheets` · `Google Apps Script` · `IMF Open Data`

**Data source:** [IMF Datasets](https://data.imf.org/en/Datasets)
