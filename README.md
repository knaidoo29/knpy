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
  - `bins.bin_data`: Bins data.
  - `bins.edges2centers`: Bin edges to centers.
  - `bins.centers2edges`: Bin centers to edges.
  - `bins.rebin`: Rebins binned data.
  - `bins.divide_1D`: Divide data along 1 axis.
  - `bins.divide_ND`: Divide data along N axes.

- File utility:
  - `files.create_folder`: To create folders.
  - Functions for opening and outputting info on hdf5 files:
    - `files.get_hdf5_keys` to print the hdf5 keys and file structure.
    - `files.get_hdf5_data` retrieves the data of interest which is specified by the hdf5 keys.

- Gaussian Processes:
  - `gp.GaussianProcesses`: Class wrapping `george`'s Gaussian Process fitting function for a 1D function.

- Plotting utility:
  - `plot.FigureSize`: Class for ensuring figures and colorbars are the correct size so that all size definitions (fonts, etc) have a definitive rather than arbitrary meaning.
  - `plot.Healpy2Cartopy`: Converting Healpix map to 2D logitude and latitude grid. This allowing one to plot using `cartopy`'s transformation routines.
  - `plot.set_matplotlib_default`: Set default to latex fonts.

- Progress bar:
  - `utils.progress_bar`: Print's a changing progress bar to give visual updates of for-loop progression.

- Statistics:
  - `stats.Jackknife`: A jackknife resampling class.
  - `stats.round_up`: Rounding a number to a given significant figure.
