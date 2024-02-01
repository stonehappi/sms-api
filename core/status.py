from enum import Enum


class EStatus(int, Enum):
    INACTIVE = 0
    ACTIVE = 1
    DRAFT = 2
    DELETED = 3
    PENDING = 4
    REJECTED = 5
    APPROVED = 6
    PUBLISHED = 7
    UNPUBLISHED = 8
    ARCHIVED = 9
    CANCELLED = 10
    COMPLETED = 11
    FAILED = 12
    SUCCESSFUL = 13
