import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import folium

def get_exif_data(file_path):
    """Get EXIF data from an image file."""
    image = Image.open(file_path)
    exif_data = image._getexif()
    if not exif_data:
        return {}
    return {TAGS.get(tag, tag): value for tag, value in exif_data.items()}

def get_gps_coordinates(exif_data):
    """Extract GPS coordinates from EXIF data and convert to decimal degrees."""
    if not exif_data:
        return None

    gps_info = exif_data.get('GPSInfo', {})
    if not gps_info:
        return None

    try:
        lat = gps_info[2]
        lon = gps_info[4]
        lat_ref = gps_info[3]
        lon_ref = gps_info[1]

        lat_deg, lat_min, lat_sec = lat
        lon_deg, lon_min, lon_sec = lon

        latitude = dms_to_decimal(lat_deg, lat_min, lat_sec, lat_ref)
        longitude = dms_to_decimal(lon_deg, lon_min, lon_sec, lon_ref)

        return (latitude, longitude)
    except (KeyError, TypeError, IndexError):
        return None

def dms_to_decimal(degrees, minutes, seconds, direction):
    """Convert DMS coordinates to decimal degrees."""
    decimal = degrees + (minutes / 60) + (seconds / 3600)
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def main(directory):
    """Main function to plot GPS coordinates."""
    m = folium.Map(location=[41.8781, -87.6298], zoom_start=12)  # Centered on Chicago

    for file_name in os.listdir(directory):
        if file_name.lower().endswith('.jpg'):
            file_path = os.path.join(directory, file_name)
            exif_data = get_exif_data(file_path)
            coords = get_gps_coordinates(exif_data)

            if coords:
                latitude, longitude = coords
                print(f"Adding point for {file_name}: ({latitude}, {longitude})")  # Debug output
                folium.Marker(
                    location=[latitude, longitude],
                    popup=file_name
                ).add_to(m)

    filename = 'map.html'
    
    if len(m._children) > 1:  # Check if there are markers added
        m.save(filename)
        print(f"Map saved to {filename}")
    else:
        print("No coordinates to plot.")

if __name__ == '__main__':
    directory = 'chicago_images'  # Update with your directory
    main(directory)
# def get_exif_data(img_path):
#     """Extract EXIF data from an image."""
#     image = Image.open(img_path)
#     info = image._getexif()  # Get EXIF data
    
#     if info is None:
#         return {}
    
#     exif_data = {}
#     for tag, value in info.items():
#         tag_name = TAGS.get(tag, tag)
#         exif_data[tag_name] = value
    
#     return exif_data

# def get_gps_coordinates(exif_data):
#     """Extract GPS coordinates from EXIF data."""
#     if 'GPSInfo' not in exif_data:
#         return None

#     gps_info = exif_data['GPSInfo']
#     latitude = gps_info.get(2, (0, 0, 0))
#     longitude = gps_info.get(4, (0, 0, 0))

#     if gps_info.get(3) == 'S':
#         latitude = -latitude[0] - latitude[1]/60 - latitude[2]/3600
#     else:
#         latitude = latitude[0] + latitude[1]/60 + latitude[2]/3600

#     if gps_info.get(1) == 'W':
#         longitude = -longitude[0] - longitude[1]/60 - longitude[2]/3600
#     else:
#         longitude = longitude[0] + longitude[1]/60 + longitude[2]/3600

#     return latitude, longitude

# def main(directory):
#     """Main function to plot GPS coordinates."""
#     m = folium.Map(location=[41.8781, -87.6298], zoom_start=12)  # Centered on Chicago

#     for file_name in os.listdir(directory):
#         if file_name.lower().endswith('.jpg'):
#             file_path = os.path.join(directory, file_name)
#             exif_data = get_exif_data(file_path)
#             coords = get_gps_coordinates(exif_data)

#             if coords:
#                 latitude, longitude = coords
#                 print(f'Adding pint for {file_name}: ({latitude}, {longitude})')
#                 folium.Marker(
#                     location=[latitude, longitude],
#                     popup=file_name
#                 ).add_to(m)

#     if len(m._children) > 1:  # Check if there are markers added
#         m.save('map.html')
#         print("Map saved to map.html")
#     else:
#         print("No coordinates to plot.")

# if __name__ == "__main__":
#     directory = 'chicago_images'  # Directory containing the images
#     main(directory)