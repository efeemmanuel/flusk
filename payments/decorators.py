from django.shortcuts import redirect

def verified_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.payment_set.filter(verified=True).exists():
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to an unauthorized page or return an error message.
            return redirect('/make_payment')  # You need to define 'unauthorized_page' in your URLs
    return _wrapped_view