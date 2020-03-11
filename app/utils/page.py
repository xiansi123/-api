from rest_framework.pagination import PageNumberPagination
#LimitOffsetPagination 基于偏移方式的分页
# CursorPagination 加密

class MyPagination(PageNumberPagination):
    # 同样一般在配置文件中设置
    page_size = 2

    # 指定url中的参数
    page_size_query_param = 'page_size'
    max_page_size = 10000


