from PIL import Image, ImageDraw
from colors import color_range 
from sklearn.cluster import KMeans
import random, numpy as np

# Function that converts the badge to the requested specifications  
def convert(img_path):
    # Verification that the badge path exists
    try:
        img = Image.open(img_path)
    except:
        return False, "Image path does not exist"
    
    # Convert the format of the badge to RGBA (Adding transparency if is the case)
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    new_img_path = img_path.split(".",1)[0]+"_valid.png" # New badge is saved in the same path, with the same name adding "_valid"
    num_clusters = 3 # Number of clusters for the badge color sectorization (more clusters, more processing time)
    new_colors = color_range() # Colors consider as happy

    img_array = np.array(img) # Convert badge to numpy matrix

    flattened_img_array = img_array.reshape((-1, 3))

    # Grouping colores
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(flattened_img_array)

    # Assign each pixel to the nearest centroid
    clustered_img_array = kmeans.cluster_centers_[kmeans.labels_].astype(np.uint8)

    # Change badge colors to the "happy" ones
    for i in range(num_clusters):
        clustered_img_array[kmeans.labels_ == i] = random.choice(new_colors)
            
    clustered_img_array = clustered_img_array.reshape(img_array.shape) # Reform the matrix to the original form
    img = Image.fromarray(clustered_img_array) # Create a new image from the grouped matrix

    # Convert the format of the badge to RGBA (Adding transparency if is the case)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')

    # Convert the size of the badge file into 512x512
    img = img.resize((512, 512))

    img.save(new_img_path)

    return new_img_path