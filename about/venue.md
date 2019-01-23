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

### Need a Lyft?

We've partnered with Lyft to offer exclusive ride discounts to PyTennessee!
Use the code `PYTN2019` to save 10% off 4 rides to or from PyTennessee, which will get you there and back both days.
Be safe out there, y'all.

<div class="flex-container venue-info" markdown="1">

- ### {{ site.data.event.venue.name }}
{% for line in site.data.event.venue.address %}- {{ line }}
{% endfor %}- <{{ site.data.event.venue.url }}>

{{ site.data.event.venue.map }}

</div>
