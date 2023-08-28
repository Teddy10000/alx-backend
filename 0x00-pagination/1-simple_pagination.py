#!/usr/bin/env python3
"""Write a function named index_range that takes two integer
arguments page and page_size.

The function should return a tuple of size two containing a
start index and an end index corresponding to the range of
indexes to return in a list for those particular pagination
parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.
"""

class CSVData:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.data = self.load_data()

    def load_data(self):
        data = []
        with open(self.csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data

    def index_range(self, page, page_size):
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return start_index, end_index

    def get_page(self, page=1, page_size=10):
        assert isinstance(page, int) and page > 0, "Page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size should be a positive integer"

        start_index, end_index = self.index_range(page, page_size)
        if start_index >= len(self.data):
            return []

        return self.data[start_index:end_index]
