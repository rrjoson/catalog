from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages


def slices(page, per_page):
    '''
    Used to help setup pagination
    '''
    stop = page * per_page
    if page == 1:
        start = 0
    else:
        start = stop - per_page
    return start, stop
