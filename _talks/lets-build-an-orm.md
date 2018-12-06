---
title: Let's build an ORM!
layout: talk
body_class: talk
permalink: talks/lets-build-an-orm
about: I've been a Python developer for 10 years and have given several presentations on writing better Python code. I enjoy teaching others the things I've learned over the course of my career.
abstract: Applications rely on data, and relational databases are a convenient way to organize structured information. Object-relational mappers like SQLAlchemy and Django's ORM are complex libraries, but they aren't black magic. De-mystify some of the magic as we build a (basic) ORM in under an hour.
type: talk
expected_length: 30min
intended_audience: Intermediate
speakers: Greg Back
---

## Talk Description

We'll start with some background on relational database terminology, including CRUD, ACID, normalization, and the Active Record pattern. Next, we'll build a basic ORM that allows creating simple tables and inserting, querying, and deleting records. Finally, we'll talk about some of the challenges of building a production-grade ORM, including caching, transactions, supporting multiple dialects, and we'll briefly discuss security implications of ORMs, including SQL injection. You will leave with a greater appreciation for the inner workings of the ORMs you use on a daily basis, while understanding the challenges that go into building one.
