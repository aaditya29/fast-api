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

    @field_validator("username")  # this function validates username field
    @classmethod  # class method decorator
    def validate_username(cls, v: str) -> str:
        if not v.replace("_", "").isalnum():  # check if username is alphanumeric
            # raise error if not
            raise ValueError("Username must be alphanumeric")
        return v.lower  # return valid username

    # validate website field before standard validation
    @field_validator("website", mode="before")
    @classmethod
    def validate_website(cls, v: str | None) -> str | None:
        # if website is provided and doesn't start with http
        if v and not v.startswith("http"):
            return "http://" + v  # prepend http://
        return v  # return valid website or None

    @computed_field  # computed field for full name
    @property  # concatenate first and last names
    def display_name(self) -> str:
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"  # return full name
        return self.username  # return username if names are empty

    @computed_field  # computed field for account age
    @property
    def is_influencer(self) -> bool:
        return self.follower_count > 10000  # influencer if followers > 10000


class Comment(BaseModel):
    content: str  # Comment content
    author_email: EmailStr  # Author's email
    likes: int = 0  # Number of likes with default is 0


class BlogPost(BaseModel):
    # Title with length constraints
    title: Annotated[str, Field(min_length=1, max_length=200)]
    # Content with minimum length
    content: Annotated[str, Field(min_length=10)]
    author: User  # Author of the blog post
    view_count: int = 0  # View count with default is 0
    is_published: bool = False  # Publication status with default is False
    # List of tags with default empty list
    tags: list[str] = Field(default_factory=list)
    # Creation timestamp with default current time
    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    # Status with limited choices and default is draft
    status: Literal["draft", "published", "archived"] = "draft"
    # Slug with regex pattern constraint
    slug: Annotated[str, Field(pattern=r"^[a-z0-9-]+$")]

    # List of comments with default empty list
    comments: list[Comment] = Field(default_factory=list)


class UserRegistration(BaseModel):
    email: EmailStr  # user's email address
    password: str  # user's password
    confirm_password: str  # confirmation of the user's password

    @model_validator(mode="after")  # validate that passwords match
    def passwords_match(self) -> "UserRegistration":  # custom validation method
        if self.password != self.confirm_password:  # if passwords don't match
            # raise validation error
            raise ValueError("Passwords do not match")
        return self  # return the validated model instance
