# knpy

Personal python utility functions.

## Dependencies

- `python 3`
- `numpy`
- `matplotlib`
- `healpy`
- `h5py`
- `george`

## Installation

```
git clone https://github.com/knaidoo29/knpy.git
cd knpy
python setup.py build
python setup.py install
```

## Uses

- Binning functions:
  - `bins.rebin`: Rebins binned data.

- File utility:
  - Functions for opening and outputting info on hdf5 files:
    - `files.create_folder` to create a folder from python.
    - `files.get_hdf5_keys` to print the hdf5 keys and file structure.
    - `files.get_hdf5_data` retrieves the data of interest which is specified by the hdf5 keys.

- Plotting utility:
  - `plot.FigureSize`: Class for ensuring figures and colorbars are the correct size so that all size definitions (fonts, etc) have a definitive rather than arbitrary meaning.
  - `plot.Healpy2Cartopy`: Converting Healpix map to 2D logitude and latitude grid. This allowing one to plot using `cartopy`'s transformation routines.
  - `plot.set_matplotlib_default`: Set default to latex fonts.

- Progress bar:
  - `utils.progress_bar`: Print's a changing progress bar to give visual updates of for-loop progression.
