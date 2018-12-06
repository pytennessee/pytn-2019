---
title: "asyncio: We Did it Wrong"
layout: talk
body_class: talk
permalink: talks/asyncio-we-did-it-wrong
about: Lynn Root is a Lead Site Reliability Engineer at Spotify in NYC with historical issues of using her last name as her username, and the resident FOSS evangelist. She is also a global leader of PyLadies and former Vice Chair of the Python Software Foundation Board of Directors. When her hands are not on a keyboard, they are usually holding a bass guitar or paint brushes.
abstract: Everyone’s talking about it. Everyone’s using it. But most likely, they’re doing it wrong, just like we did. While building our own simplified chaos monkey, this talk will go through common mistakes and antipatterns, drawing from experience with how we’ve used asyncio in Spotify’s infrastructure.
type: talk
expected_length: 45min
intended_audience: All
speakers: Lynn Root
---

## Talk Description

Everyone’s talking about it. Everyone’s using it. But most likely, they’re doing it wrong, just like we did.

This talk will walk through building a very simplified [chaos monkey](https://github.com/Netflix/SimianArmy/wiki/Chaos-Monkey) using `asyncio`. While building this, I'll walk through common mistakes and anti-patterns, drawing from experience with how we’ve used `asyncio` in Spotify’s infrastructure. You’ll learn how to approach asynchronous & concurrent programming with Python’s `asyncio`, take away some best practices, and what pitfalls to avoid.
