title: The Graphics Pipeline

## More fun than it sounds...

I wanted to do something constructive with my PEY term, so I decided to
learn what I could about 3D graphics.  When I say "learn" I don't mean any
particular library or product like OpenGL or DirectX or POV-Ray (although I
did have some fun with POV-Ray).  I decided to learn about the math involved
so I could write my own 3D library.  I was taking home a paycheck and I was
feeling brave.

So here we are. The library's name is GP, for Graphics Pipeline (I never
said I was creative). It is low level polygon renderer with a design similar
to OpenGL, although not identical (OpenGL, for instance does not allow
oblique projections, while this API does). I think the shading might be a
bit off but...whatever. It was all in good fun and maybe I'll fix it
someday.

## Gallery

### Sine wave carpet
<table style="border: none">
<tr>
<td style="border: none"><a href="/static/gp/carpet10.jpg"><img src="/static/gp/carpet10_thumb.jpg"/></a></td>
<td style="border: none"><a href="/static/gp/carpet20.jpg"><img src="/static/gp/carpet20_thumb.jpg"/></a></td>
<td style="border: none"><a href="/static/gp/carpet40.jpg"><img src="/static/gp/carpet40_thumb.jpg"/></a></td>
</tr>
<tr>
<td style="border: none">200 triangles</td>
<td style="border: none">800 triangle</td>
<td style="border: none">3200 triangles</td>
</tr>
</table>

### Simple water wave
<table style="border: none">
<tr>
<td style="border: none"><a href="/static/gp/yelcos.jpg"><img src="/static/gp/yelcos_thumb.jpg"/></a></td>
<td style="border: none"><a href="/static/gp/redcos.jpg"><img src="/static/gp/redcos_thumb.jpg"/></a></td>
<td style="border: none"><a href="/static/gp/bgcos.jpg"><img src="/static/gp/bgcos_thumb.jpg"/></a></td>
</tr>
<tr>
<td style="border: none">Yellow</td>
<td style="border: none">Red</td>
<td style="border: none">Blue solid and green wire</td>
</tr>
</table>

### Mobius strip

<table style="border: none">
<tr>
<td style="border: none"><a href="/static/gp/bluemobius.jpg"><img src="/static/gp/bluemobius_thumb.jpg"/></a></td>
<td style="border: none"><a href="/static/gp/yellowmobius.jpg"><img src="/static/gp/yellowmobius_thumb.jpg"/></a></td>
<td style="border: none"><a href="/static/gp/colormobius.jpg"><img src="/static/gp/colormobius_thumb.jpg"/></a></td>
</tr>
<tr>
<td style="border: none">Blue</td>
<td style="border: none">Yellow</td>
<td style="border: none">Psychedelic</td>
</tr>
</table>

### Source Code
* [gpbase.h](/static/gp/src/gpbase.h)
* [gpbase.c](/static/gp/src/gpbase.c)
* [algebra.h](/static/gp/src/algebra.h)
* [algebra.c](/static/gp/src/algebra.c)
* [clip.h](/static/gp/src/clip.h)
* [clip.c](/static/gp/src/clip.c)
* [light.h](/static/gp/src/light.h)
* [light.c](/static/gp/src/light.c)
* [pipe.h](/static/gp/src/pipe.h)
* [pipe.c](/static/gp/src/pipe.c)
* [raster.h](/static/gp/src/raster.h)
* [raster.c](/static/gp/src/raster.c)
* [view.h](/static/gp/src/view.h)
* [view.c](/static/gp/src/view.c)
