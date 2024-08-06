## Summary

This report details the investigation of a forensic image of a thumb drive taken from Jenny Card. Jenny Card was arrested in Chicago for selling fraudulent gift cards from various retail stores. The forensic analysis aims to uncover evidence related to these illegal activities.

## Purpose
The purpose of this investigation is to examine the forensic image of the thumb drive confiscated from Jenny Card. By analyzing the data within the image, we aim to uncover and document any evidence of fraudulent activities, including the creation, distribution, and sale of counterfeit gift cards. 

## Methodology

In order to obtain data pertenent to the investigation, we Kali Linux, setup as a virtual machine.  The image was obtained from the server 'ada.cs.pdx.edu' and decompressed.
```
bash
scp <user_name>@ada.cs.pdx.edu:/disk/scratch/forensics/fsf.dd.bz2 fsf.dd.bz2
bzip2 fsf.dd.bz2 fsf.dd
```
The forensic image was then mounted:
```
bash
sudo kpartx -av fsf.dd
mkdir ~/fsf
sudo mount -t ntfs-3g -o ro,noexec /dev/mapper/loopXp2 ~/fsf
```

No data was available so more sophisticated methods were employed.
Attempts were made to extract the data manually, but ultimately automated tools were employed
to extract the data.

The tools 'foremost' and 'photorec' were installed.
```
bash
sudo apt-get install foremost
foremost -T -t jpg,gif,pdf -i fsf.dd
udo apt-get install testdisk
photorec fsf.dd

```

Both of these methods created much data.  A custom python script was created to find GPS signatures of photos that were near the alleged scene of the crime.  20 photos were found that were taken in and around the Chicago area.  These photos were acquired from the foremost tool.  The photorec tool (part of the testdisk suite) gathered many more photos (jpg, gif, png), but GPS data was lacking in many of them.


### Data analysis and Visualizaation

The extracted files of interest, that had pertinent GPS data were copied into a directory.  A custom python script was created to visualize the locations of the pictures.  A  file named 'map.html' may be opened up in the web browser of your choice, and locations of the the pictures can be viewed.

## Findings

Multiple pictures were found of various retail stores were discovered on the hard drive, as well as pictures of gift cards from said retail stores including Neiman Marcus, Nordstroms, the Gap, Abercrombie, and Starbucks.  A photo of a 'happy birthday' display was also discovered with the same GPS (Chicago-Land) coordinates.  
Many .txt files were found by the photorec that have the structure of algorithmic keys, similar to a product key used for installing a new operating system.  

## Conclusion

The forensic investigation of the thumb drive seized from Jenny Card revealed significant evidence linking her to the fraudulent activities. Numerous photos of various retail stores and gift cards from these stores were discovered on the drive, indicating her involvement in documenting and possibly planning the fraudulent use of these cards. Additionally, several .txt files containing sequences resembling product keys were found. These files likely contain different keys for the gift cards, further supporting the suspicion of her engagement in the creation and distribution of fraudulent gift cards. 




