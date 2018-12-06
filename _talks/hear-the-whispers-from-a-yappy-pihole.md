---
title: Hear the whispers from a yappy Pi-hole
layout: talk
body_class: talk
permalink: talks/hear-the-whispers-from-a-yappy-pihole
about: I'm a Linux nerd, security dork and trained meteorologist working in DevOps for the last 6 years.  I love what I do, have security certifications in penetration testing and Python, am a Red Hat Certified Engineer, AWS Certified Solutions Architect and enjoy discussing what all of us at the conference are passionate about.  I graduated from the University of Kentucky (GO BIG BLUE) and Western Kentucky University and have made the Nashville area my home since meeting my wife.
abstract: Ad blocking is popular but some connected devices are more noisy than others.  Finding those devices that "phone home" less frequently can be difficult if it means filtering through the noise.  I started a project to test out data classes, async/await and fill in a gap in my DNS sinkhole recon.
type: talk
expected_length: 30min
intended_audience: All
speakers: Jeremy Young
---

## Talk Description

Using data classes and async/await functionality in Python 3.7 I query the Pi-hole web API (tested with Pi-hole FTL 4.0) to get a list of all requests currently in memory on the Pi-hole server.  Using Counter from Collections I return a list of names encountered and the frequency at which they've been requested.  Paring down the list to those encountered 100 times or less allows me to focus on sites forwarded to my upstream DNS server infrequently, highlighting ad sites I can block or potentially malicious traffic I may want to investigate.
