---
title: Small Scale Deployments on AWS
layout: talk
body_class: talk
permalink: talks/small-scale-deployments-on-aws
about: Ernst is a Product Marketing Manager for PyCharm at JetBrains. He writes about PyCharm and Python, and aims to make PyCharm better for Python developers. He currently lives in Munich, and has lived in four other countries before moving to Germany. He enjoys traveling and good food.
abstract: AWS is great when you're building the next Instagram. But how about when you're just putting together a website for a local business that gets very little traffic? Can we still follow deployment best practices when we limit ourselves to a single EC2 instance?
type: talk
expected_length: 30min
intended_audience: Intermediate
speakers: Ernst Haagsman
---

## Talk Description

Engineers from large companies always tell amazing stories about how they use AWS to handle tidal waves of users, and there's a lot of content out there for that. However, a common use case that gets far less attention is that of smaller projects. How can we use a small scale deployment of a personal project to learn about AWS best practices? How can we help out our friend who has has a small business and needs some web presence, but nothing very high traffic. 

Of course, there are solutions like Heroku that allow you to quickly and easily deploy things, and for the smallest cases this works great. But if you ever need to scale it just a little bit, it gets really expensive quickly. Let's see how we can use Terraform and Ansible to create a one-instance deployment for a Python web application. We'll look into configuring database backups to S3, and to see what further things we can achieve while still keeping things lean and mean for the kind of use case we're addressing here. Having all configuration in infrastructure-as-code and configuration management tools means it's very simple to integrate with a CI server and automate our deploys.
