---
title: About the Venue
body_class: venue
layout: base
permalink: venue
---

## PyTennessee 2019 Venue Information

The {{ site.data.event.venue.name }} has played host to {{ site.data.event.short_name }} since
the beginning, and we're excited to return to the NSL again this year!

{{ site.data.event.venue.description }}

- ### {{ site.data.event.venue.name }}
{% for line in site.data.event.venue.address %}- {{ line }}
{% endfor %}- <{{ site.data.event.venue.url }}>

{{ site.data.event.venue.map }}
