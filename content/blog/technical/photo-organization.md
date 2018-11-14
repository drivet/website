title: How I Organize my Photos
date: 2018-11-09 21:16:02
modified: 2018-11-09 21:16:02
status: draft

I have a large collection of digital photos, dating back over 15 years.  An
impressively small fraction of them are any good, but that's a different
conversation, probably revolving around my digital hoarding habits.

Anyway such a large collection deserves a particular method of organization.
Or maybe it doesn't.  Anyway, I have one! I thought I'd share in case anyone
finds it useful (including a future version of myself, my mind being a sieve
and all).

The procedure I came up with is strongly influenced by several personal
idiosyncrasies.

 * I have a strict rule about keeping my original photos intact and under my
   control.  The masters are never be stored anywhere but on my hard drive
   (which is backed up every night).
   
 * The process of selecting and then touching up the photos that make it
   into the albums is time consuming, and I don't want that fruits of that
   labour to be reside in an external service over which I have no control.
   So while I don't mind showing or exporting my albums on Facebook or
   Instagram, those services do not _define_ my albums.

 * I don't want to rely too much on any particular desktop application.  If
   I ever decide to switch tools, I don't want that process to be too
   arduous.
   
 * I'm a Linux user, and I tend to prefer command line tools, though when
   you're dealing with photos it's often counterproductive to take this
   attitude to extremes.

All of my photos, every single one, is stored and organized under one folder
on my hard drive.  When I have new photos that I want to bring into the
fold, the first step is to download the contents of my camera onto my hard
disk.  Sometimes the camera is my phone and sometimes it's a real camera.
In any case, I don't try to be clever at this point; I just do a brainless
dump of the camera contents into a temporary folder.

To make things easier for the next step, this temporary folder is usually
tucked under the folder where I keep all my organized photos.

Since I tend not to delete the contents of my camera when I do this, I'll
often end up with duplicates at this point - some (maybe even most) of the
photos I just downloaded will have already been organized into their final
destinations.  The next step, therefore, is to remove duplicates photos.
For this purpose I use a command line tool called [fdupes][1], readily
available in my Linux Mint distribution.  One line will do it:

`fdupes -rdN organized_image_folder/`

This will remove all the duplicates files from the folder you passed - which
should only come from the folder you dumped.  It doesn't matter which file
gets deleted, since the next step will smooth that over.

The next step is to move your new photos into your organized image folder.
For this purpose I use a command line tool called [sortphotos][2].  From the
README file:

> SortPhotos is a Python script that organizes photos into folders by date
> and/or time (year, year/month, year/month/day, or other custom formats).

The tool uses photo EXIF data to move your photos into a folder hierarchy
that you define.  I just use the default folder structure, which is just
year and month based.  An example would be "2018/10-Oct".

If there is an obvious way to sub-categorize the photos within the folder
structure, I'll do that as well.  So, for example, if I went on a trip some
month, or it was someone's birthday, I'll tuck those photos under a
sub-folder named for the event.  So you'll occasionally see a folder
hierarchy that looks like year/month/category (for example,
"2018/10-Oct/Chicago").

## Selecting Photos for Sharing

As I mentioned before, because I take a lot of mediocre photos, only a small
fraction are suitable for sharing.  Even then, I often find myself editing
the selected photos, rotating and cropping and sharpening to compensate for
my lack of photography skills.

The process of curating, polishing and sharing my photos can be time
consuming and I don't want the fruits of that labour to reside solely in the
software that I choose to use.  I don't want my "albums", for example, to
exist only as bits and bytes on Facebook's servers - or any other server,
even if it's under my control.


When choosing a piece of software for this purpose, I'm influenced by a few
factors.

My photo sharing software of choice is [piwigo][3], partly because I have a
bias towards self-hosted software, but also because piwigo lets people
download the entire, unmodified image if they want.

I use an open source piece of software called [digikam][4] for this process.

Once I've done the work of choosing and editing the images for my albums, I
don't want to repeat the work.

[1]: https://linux.die.net/man/1/fdupes
[2]: https://github.com/andrewning/sortphotos
[3]: https://piwigo.org/
[4]: https://www.digikam.org/
