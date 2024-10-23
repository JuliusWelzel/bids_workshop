# BIDS workshop (Python & Matlab tracks) - EEG & Motion data conversion

## Subfolders

- **data**: Example source data snippets with subfolders sourcedata and bids

```
/data
├── sourcedata
│   ├── 1
│   │   └── control_body.xdf
│   └── 2
│       └── control_body.xdf
├── bids
│   ├── sub-01
│   │   ├── eeg
│   │   │   └── sub-01_task-SpotRotation_eeg.eeg
|
│   └── sub-02
│       ├── eeg
│       │   └── sub-02_task-SpotRotation_eeg.eeg

```
## Specifications

The specifications for the BIDS format can be found at the following links:
- **EEG**: [BIDS EEG Specification](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/electroencephalography.html)
- **MOTION**: [BIDS Motion Specification](https://bids-specification.readthedocs.io/en/stable/modality-specific-files/motion.html)


## Dependencies for Python-based track
You can also install depedecies via the 'pyproject.toml' file using the following command:
```bash
pip install -r pyproject.toml
```

- Python 3.10 or newer
- pip:
	- `mne==1.4.0`
	- `mne-bids==0.12`
	- `mnelab==0.8.6`
	- `pyxdf==1.16.4`



## Contacts

- Julius Welzel ([@JuliusWelzel](https://github.com/JuliusWelzel)) & Sein Jeung ([@sjeung](https://github.com/sjeung)), respectively produced example scripts for Python and Matlab tracks
