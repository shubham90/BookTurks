from django.http import HttpResponseRedirect
from django.http import Http404

from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User

from service.models import User as UserModel


def register_arena(request):
    alert_message = request.session.get('alert_message', None)
    alert_type = request.session.get('alert_type', None)
    if 'alert_message' in request.session:
        del request.session['alert_message']
        del request.session['alert_type']
    return render(request, 'service/register.html', {'alert_message': alert_message, 'alert_type': alert_type})


def register_check_arena(request):
    user_id = request.POST['user_id']
    user_first_name = request.POST['user_first_name']
    user_last_name = request.POST['user_last_name']
    user_email = request.POST['user_email']
    user_phone = request.POST['user_phone']
    user_dob = request.POST['user_dob']
    password = request.POST['password']
    repassword = request.POST['repassword']

    if user_id is None or \
                    user_email is None or \
                    user_first_name is None or \
                    user_last_name is None or \
                    user_phone is None or \
                    user_dob is None or \
                    password is None or \
                    password != repassword:
        message = "The password should be same in both the fields"
        alert_type = "danger"
        request.session['alert_message'] = message
        request.session['alert_type'] = alert_type
        return HttpResponseRedirect(reverse('service:register'))

    try:
        db_user = get_object_or_404(UserModel, user_id=user_id)
    except(Http404):
        pass
    else:
        message = "User ID already present"
        alert_type = "danger"
        request.session['alert_message'] = message
        request.session['alert_type'] = alert_type
        return HttpResponseRedirect(reverse('service:register'))

    auth_user = User.objects.create_user(user_id, user_email, password)
    user = UserModel(user_id=user_id,
                     user_email=user_email,
                     user_first_name=user_first_name,
                     user_last_name=user_last_name,
                     user_phone=user_phone,
                     user_dob=user_dob)
    user.save()
    message = "".join([user_id, " registered successfully"])
    alert_type = "success"
    request.session['alert_message'] = message
    request.session['alert_type'] = alert_type
    return HttpResponseRedirect(reverse('service:login_page'))
