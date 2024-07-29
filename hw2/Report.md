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

### Findings
 
The employee KT had this itinerary of conferences to attend:

    2011
        Mar 13-18 Memphis
        Mar 21-25 New Orleans
        Jul 14-20 Chicago
        Oct 04-06 St. Louis
    2012
        Feb 20-21 Las Vegas
        Jun 07-10 Nashville
        Jul 12-15 Chicago
    2013
        Jan 23-25 Minnesota
        Jul 16-20 Chicago
    2014
        Mar 19-21 Indianapolis
This script was ran to produce the locations of photos taken found in KT's hard drive:
```
python

import os
import subprocess

# Path to the output file
output_file = '/home/joel/ktunes_jpginfo.txt'
# Directory containing JPG files
directory = '/home/joel/mfb/Pictures'

# Function to extract metadata from a single file using exiftool
def extract_metadata(file_path):
    try:
        # Run exiftool command to get metadata
        result = subprocess.run(
            ['exiftool', '-GPSLatitude', '-GPSLongitude', '-DateTimeOriginal', file_path],
            capture_output=True, text=True
        )
        
        # Check if exiftool command was successful
        if result.returncode == 0:
            output = result.stdout
            
            # Extract GPS and Date/Time information
            gps_latitude = next((line.split(': ')[1] for line in output.splitlines() if 'GPS Latitude' in line), 'N/A')
            gps_longitude = next((line.split(': ')[1] for line in output.splitlines() if 'GPS Longitude' in line), 'N/A')
            datetime_original = next((line.split(': ')[1] for line in output.splitlines() if 'Date/Time Original' in line), 'N/A')
            
            # Write to output file
            with open(output_file, 'a') as f:
                f.write(f"Metadata for {file_path}:\n")
                f.write(f"GPS Latitude: {gps_latitude}\n")
                f.write(f"GPS Longitude: {gps_longitude}\n")
                f.write(f"Date/Time Original: {datetime_original}\n\n")
        else:
            with open(output_file, 'a') as f:
                f.write(f"Error occurred while processing {file_path}.\n")
                
    except Exception as e:
        with open(output_file, 'a') as f:
            f.write(f"Exception occurred: {e}\n")

# Ensure the output file is empty or created
with open(output_file, 'w') as f:
    pass

# Check if directory exists
if not os.path.isdir(directory):
    with open(output_file, 'a') as f:
        f.write(f"Directory {directory} does not exist.\n")
else:
    # Process each JPG file in the directory
    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.jpg'):
            file_path = os.path.join(directory, file_name)
            extract_metadata(file_path)
```

This is the output.  Some of the files did not have GPS metadata: 
```
text
Metadata for /home/joel/mfb/Pictures/12.jpg:
GPS Latitude: 41 deg 52' 59.40" N
GPS Longitude: 87 deg 40' 1.20" W
Date/Time Original: 2012:07:14 21:17:00

Metadata for /home/joel/mfb/Pictures/13.jpg:
GPS Latitude: 40 deg 6' 49.20" N
GPS Longitude: 88 deg 12' 28.80" W
Date/Time Original: 2012:09:28 21:30:40

Metadata for /home/joel/mfb/Pictures/10.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 2012:06:09 16:27:10

Metadata for /home/joel/mfb/Pictures/17.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 2014:07:18 16:31:48

Metadata for /home/joel/mfb/Pictures/06.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 2012:06:08 19:50:30

Metadata for /home/joel/mfb/Pictures/03.jpg:
GPS Latitude: 40 deg 5' 46.80" N
GPS Longitude: 88 deg 14' 10.20" W
Date/Time Original: 2011:10:01 21:43:38

Metadata for /home/joel/mfb/Pictures/15.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 

Metadata for /home/joel/mfb/Pictures/07.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 2011:03:21 22:37:37

Metadata for /home/joel/mfb/Pictures/09.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 2012:06:09 16:14:27

Metadata for /home/joel/mfb/Pictures/11.jpg:
GPS Latitude: 41 deg 53' 3.60" N
GPS Longitude: 87 deg 39' 54.60" W
Date/Time Original: 2012:07:15 20:33:37

Metadata for /home/joel/mfb/Pictures/08.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 2011:07:16 15:44:29

Metadata for /home/joel/mfb/Pictures/16.jpg:
GPS Latitude: 40 deg 6' 24.63" N
GPS Longitude: 88 deg 13' 25.11" W
Date/Time Original: 2013:09:27 01:16:20

Metadata for /home/joel/mfb/Pictures/01.jpg:
GPS Latitude: 35 deg 2' 43.80" N
GPS Longitude: 90 deg 1' 22.80" W
Date/Time Original: 2011:03:18 14:58:09

Metadata for /home/joel/mfb/Pictures/02.jpg:
GPS Latitude: 40 deg 7' 3.60" N
GPS Longitude: 88 deg 14' 27.60" W
Date/Time Original: 2011:09:25 23:19:14

Metadata for /home/joel/mfb/Pictures/04.jpg:
GPS Latitude: 38 deg 36' 54.00" N
GPS Longitude: 90 deg 11' 45.60" W
Date/Time Original: 2011:10:06 21:21:53

Metadata for /home/joel/mfb/Pictures/14.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 

Metadata for /home/joel/mfb/Pictures/18.jpg:
GPS Latitude: 41 deg 53' 3.26" N
GPS Longitude: 87 deg 39' 57.49" W
Date/Time Original: 2014:07:19 17:16:02

Metadata for /home/joel/mfb/Pictures/05.jpg:
GPS Latitude: N/A
GPS Longitude: N/A
Date/Time Original: 2012:06:08 14:20:40

```


In 2011, KT had a conference in Memphis (mar13-18).  The GPS coordinates (35.0455, -90.023) pertiaing to that date show KT at Graceland at 14:58.  Graceland is located near Memphis, where the conference was held.  The data shows KT being in/around St. Louis on the appointed date(3-26-11).
On 6-8-12, the jpg '05.jpg' show a picture taken at a concert at 14:58.  No GPS data is included in the file.  KT was scheduled for a conference Memphis 6-7-12 thru 6-10-12.
On 7/14/2012 KT had a conference in Chicago.  The  GPS coordinates: GPS Latitude: 41 deg 52' 59.40" N
GPS Longitude: 87 deg 40' 1.20" W show him in Chicage at W. Washington and S. Michigan.  jpg.11 shows a concert.  The timestamp is at 20:33, and the GPS coordinates put KT in a Chicago North Side location.

Files that did not have GPS data or Date/Time of original were modifed at ~2015:06:30 07:58:55. 

### PDF 
There is a pdf in ~KevinTunes/Documents :ol 11291307605-327242879-ticket.pdf 
When exiftool  11291307605-327242879-ticket.pdf is applied to it, we can see that it was created by EventBrite at 2014 9-23 at 10:03 am.  The pdf referes to a concert ot be held on 9/14 called Pygmalion festival.  