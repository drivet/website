title: Enum Musings in TypeScript
date: 2020-11-30 22:21:29 -0500
modified: 2020-11-30 22:21:29 -0500
tags: typescript
blurb: Typescript enums are kind of weird
mp_syndicate_to: twitter_bridgy

At one time in my career, I developed web applications using the Google Web
Toolkit (GWT), a Java to JavaScript transpiler, and I learned to dislike the
experience thoroughly.

GWT was truly a product of its time, and that time viewed JavaScript as a
necessary evil at best.  We're talking about the years roughly before 2010,
when JavaScript was mostly considered a "toy" language, replete with warts
and inconsistencies, and relegated to the implementation of cute web browser
effects.  Anything which enabled you to avoid writing it was considered a
boon.  This was roughly the same era that produced CoffeeScript, another
famous attempt to avoid writing JavaScript at all costs.

As someone who used to hate JavaScript as much as the next guy, I understand
the rationale, but JavaScript-transpiled languages come with a batch of
problems that are sometimes not entirely obvious to someone blinded by an
agenda.  One of them is impedance mismatch, so to speak.  More often than
not, the source language contains features which simply don't translate well
to JavaScript.  GWT was notorious for this.  It was a bit misleading, in
fact, to call it a Java to JavaScript transpiler at all; more accurately, it
transpiled a *subset* of Java into JavaScript.  The entire Java threading
package, for example, was off limits as such a thing didn't make any sense
in the context of a web browser.  A related issue is the availability of
supporting libraries.  The GWT team provided JavaScript versions of most of
the standard Java libraries as of version 1.3, but they started to run out
of steam after version 1.5, and it's not as if you can just use any
third-party library to compensate. Most libraries are provided as jar files,
which won't work in this context; full source code is needed to convert it
to JavaScript, and there is no guarantee that the writer of the library
restricted themselves to the supported subset of the language.

The impedance mismatch I mentioned before surfaces in other ways as well.
Although arrays and object and classes exist (to some extent) in JavaScript,
they are not directly related to the Lists and Classes that one find in
Java.  Certainly

One aspect of using these languages that usually wasn't considered a problem
but which sometimes made me vaguely uncomfortable was the quality of
JavaScript produced.  It was generally pretty unreadable, mostly because it
wasn't meant to be read.  In these kinds of applications, JavaScript is
often treated as the "assembly language of the web" and isn't manipulated
directly.

In any case, JavaScript has evolved significantly since those early days and
EcmaScript 6, the latest version, fixes a lot of the problems that made
people want to use different languages.  The rationale for using these kinds
of transpiled languages has mostly disappeared.

## Why TypeScript is Different

I'm a fan of TypeScript, a typed programming language which transpiles to
standard JavaScript.

One exception to this general trend is Typescript.  Typescript is different.

Typescript is different because it tries very hard to be compatible with
standard JavaScript.  While Typescript adds some welcome features to the
language, such as type checking, these features are entirely optional. In
theory, a pure JavaScript program is parseable by the Typescript compiler.
Typescript embodies the idea that Javascript is actually pretty good on its
own, and only needs a few extra features to make it even better.

