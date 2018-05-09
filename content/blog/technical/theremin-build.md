title: On Finding an Excuse to Buy an Arduino or: How I Finally Got Myself a Theremin
date: 2018-03-22 10:10:44
modified: 2018-03-22 10:10:44
tags: theremin,arduino
status: draft

In my [last blog entry][3], I talked about theremins.  I've known about them
for a while, and I've always found them fascinating, but I've never actually
taken the plunge and bought one, despite being being tempted on many
occasions (they're not that expensive).

At the same time, I've known about [Arduinos][4] for a long time, and I've
always wanted an excuse to buy one, but I've never actually taken the plunge
and bought one.  As I'm fond of saying, an Arduino is a solution in search
of a problem, and I just never found the right problem for one.

That is, until I found this website:

[http://www.gaudi.ch/OpenTheremin/][5]

A chance to build a theremin out of an Arduino?  How could I pass this up?
I couldn't, that's how.

You have two choices if you want to build an Open Theremin.  You can [buy
the kit][8] or, if you're feeling brave, you can study the [schematics][7]
and build it from scratch.

I myself had two important but conflicting goals that I wanted to accomplish
with this project:

1. I wanted a working theremin
1. I wanted to deepen my knowledge of electronics

I stood a much better chance of accomplishing (1) if I bought the kit.  I
stood a much better chance of accomplishing (2) if I built one from scratch.
I eventually decided to try for both; I bought the kit and started the
process of buying the component parts separately.  My success on that score
will be detailed in subsequent blog entries.

## Building the Theremin

The kit basically consists of the board and the control knobs (along with a
couple of LEDs, and the antennae connectors).  The electronics are all
pretty much pre-soldered onto the board; the knobs and LEDs, on the other
hand, are not.  The bare board looks like this:


<div style="clear: both; text-align: center;"> 
<a href="/blog/technical/open_theremin_board.jpg" 
   style="margin-left: 1em; margin-right: 1em;">
<img border="0" height="266" width="200" 
     src="/blog/technical/open_theremin_board_t.jpg" 
     alt="Open Theremin Board (Front)" />
</a>
<a href="/blog/technical/open_theremin_board_back.jpg" 
   style="margin-left: 1em; margin-right: 1em;">
<img border="0" height="266" width="200" 
     src="/blog/technical/open_theremin_board_back_t.jpg" 
     alt="Open Theremin Board (Back)" />
</a>
</div>

There's not actually that much to put together.  You have to solder on the
Arduino connectors and the knobs, as well as the LEDs, but that's about it.
It all sounds very easy, and it is - if you know how to solder.  I was
reasonably good at it 20 years ago, back in school, but did I still have the
knack?  Was it like riding a bike?

The answer is...no.  It is not like riding a bike. Not even close.
Soldering was much harder than I remembered it.  In addition, the LEDs and
one of the knobs were surface mounted (somewhat gratuitously, I thought,
since it seemed to me that the components could just as easily have been
soldered "through-hole"), which just added a new layer of difficulty.  In my
opinion, I ended up doing a not-horrible job, but it took _way_ longer than
it should have.  The soldered result looks like this:

<div style="clear: both; text-align: center;"> 
<a href="/blog/technical/open_theremin_soldered.jpg" 
   style="margin-left: 1em; margin-right: 1em;">
<img border="0" height="200" width="266" 
     src="/blog/technical/open_theremin_soldered_t.jpg" 
     alt="Open Theremin Board (Soldered)" />
</a>
</div>

I'm a little disappointed at the "blobby" soldering job I did on the LEDs
and Function switch, but on the whole I don't think it's that bad.

The kit doesn't actually come with the antennae - only the connectors which,
thankfully, are merely screwed on, not soldered (using the pads on the upper
left and right sides). The web site does some handwaving about this,
claiming that the required 4 mm alumunium tubes are difficult to ship, and
then goes on to say that they should be widely available at any hardware
store.  This is simply untrue, at least in Montreal, where I live; I
couldn't find tubes of the right size anywhere.  I eventually had to order
them from Ebay.

The website also does some handwaving on what exactly you're supposed to do
with the tubes. It claims that "you can easily bend antennas from aluminium
tubes of 6 mm diameter by hand to the desired shape" which isn't _entirely_
untrue; I had to bend mine around a hard plastic tube about 10 cm in
diameter.  I've heard that wine bottles also work well.

Anyway, you put it all together, add an Arduino, connect the resulting
monstrosity to a pair of speakers and voila!  You have yourself a working
theremin.  The final result look like this:

<div style="clear: both; text-align: center;"> 
<a href="/blog/technical/complete_theremin.jpg" 
   style="margin-left: 1em; margin-right: 1em;">
<img border="0" height="266" width="200" 
     src="/blog/technical/complete_theremin_t.jpg" 
     alt="Complete Open Theremin Board" />
</a>
</div>

This particular theremin is sitting on a camera tripod, which is itself
seated on a stool.  The speakers were the cheapest I could find.

## Grounding the Theremin

I made it sound like all you had to do was plug it in, connect up some
speakers and start playing but sadly it's not quite that simple.

For one thing, proper grounding is cruicial.  Given that the player is
actually part of the circuit (forming one half of a capacitor, the other
half being the antennae), the instrument simply won't unless both the player
and the instrument are conected to ground.  Luckily, the board comes with a
grounding pad, which I connected to a makeshift copper wire bracelet via
alligator clips:

<div style="clear: both; text-align: center;"> 
<a href="/blog/technical/grounding_bracelet.jpg" 
   style="margin-left: 1em; margin-right: 1em;">
<img border="0" height="200" width="266" 
     src="/blog/technical/grounding_bracelet_t.jpg" 
     alt="Complete Open Theremin Board" />
</a>
</div>


Note that, in theory, you can also use a properly grounded power plug, but
either my house isn't properly grounded (a distinct possibility) or the
carpet I play on is a better insulator than I thought, because using such a
plug was ineffective.  Manual grounding via the pad was the only thing I
could get to work.

## Calibrating the Theremin

Once the instrument is grounded, you have to _calibrate_ it.  The first step
in this process is to position yourself roughly 1.5 to 2 feet away from the
theremin.

Any theremin that's more than just a toy (like the Open Theremin) comes with
a pitch knob that allows you to adjust the length of the playable field.
Once you're seated comfortably, the idea is to use this knob to calibrate
the field so that the lowest (silent) note is somewhere in the middle of
your torso.

After that comes the fine tuning.  How you do this depends on how you play.
Thereminist [Carolina Eyck][9], for example, has developed a technique
involving 8 finger positions so that she doesn't have to move her hand when
she plays.  Tuning the instrument in this case involves the following rough
steps:

1. You make finger position 1 and you find the C note in your playable field
   (in her videos, Eyck appears to have perfect pitch but I needed to
   download a Note Recognizer program on my phone to be able to do this)
2. You then make finger position 8 and adjust the field so that this
   poistion is the next highest C note.

When you're finished, your hand will span an octave, and you can play all
the notes in between by making the appropriate finger positions (much,
_much_ easier said than done).

Eyck has a rather instructive video on the subject:

<div style="clear: both; text-align: center;">
<iframe width="560" height="315"
src="https://www.youtube.com/embed/A48fm1ZEgZU" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

One of the interesting things about the Open Theremin project is that it's
able to automate the first step in the tuning process - the positioning of
the lowest note near your torso.  The mechanism by which this occurs will be
the subject of another blog entry.

## Playing the Theremin

So, once you've tuned your Open Theremin, what is it like to play?

This is a difficult question to answer.  By all accounts, the Open Theremin
is relatively easy to play, but how easy is that?  Even so called "easy"
theremins are quite difficult, given the nature of the instrument.

One of the issues that plagues theremins is the non-linearity of the playing
field, and a lot of circuitry will often go into mitigating that particular
problem.  The Open Theremin is _exceptionally_ linear, I suspect due to the
fact that it "cheats" by using an Arduino, so I suppose that's one checkmark
in the easy column.

As you might imagine, Carolina Eyck has a video that introduces her playing
technique:

<div style="clear: both; text-align: center;">
<iframe width="560" height="315"
src="https://www.youtube.com/embed/qz-Ijf9JfpI" frameborder="0"
allow="autoplay; encrypted-media" allowfullscreen></iframe>
</div>

The basic upshot is that if you learn how to play the four high notes of an
octave, plus the starting C note, you can play the beginning of "Somewhere
Over The Rainbow".  A concrete goal - I like it.  I'll let you all know how
it goes.

In the meantime, here's a video of me just making random noises:


[3]: /blog/miscellanea/theremin-intro.html

[4]: https://en.wikipedia.org/wiki/Arduino

[5]: http://www.gaudi.ch/OpenTheremin/

[7]: http://www.gaudi.ch/OpenTheremin/index.php?option=com_content&view=article&id=181&Itemid=116

[8]: http://www.gaudi.ch/OpenTheremin/index.php?option=com_content&view=article&id=182&Itemid=117

[9]: http://www.carolinaeyck.com
