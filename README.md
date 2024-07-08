# Catalan Wikipedia (Viquipèdia) Graph Study
Study of the catalan wikipedia's article distribution.

## First Steps:
Download `cawiki-20240701-pagelinks.sql.gz` (Wiki page-to-page link records.) and `cawiki-20240701-all-titles-in-ns0` (all titles, not sure if needed) from [cawiki's 2024-07-01 dump](https://dumps.wikimedia.org/cawiki/20240701/). 
Set up a new MariaDB server (since dump was made with Maria, I thought this would be a frictionless approach) and load into it the sql file using HeidiSQL. sql file took around 3 hours and a half to load and took around 8GB of my RAM.
