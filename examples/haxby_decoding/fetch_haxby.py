import os

# fetch haxby dataset
from nilearn.datasets import fetch_haxby
haxby = fetch_haxby()

# print instructions
print("To make a local copy of the data for subj2, run:")
print("$ cp -a {} .".format(os.path.dirname(haxby.func[0])))
      
