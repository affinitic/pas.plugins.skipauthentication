# -*- coding: utf-8 -*-
"""
pas.plugins.skipauthentication
------------------------------

Created by mpeeters
:license: GPL, see LICENCE.txt for more details.
"""

from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IPasPluginsSkipauthenticationLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ISkipAuthenticationPlugin(Interface):
    """Skip Authentication Plugin"""
