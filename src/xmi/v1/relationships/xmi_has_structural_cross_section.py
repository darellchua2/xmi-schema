# Optional, for forward declarations in Python 3.7+
from __future__ import annotations

from ..xmi_base import XmiBaseRelationship, XmiBaseEntity
from ..constants import *


class XmiHasStructuralCrossSection(XmiBaseRelationship):
    __slots__ = XmiBaseRelationship.__slots__

    def __init__(self, source: XmiBaseEntity, target: XmiBaseEntity, **kwargs):
        name = 'hasStructuralCrossSection'

        super().__init__(source, target, name, **kwargs)