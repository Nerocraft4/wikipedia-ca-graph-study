# Catalan Wikipedia (Viquipèdia) Graph Study: Discontinued
Study of the catalan wikipedia's article distribution.

## A frustrating --and longer than it should-- story.
I started this project a couple of months ago, and have given it several tries. Still, I have been unable to obtain results. These are the reasons that have made it tedious and horribly hard to go on, and that have made me pass on the project:
 - Hard to use table dumps and data format. Why ONLY SQL? Why not give other options to the users?
 - Badly described tables and columns, with information lacking in every single step or situation.
 - Broken tables, incorrect formats and simply corrupted/wrong data: the data from some of the dumps was just wrong, making me lose tens of hours until I realised.
 - No references, forums, or clear ways in which to ask for help. Yes, even if I was able to open a ticket, I got no feedback and felt absolutely alone while working on this.

I probably have spent more than 30 or 40 hours on just THE SETUP of the project, achieving no results. It's time to move on and leave it behind, sadly. It was a nice idea, but until the tables and the info around them are properly maintained by the engineers behind the dumps, they are mostly unusable.

## ~~First Steps:~~
~~Download `cawiki-20240501-pagelinks.sql.gz` (Wiki page-to-page link records.) and `cawiki-20240501-page.sql` from [cawiki's 2024-05-01 dump](https://dumps.wikimedia.org/cawiki/20240501/). (Note: 240701's dump is seemingly broken. This took a painstakingly great amount of time to realise. Don't use it (unless it's explicitly fixed)) 
Decompress `pagelinks`. With a bit of Python magic and patience, skip over creating a database and everything, and just parse the file into a DataFrame (again, some reformatting was needed). For safekeeping, I saved the csv split into 7 different files, each one taking around 360Mb, except the last one, which takes a bit less. I was careful to not add indexes and headers, since --specially indexes-- take up a lot of memory and are useless.
Current state: filtered main table from 65M links to around 900k. I'll save it as a CSV, but tomorrow. Now it keeps crashing, I've probably done enough to my computer for today.~~

