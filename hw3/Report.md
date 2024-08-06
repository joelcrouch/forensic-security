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

