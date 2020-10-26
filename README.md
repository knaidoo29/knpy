# knpy

Personal python utility functions.

## Dependencies

- `numpy`
- `matplotlib`
- `healpy`

## Installation

```
git clone https://github.com/knaidoo29/knpy.git
cd knpy
python setup.py build
python setup.py install
```

## Uses

- Plotting utility:
  - `plot.FigureSize`: Class for ensuring figures and colorbars are the correct size so that all size definitions (fonts, etc) have a definitive rather than relative meaning.
  - `plot.Healpy2Cartopy`: Converting Healpix map to 2D logitude and latitude grid. This allowing one to plot using `cartopy`'s transformation routines.
  - `plot.set_matplotlib_default`: Set default to latex fonts.

- Progress bar:
  - `utils.progress_bar`: Print's a changing progress bar to give visual updates of for-loop progression.
