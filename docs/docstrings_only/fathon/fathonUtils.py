#    fathonUtils.py - utils functions for fathon package
#    Copyright (C) 2019-2020  Stefano Bianchi
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
import numpy as np
def subtractMean(vec):
	"""Subtracts mean of a vector.
	
	Parameters
	----------
	vec : iterable
		Python iterable whose mean will be subtracted.
	
	Returns
	-------
	numpy ndarray
		`vec` with its mean subtracted.
	"""
	return 0

def toAggregated(vec):
	"""Subtracts mean of a vector and computes the cumulative sum.
	
	Parameters
	----------
	vec : iterable
		The vector to be integrated.
	
	Returns
	-------
	numpy ndarray
		Cumulative sum of `vec` after subtraction of its mean.
	"""
	return 0

def linRangeByStep(start, end, step=1):
    """Array of linearly separated elements.
    
    Parameters
    ----------
    start : int
        Smallest element.
    end : int
        Biggest element.
    step : int
        Step between two consecutive elements (default : 1).
    """
    return 0

def linRangeByCount(start, end, count=-1):
    """Array of linearly separated elements.
    
    Parameters
    ----------
    start : int
        Smallest element.
    end : int
        Biggest element.
    count : int
        Number of elements (default : `end` - `start` + 1).
    """
    return 0

def powRangeByStep(start, end, step=1, base=2):
    """Array of elements given by `base` raised to linearly separated exponents.
    
    Parameters
    ----------
    start : int
        Smallest element.
    end : int
        Biggest element.
    step : int
        Step between two consecutive exponents (default : 1).
    base : int
        Base of the exponential (default : 2).
    """
    return 0

def powRangeByCount(start, end, count=-1, base=2):
    """Array of elements given by `base` raised to linearly separated exponents.
    
    Parameters
    ----------
    start : int
        Smallest element.
    end : int
        Biggest element.
    count : int
        Number of elements (default : `end` - `start` + 1).
    base : int
        Base of the exponential (default : 2).
    """
    return 0

