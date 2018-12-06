---
title: IoT to the Database Soldering, ORDS, Oracle Jet, Python and a little PL/SQL
layout: talk
body_class: talk
permalink: talks/iot-to-the-database-soldering-ords-oracle-jet-python-and-a-little-plsql
about: Blaine Carter is the Oracle developer advocate for open source. He applies his exploratory eye and tinkering inclinations to the intersection of open source and Oracle Database. He helps database developers improve their workflow using open source tools and promotes the use of open source inside and outside of Oracle. Blaine is a firm believer in learning by doing, failing, figuring it out and then sharing.
abstract: In this session, I'll walk through the tweet-a-watt project and explain a few changes I made to its included Python code. Then I'll build an Oracle Rest Data Services rest API and an Oracle JET application from scratch and tie it all together. I encourage the audience to try something new.
type: talk
expected_length: 45min
intended_audience: All
speakers: Blaine Carter
---

## Talk Description

If you're like me, you use way too much power and you’re not quite sure where. Tracking your power usage is a great start, but analyzing the data is often easiest when it's in a database. Having to type it in by hand would be a pain; let's void a warranty instead!

Building on the "Watch me make a Watt-watcher" project (https://learn.adafruit.com/tweet-a-watt), I will start by giving an overview of the steps and components used to assemble the hardware. Next, we'll discuss what to do with the data. As the project says, we can save it to a file on our computer, upload it to a database, tweet it or whatever you'd like.

Of course, I want my data in a database. I'll simplify the data ingestion by taking advantage of a REST interface to a cloud database. I will walk through choosing a table for the data and enabling a RESTful service on it.  Then I'll modify the project to post data to our new service.  Once we get some data in the table, I'll display the data in a graph.

You'll leave this session with the tools to track the data in your own projects and hopefully some new ideas.  (But no electrical burns!)
