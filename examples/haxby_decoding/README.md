# `haxby_decoding`

This example uses fMRI data from the Haxby et al. 2001 decoding study to
demonstrate how to run the `dyneusr-fire` pipeline on real neuroimaging 
data. This example usese Nilearn's `datasets.fetch_haxby()` function to
download data for a single subject. See below for a few examples.



## Downloading the data


To download the data for this example, run:
```
$ python fetch_haxby.py
```




## Running `dyneusr-fire`


### Option 1 (`run.sh`)


You can run `dyneusr-fire` directly from the terminal, e.g., 
```
$ dyneusr-fire mask_nifti \
             --func subj2/bold.nii.gz \
             --mask_img subj2/mask4_vt.nii.gz \
             --detrend True \
             --smoothing_fwhm 4.0 \
             --low_pass 0.09 \
             --high_pass 0.008 \
             --t_r 2.5 \
             --standardize True \
        - load_data --y subj2/labels.txt \
        - run_mapper --resolution 20 --gain 0.4 \
        - visualize --save_as "dyneusr_subj2.html"
```


Note, the preprocessing settings are optional, feel free to skip and just mask the data, e.g.,
```
$ dyneusr-fire mask_nifti --func subj2/bold.nii.gz --mask_img subj2/mask4_vt.nii.gz \
        - load_data --y subj2/labels.txt \
        - run_mapper --resolution 20 --gain 0.4 \
        - visualize --save_as "dyneusr_subj2.html"
```



The example above can be broken down into two steps: masking your data, and running the `DyNeuSR` pipeline. First, you will need to save your masked data as a `*.npy` file, e.g.,
```
$ dyneusr-fire mask_nifti \
             --func subj2/bold.nii.gz \
             --mask_img subj2/mask4_vt.nii.gz \
             --detrend True \
             --smoothing_fwhm 4.0 \
             --low_pass 0.09 \
             --high_pass 0.008 \
             --t_r 2.5 \
             --standardize True \
             --save_as subj2_bold_mask4_vt.npy

```


Then, you can run the pipeline as normal, e.g., 
```
$ dyneusr-fire load_data --X subj2_bold_mask4_vt.npy --y subj2/labels.txt \
        - run_mapper --resolution 20 --gain 0.4 \
        - visualize --save_as "dyneusr_subj2.html"
```




### Option 2 (`run_interactive.sh`)


To run `dyneusr-fire` inside an IPython environment, run:
```
$ dyneusr-fire init -- --interactive
```


You can then interact with the `DyNeuSR` pipeline inside the IPython environment, e.g.,
```
In [1]: pipeline = DyNeuSR()
Out[1]: <__main__.DyNeuSR at 0x1a1cf65e50>

In [2]: pipeline.mask_nifti(
   ...:     func="subj2/bold.nii.gz", 
   ...:     mask_img="subj2/mask4_vt.nii.gz",
   ...:     detrend=True,
   ...:     smoothing_fwhm=4.0,
   ...:     low_pass=0.09,
   ...:     high_pass=0.008,
   ...:     t_r=2.5,
   ...:     standardize=True,
   ...:     );

In [3]: pipeline.run_mapper();

In [4]: pipeline.visualize();

```
