function processUniversal() 
{
  // --- CONFIGURATION SECTION ---
  // Replace these IDs with the actual Drive folder IDs you want to use.
  var sourceFolderId = '1yecwal_q9V1hBVaq4wdMYoc4Rrax2XMX';
  var archiveFolderId = '1cA2m-mw5xcmNCDAbTWJAP5b8LBcIpIsm';
  // -----------------------------

  // Get folder objects from Drive using the IDs above
  var sourceFolder = DriveApp.getFolderById(sourceFolderId);
  var archiveFolder = DriveApp.getFolderById(archiveFolderId);



  // Use the currently active spreadsheet and its active sheet as the master sheet
  var masterSheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();


  // Get an iterator over files in the source folder
  // It loops through the folder one file at a time, reads information about the file, and prepares an empty container to store its data.
  var files = sourceFolder.getFiles(); //It is a FileIterator, a special object that lets you move through folder files one-by-one.

  while (files.hasNext()) //It checks whether there is another file available to process,Returns true if files are still left, else false 
  {
    var file = files.next(); //move to next file 
    var fileName = file.getName(); //get file name 
    var mimeType = file.getMimeType(); //get file type

    Logger.log("Found: " + fileName + " | Type: " + mimeType);   //logging the file. It prints a message to the execution logs.

    // We'll store the sheet data (2D array) here if we can read it
    var dataToCopy = [];


     // --- SCENARIO 1: Input is already a Google Sheet ---
    if (mimeType === MimeType.GOOGLE_SHEETS) 
    {
      Logger.log('Processing as Google Sheet: ' + fileName);
      try 
      {
        // Open the Google Sheet by ID and grab the first sheet/tab
        var sheet = SpreadsheetApp.openById(file.getId()).getSheets()[0];
        // Read all values as a 2D array (rows × columns)
        dataToCopy = sheet.getDataRange().getValues();
        // Note: We do not delete the original file here. We move it later.
      } catch (e) 
      {
        // Log error but continue processing other files
        Logger.log('Error reading Google Sheet ' + fileName + ': ' + e);
      }
    } 


    // --- SCENARIO 2: Input is  not an google sheet it is an Excel file (.xlsx or excel mime type) ---
    // excel file when uploaded can take various form .xls,.xlsx,.xlsm, .xlsb
    //we need to convert it into google sheets as  google script cannot read data from excel files 

    //Create a temporary Google Sheet file
    //Insert the Excel contents into it  Google Sheet using Drive API
    //Read that temporary sheetImmediately delete it(so your Drive does not get filled with useless converted files)

    
    else if (mimeType.indexOf("excel") > -1 || mimeType.indexOf("spreadsheet") > -1 || fileName.toLowerCase().endsWith(".xlsx")) 
    {
      Logger.log('Processing as Excel Binary: ' + fileName); //log 
      try {
        //go to serivces to create an drive service
         //Create a configuration object

        var tempFileConfig = {
          name: "[TEMP] " + fileName, //What the temporary Google Sheet should be called
          mimeType: MimeType.GOOGLE_SHEETS,//Tell Google Drive: create a Google Sheet
          parents: [sourceFolderId] // put temp file in the same folder 
        };
        //You are NOT creating the file yet — this is just a blueprint of the temp file that will be created.



        var tempFile = Drive.Files.create(tempFileConfig, file.getBlob());// this line does the magic, takes excel raw files content files.blob(),ask driver api to create a file with this raw data following the blueprint created above.
        
        // Open the newly created temporary Google Sheet and read data
        var tempSheet = SpreadsheetApp.openById(tempFile.id).getSheets()[0];
        dataToCopy = tempSheet.getDataRange().getValues();  // after reading the data copy the data 
        
        // Immediately trash the temporary Google Sheet file to keep folder clean
        DriveApp.getFileById(tempFile.id).setTrashed(true);
        
      } catch (e) 
      {
        Logger.log('Error converting Excel ' + fileName + ': ' + e);
      }
    }



// now for both the cases if the file is in google sheet or the file is in  other format and we are conveting for both the cases, i have stored the data to be copied in the variable datatocopy ,  
// Now comes the step 3  , where we ahve to paste data into master sheet if we have any. 

 // --- STEP 3: PASTE DATA TO MASTER SHEET (if we have data) ---
    if (dataToCopy.length > 0)  // of there is some data then continue else not 
    {
      try {
        if (masterSheet.getLastRow() === 0) // check if master sheet is empty , as if it is empty , insert data from first row else after the last row where there is data.
        {
          // Master sheet is empty: paste the entire dataset including headers
          masterSheet.getRange(1, 1, dataToCopy.length, dataToCopy[0].length).setValues(dataToCopy);//starts from 1 row 1 column and paste the entire  dataset including all rows and all columns.

        } 
        else {
          // Master already has data: assume dataToCopy[0] contains headers
          // and append only the body (rows after the header)
          var dataBody = dataToCopy.slice(1);
          if (dataBody.length > 0) {
            masterSheet.getRange(masterSheet.getLastRow() + 1, 1, dataBody.length, dataBody[0].length).setValues(dataBody);
          }
        }
        

 // --- STEP 4: ARCHIVE the ORIGINAL file ---
        // Move the processed file from source folder to archive folder
        file.moveTo(archiveFolder);
        Logger.log('SUCCESS: Processed and Archived ' + fileName);
        
      } catch (e)
       {
        Logger.log('Error pasting data for ' + fileName + ': ' + e);
      }
    } else 
    {
      // If dataToCopy is empty, nothing was recognized or read from the file
      Logger.log('Skipped ' + fileName + ': No recognizable data found or file skipped.');
    }
  }
}


