# !/usr/bin/env python
# -*- coding: utf-8 -*-

from okky import Okky
from campuspick import CampusPick


if __name__ == "__main__":
    okky = Okky()
    okky_title, okky_content = okky.get_title(), okky.get_content()
    print(okky_title, okky_content)
