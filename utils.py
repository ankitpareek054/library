def paginate_query(query, page, per_page):
    return query.paginate(page=page, per_page=per_page, error_out=False).items
