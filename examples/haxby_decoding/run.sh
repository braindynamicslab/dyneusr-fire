#!/bin/bash


# fetch haxby dataset, make a local copy
if ! test -d subj2 ; then
	python fetch_haxby.py
	cp -a ~/nilearn_data/haxby2001/subj2 .
fi


# mask_nifti (using --mask_img or --labels_img) and save as numpy
dyneusr-fire mask_nifti \
	     --func subj2/bold.nii.gz \
	     --mask_img subj2/mask4_vt.nii.gz \
	     --detrend True \
	     --smoothing_fwhm 4.0 \
	     --low_pass 0.09 \
	     --high_pass 0.008 \
	     --t_r 2.5 \
	     --standardize True \
	     --save_as subj2_bold_mask4_vt.npy

# run dyneusr-fire as normal, loading data from numpy
dyneusr-fire load_data --X subj2_bold_mask4_vt.npy --y subj2/labels.txt \
	     - run_mapper --resolution 15 --gain 0.4 \
	     - visualize --save_as "dyneusr_subj2.html"




