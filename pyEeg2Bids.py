from mnelab.io.xdf import read_raw_xdf
import mne
from mne_bids import write_raw_bids, BIDSPath, make_dataset_description
from pathlib import Path
from pyxdf import load_xdf

# get dir of this script
dir_project = Path(__file__).parent

# set paths
dir_source = dir_project.joinpath(r'data\sourcedata')
dir_root_bids =  dir_project.joinpath(r'data\bids')

# set bids info
task = 'SpotRotation'

# check for directories in source data
dirs_ids = [x for x in dir_source.iterdir() if x.is_dir()]

# check for .xdf files in each directory
for dir_id in dirs_ids:
    files_xdf = dir_id.glob('*.xdf')

    # process each xdf file with mne_bids
    for file_xdf in files_xdf:
        print(f"Working on {file_xdf.name}")

        # get info for BIDS
        # id from directory name, might be different for your data
        sub_id = '00' + dir_id.name

        # find eeg stream in .xdf file
        streams, _ = load_xdf(file_xdf)
        streams_ids = [stream["info"]["stream_id"] for stream in streams]
        stream_types = [stream['info']['type'] for stream in streams]

        # get id for eeg stream
        eeg_stream_id = streams_ids[stream_types.index(['EEG'])]
        
        # load to mne
        raw = read_raw_xdf(file_xdf, stream_ids=[eeg_stream_id], verbose=False)  # stream id has to be a list
        raw.info['line_freq'] = 50  # specify power line frequency as required by BIDS (European line frequency here)
        
        # delete events if they start before eeg recording
        events = mne.events_from_annotations(raw)

        # import the channel locations from a .elc file
        elc_file = file_xdf.parent.joinpath('channel_locations.elc')
        cust_layout = mne.channels.make_standard_montage('biosemi160')

        # make all channel type eeg
        raw.set_channel_types({ch: 'eeg' for ch in raw.ch_names})
        # set montage
        raw.set_montage(cust_layout)

        # specify BIDS path and write
        bids_path = BIDSPath(subject=sub_id, task=task, datatype='eeg', root=dir_root_bids)
        write_raw_bids(raw, bids_path, events=None, overwrite=True, allow_preload=True, format='BrainVision', verbose=True)

        print(f'Finished writing BIDS for participant {sub_id} and task {task}')


# make dataset description
make_dataset_description(
    path=bids_path.root,
    name="EEG and motion capture data set for a full-body/joystick rotation task",
    authors=["Gramann, K.", "Hohlefeld, F.U.", "Gehrke, L.", "Klug, M"],
    acknowledgements="n/a",
    data_license="n/a",
    funding=[""],
    references_and_links=[
        "Human cortical dynamics during full-body heading changes",
    ],
    doi="doi:https://doi.org/10.1038/s41598-021-97749-8",
    overwrite=True,
)
