# -*- python -*-
#
#       image: image morphology
#
#       Copyright 2006 INRIA - CIRAD - INRA
#
#       File author(s): Eric Moscardi <eric.moscardi@sophia.inria.fr>
#
#       Distributed under the Cecill-C License.
#       See accompanying file LICENSE.txt or copy at
#           http://www.cecill.info/licences/Licence_CeCILL-C_V1-en.html
#
#       OpenAlea WebSite : http://openalea.gforge.inria.fr
#
"""
This module import morphology functions
"""

__license__= "Cecill-C"
__revision__ = " $Id$ "

import numpy as np
from scipy import ndimage

__all__ = ["connectivity_4","connectivity_6","connectivity_8","connectivity_26","component_labeling"]


# Definition of 3D structure elements :
connectivity_4 = np.array([[[0],[1],[0]],[[1],[1],[1]],[[0],[1],[0]]])
connectivity_6 = ndimage.generate_binary_structure(3,1)
connectivity_8 = np.ones((3,3,1), dtype=bool)
connectivity_26 = np.ones((3,3,3), dtype=bool)

def component_labeling(img, structure=None, output=None, threshold=0, number_labels=0):
    """
    Connected-component label features in an array.

    :Parameters:
    - `img` (array) - object to be labeled.
    Any non-zero values in input are counted as features and zero values are considered the background.

    - `structure` (array) optional - structuring element that defines feature connections.
    structure must be symmetric.
    If no structuring element is provided, one is automatically generated with a squared connectivity equal to one.

    That is, for a 2D input array, the default structuring element is:

    array([[0,1,0],
           [1,1,1],
           [0,1,0]])

    - `output` (None, data-type, array) optional
    If output is a data type, it specifies the type of the resulting labeled feature array
    If output is an array-like object, then output will be updated with the labeled features from this function.

    - `threshold` (float) optional
    If threshold > 0, the threshold is used to the input
    The input contains elements 'False' if input < threshold, and elements 'True' elsewhere

    - `number_labels` (int)
    If number_labels > 0, number_labels of connected component labels is returned
    If number_labels = 1, the largest connected component label is returned

    :Returns Type:
    - `labeled_array` - array object where each unique feature has a unique value

    - `num_features` (int)
    If `output` is None or a data type, this function returns a tuple : (`labeled_array`, `num_features`).
    If `output` is an array, then it will be updated with values in :
    `labeled_array` and only `num_features` will be returned by this function.
    """

    if threshold:
        img = np.where(img < threshold, False, True)

    mat, num_features = ndimage.label(img, structure, output)

    if not number_labels:
        return mat, num_features

    object_labels = np.arange(1, num_features+1, dtype=np.int32)
    areas = np.array(ndimage.sum(img / img.max(), mat, object_labels))
    areas_decreasing = -np.sort(-areas)
    labels = object_labels[areas>=areas_decreasing[number_labels-1]]

    condlist = [mat==label for label in labels]
    choicelist = list(np.arange(1,number_labels+1))
    mat = np.select(condlist, choicelist)
    return mat, number_labels

