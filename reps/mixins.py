from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect

#Restricts what agents can see when logged in

class OrganizerAndLoginRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated and is an organizer."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_admin:
            return redirect("leads:lead-list")
        return super().dispatch(request, *args, **kwargs)