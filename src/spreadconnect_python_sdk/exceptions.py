from typing import Optional
from spreadconnect_python_sdk.models.errors import ErrorResponse

class SpreadconnectError(Exception):
    """Base exception for all Spreadconnect SDK errors."""

    def __init__(self, status_code: int, message: str, error: Optional[ErrorResponse] = None):
        self.status_code = status_code
        self.message = message
        self.error = error
        super().__init__(f"[{status_code}] {message}")


class OrderError(SpreadconnectError):
    """Special exception for order-related errors that return an Order ErrorResponse."""

    def __init__(self, status_code: int, error: ErrorResponse):
        super().__init__(status_code, error.reason or "Order API Error", error=error)
        self.order_id = error.order_id
