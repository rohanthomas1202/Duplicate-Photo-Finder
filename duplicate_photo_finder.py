import os
import imagehash

from PIL import Image


# the folder where your photos are stored
folder = 'photos'

# create a dictionary to store the filenames and their hashes
hashes = {}

# iterate over all files in the folder
for root, dirs, files in os.walk(folder):
    for file in files:
        # get the full path of the file
        path = os.path.join(root, file)

        # open the image file
        image = Image.open(path)

        # compute the hash of the file using the pHash algorithm
        hash = imagehash.phash(image)



        # add the file and its hash to the dictionary
        hashes[path] = hash

# iterate over the dictionary and print any duplicate files
for path, hash in hashes.items():
    for other_path, other_hash in hashes.items():
        if path != other_path and hash == other_hash:
            # try to compare the size of the images, and catch the FileNotFoundError if it occurs
            try:
                if os.stat(path).st_size < os.stat(other_path).st_size:
                    # print the paths of the files
                    print(f'Deleting {path} (smaller file)')
                    print(f'Keeping {other_path}')
                    # try to delete the smaller image, and catch the FileNotFoundError if it occurs
                    try:
                        os.remove(path)
                    except FileNotFoundError:
                        pass
                else:
                    # print the paths of the files
                    print(f'Deleting {other_path} (smaller file)')
                    print(f'Keeping {path}')
                    # try to delete the smaller image, and catch the FileNotFoundError if it occurs
                    try:
                        os.remove(other_path)
                    except FileNotFoundError:
                        pass
            except FileNotFoundError:
                pass


