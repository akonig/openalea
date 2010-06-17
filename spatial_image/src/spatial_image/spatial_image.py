# -*- python -*-
#
#       spatial_image: spatial nd images
#
#       Copyright 2006 INRIA - CIRAD - INRA  
#
#       File author(s): Jerome Chopard <jerome.chopard@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
# 
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
"""
This module create the main SpatialImage object
"""

__license__= "Cecill-C"
__revision__=" $Id: $ "

from numpy import ndarray,asarray

class SpatialImage (ndarray) :
	"""Associate meta data to ndarray
	"""
	def __new__ (cls, input_array, resolution = None,
	                               vdim = 1,
	                               info = None) :
		"""Instantiate a new SpatialImage
		
		if resolution is None, vdim will be used to infer space size and affect
		a resolution of 1 in each direction of space
		
		:Parameters:
		 - `cls` - internal python
		 - `input_array` (array) - data to put in the image
		 - `resolution` (tuple of float) - spatial extension in each direction
		                                   of space
		 - `vdim` (int) - size of data if vector data are used
		 - `info` (dict of str|any) - metainfo
		"""
		#initialize datas
		obj = asarray(input_array).view(cls)
		
		#assert resolution
		if resolution is None :
			resolution = (1.,) * (len(obj.shape) - vdim + 1)
		elif len(resolution) != (len(obj.shape) - vdim + 1) :
			raise ValueError("data dimension and resolution mismatch")
		
		obj.resolution = tuple(resolution)
		
		#set metadata
		if info is None :
			obj.info = {}
		else :
			obj.info = dict(info)
		
		#return
		return obj
	
	def __array_finalize__ (self, obj) :
		if obj is None :
			return
		
		#assert resolution
		res = getattr(obj, 'resolution', None)
		if res is None :#assert vdim == 1
			res = (1.,) * len(obj.shape)
		
		self.resolution = tuple(res)
		
		#metadata
		self.info = dict(getattr(obj, 'info', {}) )
