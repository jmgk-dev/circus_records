from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.response import TemplateResponse

from wagtail.models import Page
from wagtail.search.query import SearchQuery


def search(request):
    search_query = request.GET.get("query", None)
    page = request.GET.get("page", 1)

    if search_query:
        search_results = Page.objects.live().search(search_query)
        # add_hit() records this query in Wagtail's search promotions feature,
        # so popular searches can be surfaced in the admin for content tuning.
        SearchQuery.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Paginator handles both missing page numbers and out-of-range requests
    # gracefully by falling back to page 1 or the last page respectively.
    paginator = Paginator(search_results, 10)
    try:
        search_results = paginator.page(page)
    except PageNotAnInteger:
        search_results = paginator.page(1)
    except EmptyPage:
        search_results = paginator.page(paginator.num_pages)

    return TemplateResponse(
        request,
        "search/search.html",
        {
            "search_query": search_query,
            "search_results": search_results,
        },
    )
