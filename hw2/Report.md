### The Case of Kevin Tunes

This report shows the location, and streaming habits of the employee: "Kevin Tunes", referred to as KT in this report.  Allegations have been made that KT has been breaking policy of the company that employs him.  The hard drive of KT's employer supplied laptop will be interrogated.  

## Methods

The laptop of KT has been appropriated, and a direct copy of the hard drive data has been made and mounted on a Kali virtual machine which has been produced with current security standards, ie per manufacturer instructions. 

```
bash 
$ curl -LO https://web.cecs.pdx.edu/~dmcgrath/del.dd.bz2
$ bzip2 -dc del.dd.bz2 > del.dd
$ sudo apt-get install dc3dd
$ dc3dd if=del.dd of=out.dd verb=on hash=sha256 hlog=out.hashlog log=log rec=off
$  mkdir ~/out
$ sudo mount -t ntfs-3g -o loop,ro,noexec out.dd ~/out


```