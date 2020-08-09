#!/usr/bin/env python3

# Copyright (C) 2012-2013 by Łukasz Langa
# Copyright (C) 2020 by Nguyễn Hồng Quân
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from app.models import Favourites, RegularIntegers
from django import forms
from django.forms.boundfield import BoundField


class HasBoundValue(object):
    """Bound value helpers for unit tests."""
    def _bound_value(self, field_name):
        field = self.fields[field_name]
        return BoundField(self, field, field_name).value()


class FavouritesForm(forms.ModelForm, HasBoundValue):
    class Meta:
        model = Favourites
        widgets = {
            'sport': forms.HiddenInput(),
        }
        exclude = ()


class RegularIntegersForm(forms.ModelForm, HasBoundValue):
    class Meta:
        model = RegularIntegers
        exclude = ()
