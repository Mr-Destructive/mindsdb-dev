from mindsdb.integrations.libs.const import HANDLER_TYPE
from .__about__ import __version__ as version, __description__ as description

try:
    from .google_analytics_handler import GoogleAnalyticsHandler as Handler

    import_error = None
except Exception as e:
    Handler = None
    import_error = e
title = 'Google Analytics'
name = 'google_analytics'
type = HANDLER_TYPE.DATA
permanent = True
__all__ = [
    'Handler', 'version', 'name', 'type', 'title', 'description', 'import_error'
]
