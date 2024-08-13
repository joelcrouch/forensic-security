
## SUMMARY

This forensic report investigates allegations made by Allison Origin, a graduate student at the University of Illinois, against Kelly Copy, a researcher at the same institution. Allison claims that Kelly used her stolen data and writing in a federal funding proposal. The investigation involved analyzing two digital evidence sources: a USB drive (Allison.dd) that Allison used for her research and a computer (Allison.dd) used by Kelly. The primary objectives were to determine if Kelly accessed Allison’s data and to identify any suspicious activity related to file creation and deletion. This report details the methods used, findings uncovered, and conclusions drawn from the analysis.

## PURPOSE

The purpose of this investigation is to verify Allison Origin’s claims that Kelly Copy misappropriated her research data and used it to produce a federal funding proposal. Specifically, the investigation aims to:

1. Assess the timeline of file creation, modification, and deletion on the USB drive used by Allison.
 
2. Analyze the computer used by Kelly to identify any relevant file activities or evidence of data access.

3. Determine if there is a connection between the deleted files on Allison’s USB drive and the files present on Kelly’s computer.

## METHODOLOGY

The investigation was conducted using a combination of forensic tools and methodologies to analyze the file systems and metadata of the provided digital evidence. The following steps outline the methodology:

    File System Analysis of the USB Drive (Allison.dd):
        Tool Used: Sleuth Kit
        Process: Installed Sleuth Kit on Kali Linux and used the fls command to list the files and directories on the FAT32 partition of the USB drive. A timeline of file activities was generated using the mactime tool by converting the output of fls into a chronological format.

    Recovery of Deleted Files:
        Tool Used: Sleuth Kit
        Process: Identified deleted files from the USB drive by noting their inode numbers from the mactime output. Used the icat command to recover deleted .docx files and examined their contents and metadata using exiftool.

    Analysis of Kelly’s Computer (Kelly.dd):
        Tool Used: Plaso
        Process: Installed Plaso from source and used it to create a comprehensive timeline of file system events on Kelly’s computer. Generated a detailed CSV report of all file activities and relevant events.

    Timeline Comparison:
        Process: Compared the timelines of file activities from the USB drive and Kelly’s computer to identify any overlaps or suspicious activity. Focused on the creation and deletion of .docx files and other relevant documents.

By systematically applying these tools and methods, the investigation attempts to to find any evidence that would corroborate or refute Allison Origin’s claims about Kelly Copy’s alleged misuse of research data.

## FINDINGS

### Allison Origin Findings

Using these commands on a csv file created from Allison.dd to create a timeline:

```
bash
fls -l -m "/" -z CST6CDT -f fat32 -r -o 2 allison.dd > body.txt
mactime -b body.txt -d > allison.csv
```

The csv may be viewed in excel or IDE. VS Code is used in this case.  A search for '.docx' is performed and we find that the file:"/Treatment Plant Results of Purification.docx (deleted)" has beed deleted.  The file was deleted on Sun Jul 12 2015 22:00:00. The 'meta' column denotes the inode value which can be used in the following command to recover said file:

```
bash
icat -f fat32 -o 2 Allison.dd 69 > | recovered.docx
```
Next we viewed the file, and interrogated the metadata, respectively:
```
bash
libreoffice recovered.docx
exiftool recovered.docx
```

The file was created by Allison Origin, using Microsoft Macintosh Word at 2015:07_13 16:28:00, modified and saved/deleted 3 minutes later. 
This is another line from Allison's timeline:  
```
Sun Jul 12 2015 22:00:00,337839,.a..,r/rrwxrwxrwx,0,0,69,"/Treatment Plant Results of Purification.docx (deleted)"
```
### Kelly Copy Findings

A timeline is created using plaso, csv created, and a smaller file 'new.txt' to be interrogated:

```
bash 
~/plaso_env/bin/log2timeline --vss_stores 3 --volumes all --hashers all --parsers webhist,win7,win7_slow,win_gen --storage-file kelly2.plaso kelly.dd

~/plaso_env/bin/psort --output_time_zone "CST6CDT" -w kelly2.csv -o dynamic kelly2.plaso

grep .docx  kelly2.csv > new.txt
grep "\.docx" kelly2.csv > filter_docx.csv
```
The last two commands above filter similarily, but the second can be more accesible with an IDE or excel, making it more useful.

This line is found in Kelly Copy's timeline: 
```
2015-07-13T11:36:06.000000-05:00,Content Modification Time,LNK,Windows Shortcut,File size: 337839 File attribute flags: 0x00000020 Drive type: 3 Drive serial number: 0x4268856a Volume label:  Local path: C:\\Users\\Kelly Copy\\Desktop\\Grant\\Treatment Plant Results of Purification.docx Relative path: ..\\..\\..\\..\\..\\Desktop\\Grant\\Treatment Plant Results of Purification.docx Working dir: C:\\Users\\Kelly Copy\\Desktop\\Grant Link target: Grant Treatment Plant Results of Purification.docx,lnk,NTFS:\Users\Kelly Copy\AppData\Roaming\Microsoft\Windows\Recent\Treatment Plant Results of Purification.lnk,-
```

Kelly opened up a copy of the file at 2015-7-13 at 11:36, and recovered it from the recycle bin.  That is the earliest '.docx' mentioned in the timeline that has a "purification' in the referenece(title).


## Conclusion 
From the findings above, we can see that Allison Origin had a copy of the file before Kelly Copy. This investigation's finding suggest Allison Origin is the originator of the file in question.


