"""
Wrapper for DataBridges client, making it easier to load data in Python, R and STATA.
"""

from .get_data import DataBridgesShapes
from .load_stata import load_stata

__all__ = ['DataBridgesShapes', 'load_stata']
