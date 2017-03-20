from Main_class_dll import Main_class_dll
from version import VERSION

_version_ = VERSION
class SessionConnector(Main_class_dll):
    """
    This test library provides some keywords to allow
    opening, reading, writing, and saving Excel files
    from Robot Framework.
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
