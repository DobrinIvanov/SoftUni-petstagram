from enum import Enum


class Gender(Enum):

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    @classmethod
    def choices(cls):
        return [(gender.name, gender.value) for gender in cls]

