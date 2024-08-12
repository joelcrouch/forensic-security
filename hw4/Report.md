
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