# Catalogue

catalogue description
Help you write very styled pdf file using html et bootstrap
## pré requis
nodejs >=8, java >=6, (Ubuntu 15.04 security bug issue),python3    
Atom IDE is recommended and also these following packages:  apm install platformio-ide-terminal project-manager pdf-view atom-html-preview language-pug language-markdown  
python 3
apt-get install python3-bs4
pip3 install beautifulsoup4
pip3 install lxml
pip3 install html5lib


## Installation
1. npm install -g relaxedjs (ou sudo/su npm install -g relaxedjs )
2. mkdir my_folder
3. cd my_folder
4. npm init -y
5. npm install pdfmerger bootstrap --save
6. touch main.css
7. mkdir myfirst_page && cd myfirst_page
8. touch index.html css/style.css

## Files structure

```
my_folder
  │
  ────── myfirst_page
  │        │
  │        │___ index.html
  │        │
  │        └───css
  │        |    │__style.css
  │        |
  │         ──img
  │        │    │__logo.jpeg
  │        │    ...
  │
  │
  └───main.css
  └───index.js
  └───load_by_url.by
  └───generic-template.html
  └───package.json
  └───README.md
  └───node_modules


```
## Usage
main.css will contain all general styles colors that dont change, just to avoid repetition,
style.css customized styles for each page.
index.html content looks like this:

  ```

  <link rel="stylesheet" href="../node_modules/bootstrap/dist/css/bootstrap.min.css">
    <link rel="stylesheet" href="../main.css">
    <link href="https://use.fontawesome.com/releases/v5.0.7/css/all.css" rel="stylesheet">
    <link rel="stylesheet" href="css/style.css">


    <div class="container-fluid">

        // put your content here //

    </div>

  ```
You can preview your content by hitting C+SHIFT+H in atom editor.
To generate pdf, run in the terminal at the root of my_folder this command:
  ```
    relaxed myfirst_page/index.html    /path/destination/of-your.pdf
  ```
  If you have many pdf files to merge, edit index.js file and add the pdf path to arrays pdfs:
  ```

  var fs = require('fs');
  var dest_file_path = 'catalogue.pdf';
  var pdfmerger = require('pdfmerger');
  // Combining pdfs by using file paths
  var pdfs = [
          './myfirst_page/index.pdf', // page 1
          './mysecond_page/index.pdf', //page 2
          './mysecond_page/index.pdf', // page  3
              ...
              ];
  var pdfStream = pdfmerger(pdfs);
  var writeStream = fs.createWriteStream(dest_file_path);
  pdfStream.pipe(writeStream);
  // write the output to a file
  pdfmerger(pdfs, dest_file_path);
  pdfStream.on('data', function (data) {
          console.log('pdf generated successfully');
  });
  pdfStream.on('error', function (error) {
          console.log('error merging file', error);
  });
  pdfStream.on('close', function (code) {
  });

  ```
  To generate the whole pdf file, run command:
  ```
       node index.js
  ```
## Fetching html page from internet and generating pdf
At root of the my_folder, a python script, dont forget to make it executable.
  ```
  chmod +x load_by_url.py
  ./load_by_url.py  url folder_name_to_store backgroundColor http://your_url_here

  ```
## Example
  ```
    ./load_by_url.py  url anda blue https://www.docdoku.com/services/formation/anda-android-programmation-avancee/

   ```
 This command creates a folder named anda at the root of my_folder in which a style.css in css subfolder and index.html page which overrides generic-template.html.  You just need run relaxed pointing to index.html to generate the pdf file
 
 ## Technologies
nodejs, python, java, bootstrap
