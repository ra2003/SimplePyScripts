#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


"""Скрипт парсит файл формата fb2, вытаскивает из него картинки и сохраняет их в папке с таким же названием,
как файл fb2."""


import os
import base64
import io

import xml.sax
from PIL import Image

from common import sizeof_fmt


def do(file_name, debug=True):
    dir_im = os.path.splitext(file_name)[0]
    if not os.path.exists(dir_im):
        os.makedirs(dir_im)
    debug and print(dir_im + ':')

    # Analog: fb2_pictures__using_xml_expat.py

    PARSE_DATA = {
        'last_start_tag': None,
        'last_tag_attrs': None,
        'last_tag_data': '',
        'total_image_size': 0,
        'number': 1,
    }

    class BinaryHandler(xml.sax.ContentHandler):
        def startElement(self, name, attrs):
            PARSE_DATA['last_start_tag'] = name
            PARSE_DATA['last_tag_attrs'] = attrs
            PARSE_DATA['last_tag_data'] = ''

        def characters(self, content):
            if PARSE_DATA['last_start_tag'] != 'binary':
                return

            PARSE_DATA['last_tag_data'] += content

        def endElement(self, name):
            if name != 'binary':
                return

            data = PARSE_DATA['last_tag_data']

            try:
                im_id = PARSE_DATA['last_tag_attrs']['id']
                im_file_name = os.path.join(dir_im, im_id)

                im_data = base64.b64decode(data.encode())
                count_bytes = len(im_data)
                PARSE_DATA['total_image_size'] += count_bytes

                with open(im_file_name, mode='wb') as f:
                    f.write(im_data)

                im = Image.open(io.BytesIO(im_data))
                debug and print('    {}. {} {} format={} size={}'.format(
                    PARSE_DATA['number'], im_id, sizeof_fmt(count_bytes), im.format, im.size
                ))

                PARSE_DATA['number'] += 1

            except:
                import traceback
                traceback.print_exc()

    parser = xml.sax.make_parser()
    parser.setContentHandler(BinaryHandler())
    parser.parse(file_name)

    file_size = os.path.getsize(file_name)
    debug and print()
    debug and print('fb2 file size =', sizeof_fmt(file_size))
    debug and print('total image size = {} ({:.2f}%)'.format(
        sizeof_fmt(PARSE_DATA['total_image_size']), PARSE_DATA['total_image_size'] / file_size * 100
    ))


if __name__ == '__main__':
    fb2_file_name = '../input/Непутевый ученик в школе магии 1. Зачисление в школу (Часть 1).fb2'
    do(fb2_file_name)
