class SHKeeperError(Exception):
    """Base class for all exceptions in SHKeeper."""

    pass


class InvalidAPIKeyError(SHKeeperError):
    """Raised when the API key is invalid."""

    pass


class RateLimitError(SHKeeperError):
    """Raised when API rate limits are exceeded."""

    pass
