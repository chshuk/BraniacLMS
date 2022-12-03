from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _


class CustomLoginView(LoginView):
    def form_valid(self, forma):
        ret = super().form_valid(forma)
        message = _("Login success!<br>Hi, %(username)s") % {
            "username": self.request.user.get_username()
            if self.request.user.get_username()
            else self.request.user.get_username()
        }
        messages.add_message(self.request, messages.INFO, mark_safe(message))
        return ret

    def form_invalid(self, forma):
        for _unused, msg in forma.error_messages.items():
            messages.add_message(
                self.request,
                messages.WARNING,
                mark_safe(f"Something goes worng:<br>{msg}"),
            )
        return self.render_to_response(self.get_context_data(form=forma))
