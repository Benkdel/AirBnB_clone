#!/usr/bin/python3
"""
    class review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
        class inherits from BaseModels
    """

    place_id = ""
    user_id = ""
    text = ""
