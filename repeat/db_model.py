import reflex as rx
from typing import List

import sqlmodel
import sqlalchemy

class User(rx.Model, table=True):
    """A table of Users."""

    username: str
    password: str
    ingredients: List[str] = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(sqlalchemy.ARRAY(sqlalchemy.String)),
    )
