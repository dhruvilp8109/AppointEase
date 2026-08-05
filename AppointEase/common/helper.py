import re

from common.constants import PASSWORD_LENGTH_SHOULD_BE_BETWEEN_8_TO_20, PASSWORD_MUST_HAVE_ONE_NUMBER, PASSWORD_MUST_HAVE_ONE_SMALLERCASE_LETTER, PASSWORD_MUST_HAVE_ONE_SPECIAL_CHARACTER, PASSWORD_MUST_HAVE_ONE_UPPERCASE_LETTER
from exceptions.exception_handler import CustomBadRequest


def validate_password(password):

    special_characters = r"[\$#@!\*]"

    if len(password) < 8 or len(password) > 20:
        return CustomBadRequest(message=PASSWORD_LENGTH_SHOULD_BE_BETWEEN_8_TO_20)
    if re.search('[0-9]', password) is None:
        return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_NUMBER)
    if re.search('[a-z]', password) is None:
        return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_SMALLERCASE_LETTER)
    if re.search('[A-Z]', password) is None:
        return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_UPPERCASE_LETTER)
    if re.search(special_characters, password) is None:
        return CustomBadRequest(message=PASSWORD_MUST_HAVE_ONE_SPECIAL_CHARACTER)
