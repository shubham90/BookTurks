from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from service.bookturks.alerts import init_alerts

from service.bookturks.Constants import USERNAME, PASSWORD, ALERT_MESSAGE, ALERT_TYPE, DANGER, SERVICE_MAIN_HOME, \
    SERVICE_USER_HOME, MAIN_HOME_PAGE, USER, REQUEST


def main_home_arena(request):
    """
    Main home page
    Sends alerts if registration successful or login failure
    :param request: user request
    :return: renders a page with context
    """

    request, alert_type, alert_message = init_alerts(request=request)

    # Creating context
    context = {
        REQUEST: request,
        USER: request.user,
        ALERT_MESSAGE: alert_message,
        ALERT_TYPE: alert_type
    }

    return render(request, MAIN_HOME_PAGE, context)


def login_check_arena(request):
    """
    Checks login authentication result and gives failure alert if unsuccessful
    :param request: user request
    :return: renders a page with context
    """

    username = request.POST[USERNAME]
    password = request.POST[PASSWORD]

    # Authenticate the user with the provided username and password.
    # Django authentication is used here.
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            # Authentication successful
            auth_login(request, user)
            return HttpResponseRedirect(reverse(SERVICE_USER_HOME))

        else:
            # Authentication failure as user was disabled.
            # Creating respective alerts.
            message = "This account has been disabled. Contact the admin."
            alert_type = DANGER
            request.session[ALERT_MESSAGE] = message
            request.session[ALERT_TYPE] = alert_type
            return HttpResponseRedirect(reverse(SERVICE_MAIN_HOME))

    else:
        # Authentication failure
        # the authentication system was unable to verify the username and password
        message = "The username or password were incorrect."
        alert_type = DANGER
        request.session[ALERT_MESSAGE] = message
        request.session[ALERT_TYPE] = alert_type
        return HttpResponseRedirect(reverse(SERVICE_MAIN_HOME, ))


def logout_arena(request):
    """
    Logs out user
    :param request: user request
    :return: renders a page with context
    """

    logout(request)
    return HttpResponseRedirect(reverse(SERVICE_MAIN_HOME, ))
