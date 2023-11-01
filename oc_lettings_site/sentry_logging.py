import sentry_sdk
import logging


class SentryHandler(logging.Handler):
    def emit(self, record):
        try:
            sentry_sdk.capture_message(record.getMessage(), level=record.levelname)

        except Exception:
            self.handleError(record)
