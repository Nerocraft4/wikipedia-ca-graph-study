# Catalan Wikipedia (Viquipèdia) Graph Study
Study of the catalan wikipedia's article distribution.

## First Steps:
Download `cawiki-20240501-pagelinks.sql.gz` (Wiki page-to-page link records.) and `cawiki-20240501-page.sql` from [cawiki's 2024-05-01 dump](https://dumps.wikimedia.org/cawiki/20240501/). (Note: 240701's dump is seemingly broken. This took a painstakingly great amount of time to realise. Don't use it (unless it's explicitly fixed)) 
Decompress `pagelinks`. With a bit of Python magic and patience, skip over creating a database and everything, and just parse the file into a DataFrame (again, some reformatting was needed). For safekeeping, I saved the csv split into 7 different files, each one taking around 360Mb, except the last one, which takes a bit less. I was careful to not add indexes and headers, since --specially indexes-- take up a lot of memory and are useless.
Current state: filtered main table from 65M links to around 900k. I'll save it as a CSV, but tomorrow. Now it keeps crashing, I've probably done enough to my computer for today.

