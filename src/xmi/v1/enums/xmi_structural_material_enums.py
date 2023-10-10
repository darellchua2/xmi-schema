from .xmi_enums import XmiEnum


class XmiStructuralMaterialTypeEnum(XmiEnum):
    CONCRETE = 1, "Concrete"
    STEEL = 2, "STEEL"
    TIMBER = 3, "Timber"
    ALUMINIUM = 4, "Aluminium"
    COMPOSITE = 5, "Composite"
    MASONRY = 6, "Masonry"
    OTHERS = 7, "Others"
    REBAR = 8, "Rebar"  # to be removed
    TENDON = 9, "Tendon"  # to be removed
