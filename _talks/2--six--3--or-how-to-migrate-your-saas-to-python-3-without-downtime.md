---
title: 2 + six = 3 - or how to migrate your SaaS to Python 3 without downtime!
layout: talk
body_class: talk
permalink: talks/2--six--3--or-how-to-migrate-your-saas-to-python-3-without-downtime
about: Stratasan developer and wayward Nashvillian, Anthony Fox, was born at a very young age and his hobbies include Breakfast, Lunch, and Dinner. In addition to that, he co-organizes the OCPython meetup in Orange County, California and likes to speak on various topics relating to Python and programming in general. Having recently migrated his company's application from Python 2 to Python 3 without downtime, he's here to share the good word that it's possible for others to do the same!
abstract: Time is flying by and Python 2 will drop support on January 1st, 2020. But upgrading to Python 3 doesn't have to be stressful, it turns out that there's a beaten path that will lead you and your application into Python 3-land without downtime!
type: talk
expected_length: 45min
intended_audience: All
speakers: Anthony Fox
---

## Talk Description


Time is flying by and Python 2 will drop support on January 1st, 2020. But upgrading to Python 3 doesn't have to be stressful, it turns out that there's a beaten path that will lead you and your application into Python 3-land without downtime!

In this talk, we'll cover a very effective strategy for converting your SaaS from Python 2 to Python 3. Including, but not limited to, topics such as:

* Planning the upgrade
* Writing code that's Python 2 and 3 compatible
* Using automated fixers
* Python 3 deployment options
* And much more! 

In addition to what's mentioned above, the speaker also brings personal experience having just upgraded his company's 75k line code base to Python 3 and will be sharing insights along the way. This talk is aimed towards maintainers of a SaaS but has elements that can easily be applied to library maintainers as well. 

## Outline:

* Intro (3m)
	* Speaker and company intro
	* Setting the context and purpose of the talk
* Total Cost of the 2 to 3 Conversion (2m)
	* How many GitHub tickets were created
	* How long did the actual conversion take
* Background on Python 3 adoption vs Python 2 (3m)
	* Why Python 3 adoption was slow
	* Overview of trends in adoption in recent years
* The Upgrade Roadmap Outline (2 minutes)
* The Upgrade Roadmap in Detail
	* Why having a modest test suite will make this easier. (2m)
	* What to do with 3rd party libraries that don't support Python 3 (5m)
		* Opportunities to contribute to OSS along the way
	* Python 3 Syntax Changes (10m)
		* The `__future__` library
		* How to write code that's compatible with Python 2 and 3
		* Which automated fixer utilities will help
		* Oh yeah... Unicode is a big thing now!
			* Why Unicode is the source of your pain
			* Why it's very much a necessary pain (hint: not everyone speaks English!)
	* Getting Your  Test Suite Passing in Python 2 and 3 (7m)
	* Deploying Python 3 (3m)
		* How we rolled out Python 3 with our environment
		* Other methods of deployment
	* Cleaning Up Compatibility Code (3m)
* Wrap Up/Q&A (5m)

