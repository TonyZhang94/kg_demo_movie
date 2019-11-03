# -*- coding: utf-8 -*-


class IRIsPropertySet:
    def __init__(self):
        pass

    @staticmethod
    def return_birth_value():
        return u':personBirthDay'

    @staticmethod
    def return_birth_place_value():
        return u':personBirthPlace'

    @staticmethod
    def return_english_name_value():
        return u':personEnglishName'

    @staticmethod
    def return_person_introduction_value():
        return u':personBiography'

    @staticmethod
    def return_movie_introduction_value():
        return u':movieIntroduction'

    @staticmethod
    def return_release_value():
        return u':movieReleaseDate'

    @staticmethod
    def return_rating_value():
        return u':movieRating'

    @staticmethod
    def return_comedian_iris():
        return u':Comedian'

    @staticmethod
    def return_kungfuactor_iris():
        return u':KungFuActor'
