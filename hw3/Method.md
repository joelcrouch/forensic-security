### Methods

These are the commands used for this assignment.

Get the image via scp: scp crouchj@ada.cs.pdx.edu:/disk/scratch/forensics/fsf.dd.bz2 fsf.dd.bz2

Unzip it: bzip2 -dc fsf.dd.bz2 > fsf.dd

Create a forensics image:
```
bash
sudo apt-get install dc3dd
dc3dd if=fsf.dd of=out.dd verb=on hash=sha256 hlog=out.hlog rec=off

sudo kpartx -av fsf.dd
```
add map loop0p1 (254:1): 409600 linear 7:0 40
add map loop0p2 (254:1): 0 15538176 linear &:0 411648  
--You may have to install kpartx 
Note the output of this command.  You will need it for the next step
```
bash
mkdir ~/fsf
sudo mount -t ntfs-3g -o ro,noexec /dev/mapper/loopXp2 ~/fsf
```

use the output from the kpartx command and replace 'loopXp2' with 'loop0p2'

Get a cat.jpg from the internet or any jpg and interrogate it with these commands:
```
bash
xxd cat.jpg | head -n 1  = ffd8
xxd cat.jpg | tail -n 1  ==ffd9
```
Now interrogate fsf.dd:

xxd fsf.dd | grep header 
where 'header'= ffd8. Lets make it a little more convenient for us.  We want JPgdata and JFIF is included in the header so lets use:
```
bash
xxd fsf.dd | grep -m 100 "ffd8" | grep JFIF
```
That gives us a little more manageable content. Lets use the first one, and see where that takes us.

0167f000" ffd8 ffe0 0010 4ar6 4946 0001 0100 0001 ......JFIF......

This will be alot of output.  Maybe add '| less' to make it more manageable for human eyes. 

Now take the first address:0167f000, and get the decimal val:  

echo $((0x167f000))  23588864
start = 23588864
Now use this command:
xxd -s <start in decimal> fsf.dd | grep footer
xxd -s 23588864 fsf.dd | grep ffd9

### Automated File Carving 

#### Foremost

```
bash
sudo apt-get install foremost
foremost -T -t jpg,gif,pdf -i fsf.dd
```
-T = audit log creation
-t jpg,gif,pdg looks for these types of files.
-i specifies the input file.

After running that command, foremost returned 204 jpgs and 137 gif's.  No pdf's were returned.  
Lets take a look at the jpgs.  There are 204 of them, so lets see if we cant make that more palatable.  

```bash
sudo apt-get install bc

```
and then save this as a 'zsh' file if you are on a zsh terminal, or 'sh' if you are using bash.
```
bash
!/bin/zsh 


# Set the directory path
dir="output_Mon_Aug__5_10_41_04_2024/jpg"


# Check if the directory exists
if [[ ! -d "$dir" ]]; then
  echo "Directory $dir does not exist."
  exit 1
fi

# Initialize an array with the .jpg files
files=($dir/*.jpg)

# Check if the array is empty
if [[ ${#files[@]} -eq 0 ]]; then
  echo "No .jpg files found in $dir."
  exit 1
fi

# Process each file
for file in $files; do
  lat=$(exiftool -GPSLatitude -n "$file" | awk -F': ' '{print $2}')
  lon=$(exiftool -GPSLongitude -n "$file" | awk -F': ' '{print $2}')
  if [[ -n "$lat" && -n "$lon" ]]; then
    if (( $(echo "$lat > 41.5 && $lat < 42.0 && $lon > -88.0 && $lon < -87.0" | bc -l) )); then
      echo "$file was taken around Chicago"
    fi
  fi
done
```

That yields 20 jpgs. There may be more because the lat/long values are general.  

```bash
/get_location.zsh
output_Mon_Aug__5_10_41_04_2024/jpg/00068224.jpg was taken around Chicago  (apple)
output_Mon_Aug__5_10_41_04_2024/jpg/00087312.jpg was taken around Chicago   (macys)
output_Mon_Aug__5_10_41_04_2024/jpg/00092808.jpg was taken around Chicago  (starbucks)
output_Mon_Aug__5_10_41_04_2024/jpg/00097472.jpg was taken around Chicago  (mall locagtion 1)
output_Mon_Aug__5_10_41_04_2024/jpg/00102464.jpg was taken around Chicago  (mall locagtion 1)
output_Mon_Aug__5_10_41_04_2024/jpg/00107384.jpg was taken around Chicago  (NOrdstroms)
output_Mon_Aug__5_10_41_04_2024/jpg/00112352.jpg was taken around Chicago  (the Gap)
output_Mon_Aug__5_10_41_04_2024/jpg/00116408.jpg was taken around Chicago  (gift cards at starbucks)
output_Mon_Aug__5_10_41_04_2024/jpg/00280944.jpg was taken around Chicago   (the gap)
output_Mon_Aug__5_10_41_04_2024/jpg/00284997.jpg was taken around Chicago (nordastroms)
output_Mon_Aug__5_10_41_04_2024/jpg/00289957.jpg was taken around Chicago (apple)
output_Mon_Aug__5_10_41_04_2024/jpg/00294571.jpg was taken around Chicago (starbucks)
output_Mon_Aug__5_10_41_04_2024/jpg/00334544.jpg was taken around Chicago (Neiman Marcus)
output_Mon_Aug__5_10_41_04_2024/jpg/00340128.jpg was taken around Chicago (barnes & Noble)
output_Mon_Aug__5_10_41_04_2024/jpg/00346384.jpg was taken around Chicago (abercrombie)
output_Mon_Aug__5_10_41_04_2024/jpg/00352544.jpg was taken around Chicago (outside mall location)
output_Mon_Aug__5_10_41_04_2024/jpg/00358264.jpg was taken around Chicago (giftcards)
output_Mon_Aug__5_10_41_04_2024/jpg/00362424.jpg was taken around Chicago  (gift cards)
output_Mon_Aug__5_10_41_04_2024/jpg/00366816.jpg was taken around Chicago  (apple gift cards)
output_Mon_Aug__5_10_41_04_2024/jpg/00370368.jpg was taken around Chicago  (happy birthday cards)
```


The output above is from the script outlined above. The pictures have been opened and inspected.  The pictures are of a mall near Chicago, Illinois.  The pictures depict various stores that are common in malls, some gift card pictures, and a picture of a 'happy birthday' display.



We can iterrogate the gif files similarily, however the gif files do not contain lat/long data.  Visually inspecting the gif files reveals that there are many different flag gifs, 'operation working' gifs, and flashy 'new' gifs.  