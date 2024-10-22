Subfolders 
	- data: 	Example source data snippets acquired at the Berlin Brain-Body Imaging Lab in Berlin, Germany, provided by courtesy of Klaus Gramann and Friederike Hohlefeld.
			Gramann, K., Hohlefeld, F.U., Gehrke, L. et al. 
			Human cortical dynamics during full-body heading changes. 
			Sci Rep 11, 18186 (2021). https://doi.org/10.1038/s41598-021-97749-8 
	- scripts: 	Battery of scripts showing how to use MNE BIDS tools and FieldTrip BIDS tools to convert EEG and Motion data sets to BIDS formatted data sets. 
			

Made for BIDS v1.9.0
	- EEG : 	https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html
	- MOTION : 	https://bids-specification.readthedocs.io/en/stable/modality-specific-files/motion.html

Contacts 
 	- Julius Welzel (@JuliusWelzel on Github) & Sein Jeung (@sjeung on Github), respectively produced example scripts for Python and Matlab tracks
	

-----------------------------------------------------------------------------------------------------------

Dependencies for Python-based track:
- Python 3.10 or newer
- pip:
	- mne==1.4.0
	- mne-bids==0.12
	- mnelab==0.8.6
	- pyxdf==1.16.4

-----------------------------------------------------------------------------------------------------------

Dependencies for Matlab-based track 
- Matlab 2019a or newer (older versions may mot be compatible with the use of built-in writematrix.m function)
- Latest version of FieldTrip or FieldTrip LITE : 
		https://www.fieldtriptoolbox.org/download/	

Additional resources for MATLAB, EEGLAB users
- For better handling of latencies & intermodality time synchronization in EEG + Motion setup, see function bemobil_bids2set.m in BeMoBIL pipeline (https://github.com/BeMoBIL/bemobil-pipeline)
- For reading the BIDS-formatted data into EEGLAB, see EEG-BIDS by Arno Delorme : https://github.com/sccn/EEG-BIDS
 	