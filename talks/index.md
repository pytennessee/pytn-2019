---
title: Talk List
layout: base
body_class: talk-list
permalink: talks
---

# {{ site.data.event.name }} Talk List

## Keynotes

<ol class="talks">
{% assign talks = site.talks | where: 'type', 'keynote' %}
{% for talk in talks %}
  <li class="talk">
    <h3 class="talk-title"><a href="{{ talk.url }}">{{ talk.title }}</a></h3>
    <h4 class="talk-speakers">{{ talk.speakers | join: ', '}}</h4>
    <p class="talk-abstract">{{ talk.abstract }}</p>
  </li>
{% endfor %}
</ol>

## Talks

<ol class="talks">
{% assign talks = site.talks | where: 'type', 'talk' %}
{% for talk in talks %}
  <li class="talk">
    <h3 class="talk-title"><a href="{{ talk.url }}">{{ talk.title }}</a></h3>
    <h4 class="talk-speakers">{{ talk.speakers | join: ', '}}</h4>
    <p class="talk-abstract">{{ talk.abstract }}</p>
  </li>
{% endfor %}
</ol>


## Tutorials

<ol class="tutorials">
{% assign tutorials = site.talks | where: 'type', 'tutorial' %}
{% for talk in tutorials %}
  <li class="tutorial">
    <h3 class="talk-title"><a href="{{ talk.url }}">{{ talk.title }}</a></h3>
    <h4 class="talk-speakers">{{ talk.speakers | join: ', '}}</h4>
    <p class="talk-abstract">{{ talk.abstract }}</p>
  </li>
{% endfor %}
</ol>
