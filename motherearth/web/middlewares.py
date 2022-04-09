from motherearth.web.views.main import InternalErrorView


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code >= 500:
            return InternalErrorView.as_view()(request)

        return response

    return middleware


