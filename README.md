Automated Financial Reporting Pipeline

Built an automated data pipeline to consolidate daily financial reports from distributed field teams into a single, standardized dataset for reporting and analysis.

Problem
Field teams submitted reports in Excel/Google Sheets with inconsistent formats and timing, leading to manual consolidation, duplicate entries, formatting issues, and delayed visibility into daily performance.
Solution
Designed a scheduled batch data pipeline to automate ingestion, transformation, and reporting:
Orchestrates data flow from Google Drive using Drive API and Power Automate
Standardizes and validates incoming Excel/Google Sheets data
Stores intermediate data in Amazon S3 for scalable processing
Appends cleaned data into a centralized reporting dataset
Archives processed files and removes temporary artifacts

Impact
Eliminated 3–4 hours of manual consolidation per cycle by orchestrating a scheduled batch data pipeline (Power Automate → Google Drive → Drive API → Power BI) that ingests, validates, and refreshes reports daily at 3 PM without human intervention
Improved decision turnaround time by 80% by building Power BI dashboards enabling self-service tracking of collections vs expected revenue, pending payments, and reconciliation gaps in near real-time

Tech Stack
Google Apps Script (JavaScript)
Google Drive API / DriveApp
Google Sheets (SpreadsheetApp)
Power BI (DAX, Power Query)
Amazon S3
