---
title: Using Tests as a Tool to Wrangle Legacy Projects
layout: talk
body_class: talk
permalink: talks/using-tests-as-a-tool-to-wrangle-legacy-projects
about: Jason Swett helps Rails developers write better tests. Since putting his first website online in 1996, he has taught programming in four countries and worked for organizations like AT&T, Deloitte and the University of Chicago. Jason lives in Sand Lake, Michigan.
abstract: Legacy projects tend to lack test coverage. Unfortunately, legacy projects are also often written in such a way that it makes it difficult to add tests. A few powerful testing techniques can make it much easier to get legacy projects under control.
type: talk
expected_length: 30min
intended_audience: Intermediate
speakers: Jason Swett
---

## Talk Description

Most code in the world is legacy code. Legacy projects tend to be lacking in test coverage. Unfortunately, legacy projects are often written in such a way that it makes it difficult to add tests - tests that are badly needed in order to start paying down technical debt and get the project on the right track.

Fortunately there are some effective ways of wrangling legacy code into submission. If we can break apart a legacy project's entanglement of dependencies, making the code more modular and loosely coupled, we can add tests more easily. But breaking apart dependencies is tricky and requires a few certain techniques in order to be done safely.

Main points:

- Why legacy projects are harder to test than greenfield projects
- Why adding tests to legacy projects is risky
- How to mitigate the risks of modifying legacy code
- What dependency injection is, why it’s useful in testing legacy projects, and how to use it
- How to break dependencies using Michael Feathers’ “sprout class” technique
