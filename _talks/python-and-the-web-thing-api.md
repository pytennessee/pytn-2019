---
title: Python and the Web Thing API
layout: talk
body_class: talk
permalink: talks/python-and-the-web-thing-api
about: I'm an Itinerant Engineer at the Mozilla Corporation having been involved with Mozilla for about thirteen years.  I've had a long and diverse career that includes optimal school bus routing, data analysis on Wall Street, online commerce of rose bushes and Firefox crash reporting.  It all started professionally with Fortran and moved to C/C++ and eventually Python. I have steadfastly refused to move into management as programming is my true calling. I suppose I am an eccentric. I've lived in a fancy tent on an organic farm for twenty-five years.  I've never known the meaning of the word "bored" as I can always find  projects and interesting things to explore.  My hobbies include unusual plants, intricate drawing and baroque music. I have seven greenhouses filled with organic veggies, orchids and carnivorous plants. In the last few years I’ve discovered that I can draw well enough show pieces in art galleries. Finally, while I own an oboe and a family of baroque recorders, I’ve settled on an electronic woodwind instrument, a Yamaha WX-5. Oh yeah, then there are the Harleys&#58; ’08 FX-STB Night Train and a ’15 Fat Boy Low. I believe that software engineering is as beholden to the whims of fashion as the apparel industry. I believe in abstraction, encapsulation and dependency injection. I believe that recovery from failure is even better than graceful failure. I love to code. I do not fear recursion. I do not fear complexity. I do not fear hard problems. 
abstract: With the Web Thing API, a W3C draft standard, the Internet of Things becomes the Web of Things. Mozilla's Things Gateway already implements it. Python's Home Assistant has declared intent to adopt it. What is this standard and how can we use it right now to write the corporate cloud out of IoT?
type: talk
expected_length: 45min
intended_audience: All
speakers: K Lars Lohn
---

## Talk Description

The draft W3C proposal, the Web Thing API, advances the idea that the proprietary silos of the Internet of Things aren't necessary. Using a Web tool based standard for device communication opens the field to millions of Web developers. It enables small manufacturers to create novel new devices without suffering the pay-to-play tax imposed by the five hundred pound gorillas that dominate the current IoT market. We can write the corporate cloud out of the picture but still get to use their devices.

Mozilla maintains a reference implementation of the standard within its Things Gateway project. Home Assistant, a Python native IoT system, has stated intent to implement the Web Thing API.

What can we do with it right now?

The possibilities are limitless. Using familiar Web, asynchronous tools and Mozilla's Things Gateway, we can transform any Web Service into a Web Thing. A weather service or even the price of BitCoin could become a trigger for home automation. Arduino projects can become Web Things and fully participate along side Philips HUE bulbs, ZWave switches, Samsung buttons or any of hundreds of other devices.

This talk will cover an overview of the standard, but more practically, show how to use it within the Python language. With live demos using Mozilla's Things Gateway and asynchronous Python tools, I will show how to create innovative new Web Things and orchestrate their interaction with each other. I will cut across proprietary silos and show how everyone can play nicely together.
