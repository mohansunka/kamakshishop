from rest_framework.pagination import PageNumberPagination,\
    LimitOffsetPagination , CursorPagination


class MyPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'mypage'
    page_size_query_param = 'num'
    max_page_size = 5
    last_page_strings = ('endpage',)

# class MyPagination(LimitOffsetPagination):
#     # pass
#     default_limit = 2
#     limit_query_param = 'mylimit' # default  limit  not working
#     offset_query_param = 'myoffset'


# class MyPagination(CursorPagination):
#     # pass
#     ordering = '-salary'
#     # ordering = '-empname'
#     page_size = 4
