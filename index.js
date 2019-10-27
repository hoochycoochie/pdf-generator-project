
var fs = require('fs');
var dest_file_path = 'catalogue.pdf';
var pdfmerger = require('pdfmerger');
// Combining pdfs by using file paths
var pdfs = [
        './intro/index.pdf', // page 1
        './presentation/index.pdf', // 2
        './training/index.pdf',//3
        './trainers/index.pdf',//4
        './mobile/index.pdf',//5

        './gand/index.pdf',//6
        './anda/index.pdf',//7
        './ios/index.pdf',//8
        './cord/index.pdf',//9

        './web/index.pdf',//10
        './html5/index.pdf',//11
        './angu/index.pdf',//12
        './mong/index.pdf',//13
        './elas/index.pdf',//14


        './node/index.pdf',//15
        './java-intro/index.pdf',//16
        './ipjt/index.pdf',//17
        './jee7/index.pdf',//18
        './jav2/index.pdf',//19



        './ocpjp/index.pdf',//20
        './jrest/index.pdf',//21
        './jpa2/index.pdf',//22
        './ejb3/index.pdf',//23
        './devops-intro/index.pdf',//24


        './git/index.pdf',//25
        './dker/index.pdf',//26
        './micj/index.pdf',//27
        './plm-intro/index.pdf',//28
        './plma/index.pdf',//29
        './plmd/index.pdf',//30

        './calendar-mobile/index.pdf', //31
        './calendar-web/index.pdf', //32
        './calendar-javaj2ee/index.pdf', //33
        './calendar-devops/index.pdf', //34
        './calendar-plm/index.pdf', //35


        './info/index.pdf',//36
        './end-logo/index.pdf',//37



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
