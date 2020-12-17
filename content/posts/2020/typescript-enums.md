title: Enum Musings in TypeScript
date: 2020-11-30 22:21:29 -0500
modified: 2020-11-30 22:21:29 -0500
tags: typescript
blurb: Typescript enums are kind of weird
mp_syndicate_to: twitter_bridgy

I'm a pretty big fan of [TypeScript][1], probably best described as a
statically typed language that transpiles to standard JavaScript.  I've
[written about it][2] before.

People who have worked with me in the past may be surprised at my
admiration, given the rancour I sometimes direct at something like the
[Google Web Toolkit (GWT)][3], a Java-to-JavaScript transpiler, which to the
casual eye seems to be in a similar vein.

The similarities, however, are superficial; TypeScript and GWT are quite
different beasts.  Something like GWT is used in web development in order to
*avoid* writing JavaScript.  TypeScript, on the other hand, is best viewed
as JavaScript extended with an optional static typing system.  The optional
part is key; in theory, any JavaScript program is also a valid TypeScript
program.  In other words, TypeScript doesn't try to hide the fact that it's
merely an enhanced version of JavaScript.

To put it another way, GWT adopts the attitude that JavaScript is
fundamentally broken and should be avoided in shame, while TypeScript adopts
the attitude that JavaScript is elegant and should be used with pride.

Granted, the latter attitude is much easier to adopt with the advent of
[EcmaScript 6 (ES6)][6], the official name of the latest version of
JavaScript.  ES6 fixes most of the shortcomings of previous versions of
JavaScript, many of which are the reasons that GWT became a thing in the
first place.

Because Java and JavaScript are so different, using GWT comes at the expense
of an "impedance mismatch".  Although JavaScript comes with arrays,
dictionaries and something resembling classes, these features are nothing
like the analogous features in Java.  Implementing a Java-to-JavaScript
transpiler like GWT means implementing basic constructs like Java classes
and specific implementations of things like ArrayLists and HashMaps - all in
JavaScript.

You don't have to pull these kinds of shenanigans with a TypeScript
transpiler because Typescript isn't pretending to be anything other than a
somewhat safer version of JavaScript.  TypeScript doesn't provide a
specialized list implementation, for example, because JavaScript already
gives you perfectly good arrays.  TypeScript's class construct maps directly
to ES6's class construct which is, itself, mere syntactic sugar over the
somewhat more cumbersome EcmaScript 5 class construct.

What I'm trying to say is that TypeScript really is just "JavaScript with
types" which is why my hackles go up every time I hear someone describe it
as an attempt to make JavaScript more "Java-like".  This is criminally
misleading, and misses the point entirely.

It also cuts right to the core of why I dislike TypeScript enums.

## TypeScript's Enum Problem

The fundamental design strategy behind TypeScript is to re-use to JavaScript
concepts wherever possible.  Constructs like imports, classes, Arrays, Maps,
Sets will all be perfectly familar to anyone who has used ES6 - because they
are the exact same constructs.

That being said, one construct that might *not* be familiar to JavaScript
developers are [TypeScript enums][4], for the simple reason that they don't
exist in any version of JavaScript.  TypeScript enums are similar in concept
to enums from other languages, but if all you've ever used is JavaScript,
the idea might be foreign.  They provide a convenient, type-safe way to
describe a variable who's value can only be taken from a constrained list of
related values - think of a variable to hold the day of the week, or the
month of the year.

You define an enum in TypeScript like this:

```
enum DayOfWeek {
    Sunday,
    Monday,
    Tuesday,
    Wednesday,
    Thursday,
    Friday,
    Saturday
}
```

This is what's called a *numeric enum*; the values of Sunday through
Saturday are literally represented by the numbers 0 through 6.

An enum definition like the one above can be used as a type, like this:

```
function doSomethingWithDay(day: DayOfWeek) {
   ...
}
```

This is basically saying that the day variable in this function is a number
between 0-6.

And you can access the individual enum values like this:

```
const m = DayOfWeek.Monday;
```

In JavaScript, the type of m would be number.

As I mentioned before, enums are a pure TypeScript construct.  Unlike arrays
and Maps, they don't exist in any version of JavaScript.  In that sense
they're a bit like [TypeScript interfaces][5], constructs which also exist
purely in the TypeScript realm - the difference being that, unlike
interfaces, which get completely compiled away from the final, resulting
JavaScript, enums very much stay behind. And that makes them, in my opinion,
somewhat anathema to the entire idea of TypeScript.  One of the main perks
of TypeScript development is that it is not entirely disimilar to JavaScript
development, and the use of TypeScript enums definitely runs counter to that
advantage.

## Enums Are Weird

So what's the problem, exactly?  Why are TypeScript enums weird?  I mean,
it's kind of hard to imagine that JavaScript developers are unfamiliar with
the idea of a variable that can only hold one of a list of values.

The issue is that a JavaScript developer would probably just use a simple
string or number for this purpose - not a full blown object





[1]: https://www.typescriptlang.org/
[2]: /2018/01/18/static-typing
[3]: http://www.gwtproject.org/
[4]: https://www.typescriptlang.org/docs/handbook/enums.html
[5]: https://www.typescriptlang.org/docs/handbook/interfaces.html
[6]: https://en.wikipedia.org/wiki/ECMAScript#6th_Edition_%E2%80%93_ECMAScript_2015
