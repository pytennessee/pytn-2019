---
title:  A Taxonomy of Decorators' A-E
layout: talk
body_class: talk
permalink: talks/-a-taxonomy-of-decorators-ae
about: Andy Fundinger is a senior engineer at Bloomberg, where he develops Python applications in the Data License group and supports Python developers throughout the firm through the company's Python Guild. Andy has spoken twice at PyGotham, as well as other conferences such as QCon, EuroPython, and SaltConf. In the past, Andy has worked on private equity and credit risk applications, web services, and virtual worlds. Andy holds a Masters of Engineering from Stevens Institute of Technology. In his spare time, Andy is a maker who works on Internet of Things (IoT) projects and teaches classes at MakerBar in Hoboken, NJ.
abstract: Since their addition in Python 2.4, Decorators have become an established part of the Python language and many of our development projects. This talk will look at the purpose, implementation, and pitfalls of five types of decorators, from the Argument changing decorator to the Execution decorator.
type: talk
expected_length: 30min
intended_audience: Intermediate
speakers: Andy Fundinger
---

## Talk Description

This talk will briefly go over the various decorator syntaxes before breaking up the common usages of decorators into 5 categories. Effectively, these are design patterns for decorators. The usages to be considered are:

* A - Argument Changing Decorators -- Decorators that change a function's arguments, including changing its signature
* B - Binding Decorators -- Decorators that implement the Descriptor Protocol, such as the builtins: @property, @classmethod, and @staticmethod
* C - Control Flow Decorators -- Decorators that change when or whether the function will be called, such as @retry or @lrucache
* D - Descriptive Decorators -- Decorators that do not change the function, but create a reference to it elsewhere, like pytest.mark and flask.app.route
* E - Execution Decorators -- Decorators that retrieve source code and/or AST and alter it.

