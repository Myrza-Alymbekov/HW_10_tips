from rest_framework.pagination import PageNumberPagination


class QAPagePagination(PageNumberPagination):
    page_size = 3