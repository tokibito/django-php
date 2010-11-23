from django.http import HttpResponse

from djangophp.utils import find_template, run_php

def direct_to_php(request, template):
    source, display_name = find_template(template)
    content = run_php(
        display_name,
        request_method=request.method,
        query_string=request.META.get('QUERY_STRING', ''),
        content_type=request.META.get('CONTENT_TYPE', ''),
        post_data=request.raw_post_data
    )
    return HttpResponse(content)
