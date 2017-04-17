import pandas as pd
import numpy as np 

class Spectrum(pd.DataFrame):
    def __init__(self, wavelength, reflectance, reflectance_sigma, transmission_data=None):
        if transmission_data is not None:
            raise NotImplementedError()        
        super(Spectrum,self).__init__({"wavelength":wavelength, "reflectance":reflectance, "sigma_r":reflectance_sigma})        

    

    @property
    def wavelength(self):
        return self['wavelength'].values
    @property
    def reflectance(self):
        return self['reflectance'].values
    @property
    def sigma_r(self):
        return self['sigma_r'].values
    @property
    def transmission(self):
        raise NotImplementedError()
        return self['transmission'].values
    @property
    def sigma_t(self):
        raise NotImplementedError()
        return self['sigma_t'].values
    
    def save(self, filepath):
        if not filepath[-4:] =='.txt':
            filepath = filepath + '.txt.'
        np.savetxt(filepath, np.c_[self.wavelength, self.reflectance, self.sigma_r])

class Sample:
    def __init__(self, wavelength, particle_size, thickness, particle_index, matrix_index, medium_index=1, incident_angle=0):
        self.particle_size = particle_size # can we do something clever here with units? maybe using pint?
        self.thickness = thickness # again with the units
        self.wavelength = np.array(wavelength)
        n_wavelength = length(wavelength)
        
        self.particle_index = extend_array(particle_index)
        self.matrix_index = extend_array(matrix_index)
        self.medium_index = extend_array(medium_index)
        self.incident_angle = incident_angle

def extend_array(val, n):
    val = np.array(val)
    if len(val) == n:
        return val
    elif len(val) == 1:
        return np.repeat(val, n)
    else:
        raise IndexError("Arrays are of different lengths. Cannot interpret.")

def rescale(inarray):
    # Rescale values in an array to be between 0 and 1
    maxval = np.max(inarray)
    minval = np.min(inarray)
    return (inarray-minval)/(maxval-minval)

def find_close_indices(biglist, targets):

    # find the indices of interest in the data that correspond to target values
    target_ind = []
    for i, target in enumerate(targets):
        curr_ind = np.where(abs(biglist-wl) == np.min(abs(biglist-wl)))[0][0]
        target_ind.append(curr_ind)
    return target_ind

