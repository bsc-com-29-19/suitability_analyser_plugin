# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SuitabilityAnalyser
                                 A QGIS plugin
 Identify optimal locations for development projects using population density, proximity to roads and water bodies, and district boundaries. Visualise and export results directly on the map
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2024-11-30
        copyright            : (C) 2024 by plugin hacker
        email                : tonykanyamuka@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SuitabilityAnalyser class from file SuitabilityAnalyser.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .suitability_analyser import SuitabilityAnalyser
    return SuitabilityAnalyser(iface)