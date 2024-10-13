from fastapi_users.authentication import (
    AuthenticationBackend,
)

from .transport import bearer_transport
from .srategies import get_database_strategy

SECRET = "SECRET"

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
