#!/usr/bin/env python3

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import List

import click

import easy_scraper


@dataclass
class Pattern:
    format: str
    fields: List[str]

    @classmethod
    def build(cls, raw_format: str) -> Pattern:
        """Build pattern for easy_scraper

        Examples
        --------
        build("<img src={} />")
        >>> "<img src={{}} /"
        """

        if "{}" in raw_format:
            return Pattern(raw_format.replace("{}", "{{}}"), [""])

        raise NotImplementedError


@click.command()
@click.option("--delimiter", "-d", default="\t")
@click.argument("pattern")
def main(delimiter: str, pattern: str):
    """web-grep

    Read Xml or Html from stdin,
    Write into stdout.
    """
    html = "\n".join(sys.stdin)
    p = Pattern.build(pattern)
    res = easy_scraper.match(html, p.format)
    for item in res:
        values = [item[f] for f in p.fields]
        print(delimiter.join(values))


if __name__ == "__main__":
    main()
