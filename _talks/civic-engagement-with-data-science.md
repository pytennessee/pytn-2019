---
title: Civic Engagement with Data Science
layout: talk
body_class: talk
permalink: talks/civic-engagement-with-data-science
about: 
abstract: I use data science to help people identify legislation they may be interested in given their location, their legislators, and their policy interests.
type: talk
expected_length: 30min
intended_audience: All
speakers: Alexander Poon
---

## Talk Description

I use data science to answer the question: **What (state) legislation should I pay attention to?**

This might include legislation that:

- pertains to local issues in the city/town/county where I live
- pertains to issues I care about (e.g.: education)
- is introduced by my Representative/Senator
- is contentious (e.g.: comes down to a close or party line vote)

This information comes from legislative text and metadata pertaining to bills from OpenStates, a database providing comprehensive information related to state legislators and legislation for all 50 states, including bill text, topics, sponsors, progress through committees, amendments, vote tallies and votes by individual legislators.

Natural Language Processing is a field of data science concerned with processing text as data. I use Python modules (spaCy, NLTK, scikit-learn) to perform common NLP tasks such as:

- tokenizing (segmenting documents into smaller, meaningful units of text)
- lemmatizing (converting plural nouns/conjugated verbs to their root form)
- part of speech tagging (identifying nouns, verbs, etc.)
- named entity recognition (e.g.: distinguishing references to Apple the company vs. apple the fruit)
- removing stop words (words like articles and pronouns that don’t carry a lot of meaning) 

I then create a numeric representation of text that can be used to create data visualizations, calculate statistics, and as the input to a machine learning model. The goal in creating an ML model will be to answer some of these questions prospectively (e.g.: can I predict which bills be contentious before they are actually voted on so that people might call their legislator and express an opinion?).

In answering my substantive question, I illustrate uses of NLP modules so that attendees will be able to apply these tools to other text problems they may be interested in.
