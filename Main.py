#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/11/28'


import sys
import os
from PyPDF2 import PdfFileReader,PdfFileWriter


PATH = sys.path[0]


class Mergepdf:
    def __init__(self, merged_name='merged.pdf', merge_files=[]):
        self.merged_name = merged_name
        self.merge_files = merge_files

    def merge(self):
        output = PdfFileWriter()

        for each in self.merge_files:
            pdf = PdfFileReader(open(each, 'rb'))

            for page in pdf.pages:
                output.addPage(page)

        output_stream = open(PATH + '/output/' + self.merged_name, 'wb')
        output.write(output_stream)
        output_stream.close()


def find_all_pdfs(filepath):
    result = []
    for root, dirs, files in os.walk(filepath):
        for each in files:
            if os.path.splitext(each)[1].lower() == '.pdf':
                result.append(os.path.join(root, each))
    return result


# ---[test zone]---
a = find_all_pdfs(PATH + '/source')
b = Mergepdf(merge_files=a)
b.merge()


