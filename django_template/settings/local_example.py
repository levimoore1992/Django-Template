# pylint: disable=duplicate-code

from django_template.settings.default import *  # noqa: F401,F403

ALLOWED_HOSTS.extend(
    [
        "localhost",
        "127.0.0.1",
    ]
)

# Toolbar requirements.
MIDDLEWARE.append(
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)
INSTALLED_APPS.extend(
    [
        "debug_toolbar",
        "django_extensions",
    ]
)
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: DEBUG}
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar_user_switcher.panels.UserPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
]


# Local Email
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "admin@localhost"


LOGGING = {
    "version": 1,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
}