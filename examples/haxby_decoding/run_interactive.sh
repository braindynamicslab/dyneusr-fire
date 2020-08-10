#!/bin/bash


# fetch haxby dataset, make a local copy
if ! test -d subj2 ; then
	python fetch_haxby.py
	cp -a ~/nilearn_data/haxby2001/subj2 .
fi


# example command-line
dyneusr-fire init -- --interactive