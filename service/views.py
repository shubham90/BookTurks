"""
Views
"""
from service.bookturks.main_home_view import main_home_arena, login_check_arena, logout_arena
from service.bookturks.register_view import register_arena, register_check_arena
from service.bookturks.user_home_view import user_home_main_arena, user_quiz_init_arena, user_quiz_maker_arena, \
    user_quiz_verifier_arena, user_quiz_create_arena


def main_home(request):
    """
    Main Home Page
    Website landing page
    :param request: User request
    :return: Renders a page
    """
    return main_home_arena(request)


def login(request):
    """
    Login Check
    Validates login values
    :param request: User request
    :return: Renders a page
    """
    return login_check_arena(request)


def logout(request):
    """
    Logout
    Logs out the user
    :param request: User request
    :return: Renders a page
    """
    return logout_arena(request)


def register(request):
    """
    Register Page
    Register new account landing page
    :param request: User request
    :return: Renders a page
    """
    return register_arena(request)


def register_check(request):
    """
    Register Check
    Validates registration values
    :param request: User request
    :return: Renders a page
    """
    return register_check_arena(request)


def user_home(request):
    """
    User Home page
    User Dashboard and home landing page
    :param request: User request
    :return: Renders a page
    """
    return user_home_main_arena(request)


def user_quiz_init(request):
    """
    User Quiz Name verifier and initialization
    :param request: User request
    :return: Renders quiz name form
    """
    return user_quiz_init_arena(request)


def user_quiz_maker(request):
    """
    User Quiz Maker page
    :param request: User request
    :return:  Renders a page
    """
    return user_quiz_maker_arena(request)


def user_quiz_verifier(request):
    """
    User Quiz Verifier page and answer key generator
    :param request: User request
    :return:  Renders a page
    """
    return user_quiz_verifier_arena(request)


def user_quiz_create(request):
    """
    Creates the quiz and uploads to the storage
    :param request: User request
    :return: Redirects to dashboard
    """
    return user_quiz_create_arena(request)
