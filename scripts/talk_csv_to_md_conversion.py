#!/usr/bin/env python3

"""Converts Talk selection CSV file from papercall to jekyll markdown files"""
import csv
import string

IN_FILE_PATH='/Users/jstephens/Downloads/pytn-2019.csv'
OUT_FILE_PATH='/Users/jstephens/development/personal/pytn-2019/_talks'

def get_talk_type(record):
    """Returns the type of submission for a given record"""
    return 'tutorial' if 'Tutorial' in record['talk_format'] else 'talk'

def create_markdown_file_name(record):
    """Returns a filename for a record"""
    return ''.join([x for x in row.get('title', '') if x not in string.punctuation]).replace(' ', '-')


def talk_markdown_file(record, permalink, talk_type):
    """Creates a markdown for a talk"""
    talk_length = record.get('talk_format').replace('Talk', '').replace('Tutorial', '')
    talk_length = talk_length.replace('(', '').replace(')', '').replace(' ', '')

    data_dict = {
        'title': record.get('title', ''),
        'permalink': permalink,
        'bio': record.get('bio', ''),
        'abstract': record.get('abstract', ''),
        'talk_type': talk_type,
        'talk_length': talk_length,
        'audience_level': record.get('audience_level', 'all'),
        'name': record.get('name', ''),
        'description': record.get('description', '').replace('## Talk Description', '')
    }

    talk_format = """---
title: {title}
layout: talk
body_class: talk
permalink: talks/{permalink}
about: {bio}
abstract: {abstract}
type: {talk_type}
expected_length: {talk_length}
intended_audience: {audience_level}
speakers: {name}
---

## Talk Description
{description}
    """
    return talk_format.format(**data_dict)

with open(IN_FILE_PATH, 'r') as infile:
    entities = csv.DictReader(infile)

    for row in entities:
        if row['state'] == 'accepted':
            out_file = create_markdown_file_name(row).lower()
            result = talk_markdown_file(row, out_file, get_talk_type(row))

            with open(OUT_FILE_PATH + '/' + out_file + '.md', 'w') as markdown_file:
                markdown_file.write(result)