# BIDS workshop (Python & Matlab tracks) - EEG & Motion data conversion
## Subfolders

- **data**: Example source data snippets

```
/data
├── sourcedata
│   ├── 1
│   │   └── control_body.xdf
│   └── 2
│       └── control_body.xdf
|
├── bids
│   ├── sub-01
│   │   ├── eeg
│   │   │   └── sub-01_task-SpotRotation_eeg.eeg
|
│   └── sub-02
│       ├── eeg
│       │   └── sub-02_task-SpotRotation_eeg.eeg

```
**Made for BIDS v1.9.0**

- **EEG**: [BIDS EEG Specification](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html)
- **MOTION**: [BIDS Motion Specification](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/motion.html)

## Contacts

- Julius Welzel ([@JuliusWelzel](https://github.com/JuliusWelzel)) & Sein Jeung ([@sjeung](https://github.com/sjeung)), respectively produced example scripts for Python and Matlab tracks

---

## Dependencies for Python-based track

- Python 3.10 or newer
- pip:
	- `mne==1.4.0`
	- `mne-bids==0.12`
	- `mnelab==0.8.6`
	- `pyxdf==1.16.4`

---

## Dependencies for Matlab-based track

- Matlab 2019a or newer (older versions may not be compatible with the use of built-in `writematrix.m` function)
- Latest version of [FieldTrip or FieldTrip LITE](https://www.fieldtriptoolbox.org/download/)

## Additional resources for MATLAB, EEGLAB users

- For better handling of latencies & intermodality time synchronization in EEG + Motion setup, see function `bemobil_bids2set.m` in [BeMoBIL pipeline](https://github.com/BeMoBIL/bemobil-pipeline)
- For reading the BIDS-formatted data into EEGLAB, see [EEG-BIDS by Arno Delorme](https://github.com/sccn/EEG-BIDS)