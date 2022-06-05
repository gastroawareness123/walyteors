from django.shortcuts import redirect, reverse

def select_language(view_func):
    def wrapper_func(request, *args, **kwargs):
        if not request.GET.get('language'):
            return redirect(f'{reverse("language_selected_page")}?next={request.path}')
        return view_func(request, *args, **kwargs)
    return wrapper_func