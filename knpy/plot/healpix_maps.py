import numpy as np
import healpy as hp


class Healpy2Cartopy:

    """For the projection of healpix maps onto cartopy plots. Constructs a grid of points
    in longitude and latitude. 2 ngrid points are constructed in longitude and ngrid points
    in latitude.

    Basic usage
    -----------

    # initiate the class
    h2c = Healpy2Cartopy()
    # setup the longitude/latitude grid
    h2c.setup(ngrid=1000)
    # get the healpix pixels for the longitude/latitude grid
    nside = 128
    pix = h2c.getpix(nside)

    # conversion from healpix map to cartopy longitude/latitude grid
    healpy_map = # get the map somewhere
    lonlatgrid_map = healpy_map[pix]

    # to plot using cartopy mollweide projection use

    ax = plt.axes(projection=ccrs.Mollweide())
    ax.pcolormesh(np.rad2deg(h2c.lon2d), np.rad2deg(h2c.lat2d), lonlatgrid_grid, transform=ccrs.PlateCarree())
    plt.show()

    # clean and refresh the class
    h2c.clean()
    """

    def __init__(self):
        # initialises the class.
        self.ngrid = None
        self.latmin = None
        self.latmax = None
        self.lonmin = None
        self.lonmax = None
        self.lat = None
        self.lon = None

    def setup(self, ngrid=100, latmin=-90., latmax=90., lonmin=-180., lonmax=180.):
        # creates a grid of points for longitude and latitude coordinates.
        self.ngrid = ngrid
        self.latmin = latmin
        self.latmax = latmax
        self.lonmin = lonmin
        self.lonmax = lonmax
        _lat = np.linspace(np.deg2rad(latmin), np.deg2rad(latmax), self.ngrid+1)
        _lon = np.linspace(np.deg2rad(lonmin), np.deg2rad(lonmax), 2*self.ngrid+1)
        self.lat = 0.5*(_lat[1:] + _lat[:-1])
        self.lon = 0.5*(_lon[1:] + _lon[:-1])
        self.lon2d, self.lat2d = np.meshgrid(self.lon, self.lat)
        self.lat2d_healpy = np.deg2rad(90.) - self.lat2d
        self.lon2d_healpy = - self.lon2d

    def getpix(self, nside):
        # finds the healpix pixel for each point in the longitude latitude grid.
        return hp.ang2pix(nside, self.lat2d_healpy, self.lon2d_healpy)

    def clean(self):
        # clears and reinitialises the class.
        self.__init__()
