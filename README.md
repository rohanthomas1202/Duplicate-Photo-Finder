Duplicate Photo Finder

This program is a simple tool that helps you find and delete duplicate photos in a given folder. It uses the pHash algorithm to compare the contents of the photos, and it keeps the larger (or higher resolution) version of the duplicate photos.
Requirements

    Python 3.6 or later
    imagehash and Pillow libraries

Installation

To install the required libraries, you can use the following pip commands:

pip install imagehash
pip install Pillow

Usage

To use the program, you need to specify the folder where your photos are stored. You can do this by setting the folder variable in the code to the path of the folder. For example:

folder = 'C:\Users\rohan\Pictures\Photos'

Then, you can run the program using the following command:

python duplicate_photo_finder.py

The program will scan the given folder and all its subfolders, and it will compute the pHash of each photo. It will then compare the hashes of all photos, and it will print the paths of any duplicate photos it finds.

Finally, the program will keep the larger (or higher resolution) version of the duplicate photos, and it will delete the smaller (or lower resolution) ones. It will print the paths of the files it keeps and deletes, so that you can verify that the correct files are being processed.
Limitations

The program uses the pHash algorithm to compare the photos, which is a good method for detecting similar images. However, it is possible that the program may miss some duplicates if the photos are very different, such as if they have been edited in a significant way. In addition, the program only compares the size of the photos to determine which one to keep and which one to delete. If the photos have the same size but different resolutions, the program may not always choose the correct one to keep.
Future Work

In the future, the program could be improved by using a more advanced algorithm for comparing the photos, such as a neural network. This would allow the program to detect duplicates even if the photos are significantly different, and it would also allow the program to compare the resolution of the photos in addition to their size.
