---
title: Let's choose Kaizen instead of "The Rewrite"
layout: talk
body_class: talk
permalink: talks/lets-choose-kaizen-instead-of-the-rewrite
about: Brandon Williams is a Systems Engineer at Ramsey Solutions. He's been practicing DevOps for the last few years of his career as he's migrated from application development to AWS deployments and building/bundling application code for distribution. He finds joy in simplifying processes, understands that simple is not easy, and loves sharing all that he learns. When not writing code, blog posts, or listening to technology podcasts, he enjoys going for hikes and playing board and card games with his wife and kids.
abstract: New team. Old code. The code is complex and lacking any automated testing. You're tasked with a "small" change to a massive build script. You want to "fix" all the issues you see and completely rewrite the script. Should you rewrite or should you follow Kaizen to make it 1% better?
type: talk
expected_length: 30min
intended_audience: All
speakers: Brandon Williams
---

## Talk Description

I have been a part of teams where "scripts", particularly build and deploy scripts, lack automated tests. The question of how to improve the code arises and one answer usually ends up being a rewrite. I have seen several rewrites and during these rewrites:

1. requirements/existing features are missed
2. time invested is more than time estimated
3. new bugs are introduced

The rewrites have been proposed because the code is perceived to be too big/complex to get tests around it or because it's complex beyond further maintenance. So if rewrites are not the answer, what can we do?

Kaizen is the philosophy of continuous improvement of working practices. You decide to just make the script 1% better today instead of doing the rewrite. We will explore two options for doing so, both of which involve automated testing. We can write the first characterization test for the script or specifically unit test the new feature. We'll talk about both approaches and why you might choose one over the other. In time, this script may undergo the "rewrite" that you initially dreamed of but you went about it in a much safer way.
