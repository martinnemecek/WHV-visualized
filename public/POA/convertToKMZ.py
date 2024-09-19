import zipfile
import os

def kml_to_kmz(kml_file_path, kmz_file_path):
    # Ensure the KML file exists
    if not os.path.isfile(kml_file_path):
        raise FileNotFoundError(f"KML file not found: {kml_file_path}")

    # Create a KMZ file (which is essentially a ZIP file with a .kmz extension)
    with zipfile.ZipFile(kmz_file_path, 'w', zipfile.ZIP_DEFLATED) as kmz:
        kmz.write(kml_file_path, os.path.basename(kml_file_path))

# Example usage
kml_file = './10.kml'
kmz_file = './10.kmz'
kml_to_kmz(kml_file, kmz_file)
