# -*- coding: utf-8 -*-
"""
***************************************************************************
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
    """Load QPackage class from file QPackage.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .QPackage import QPackage
    return QPackage(iface)
