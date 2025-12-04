import json
from datetime import UTC, datetime
from functools import partial
from typing import Annotated, Literal
from uuid import UUID, uuid4

from pydantic import (
    BaseModel,        # Base class for all Pydantic models
    ConfigDict,       # Configuration settings for models
    EmailStr,         # Validates email format
    Field,            # Adds constraints and metadata to fields
    HttpUrl,          # Validates URLs
    SecretStr,        # Hides passwords when printing
    ValidationError,  # Raised when validation fails
    ValidationInfo,   # Context info during validation (not used in this code)
    # Creates calculated fields (like full_name from first+last)
    computed_field,
    field_validator,  # Custom validation for individual fields
    model_validator,  # Custom validation across multiple fields
)


class User(BaseModel):  # defining User class with Pydantic basemodel
    model_config = ConfigDict(
        populate_by_name=True  # allow population by field name
        strict=True  # enable strict type checking
        extra="allow"  # allow extra fields not defined in the model
        frozen=True  # make model immutable
    )

    # uid is field name of type UUID
    # Field is used to provide additional metadata and constraints
    # default_factory=uuid4 isuto-generates a unique ID if not provided
    # UUID type must be a valid UUID format
    # unique identifier with default value
    uid: UUID = Field(alias="id", default_factory=uuid4)
    # username field with length constraints
    username: Annotated[str, Field(min_length=3, max_length=50)]
    email: EmailStr  # email field validated as email format
    website: HttpUrl | None = None  # optional website field validated as URL
    # age field with range constraints
    age: Annotated[int, Field(ge=0, le=150)]
    # optional datetime field for verification status
    verified_at: datetime | None = None
    bio: str = ""
    is_active: bool = True  # boolean field for active status
    first_name: str = ""
    last_name: str = ""
    follower_count: int = 0
