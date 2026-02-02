# Automated Financial Reporting

Automates daily financial report consolidation  by ingesting uploaded Excel/Google Sheets files from Google Drive, standardizing the data, and appending it into a single master dataset for reporting.

## Problem
Field teams submit daily reports in Excel/Google Sheets, often with inconsistent formats and timing. Manual downloads and consolidation lead to:
- Data entry errors and duplicates
- Formatting inconsistencies
- Slow reporting turnaround
- Limited visibility into daily performance

## Solution
This project provides a Google Apps Script pipeline that:
- Scans a Google Drive **Source** folder for new files
- Reads **Google Sheets** directly
- Converts **Excel (.xlsx)** uploads into a temporary Google Sheet (Drive API) and extracts data
- Appends the data into a **Master Google Sheet** (headers added once, rows appended thereafter)
- Archives processed files to an **Archive** folder
- Deletes temporary converted files to keep Drive clean

## Tech Stack
- **Google Apps Script (JavaScript)**
- **Google Drive API / DriveApp**
- **Google Sheets (SpreadsheetApp)**
- **Excel ingestion (.xlsx → Google Sheets conversion)**

## Folder Setup
Create two folders in Google Drive:
1. **Source Folder** – field agents upload daily reports here  
2. **Archive Folder** – processed reports are moved here automatically  

Update these IDs in the script:
```js
var sourceFolderId = 'SOURCE_FOLDER_ID';
var archiveFolderId = 'ARCHIVE_FOLDER_ID';
