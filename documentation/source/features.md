---
title: East Syriac Marcus New - Font Features
fontversion: 1.106
---

East Syriac Marcus New is an OpenType-enabled font family that supports the East Syriac style of the Syriac script. It includes a number of optional features that may be useful or required for particular uses or languages. This document lists all the available features.

These OpenType features are primarily specified using four-letter tags (e.g. 'cv38'). For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features). Some of the ligatures are also available if an application supports "Discretionary Ligatures".

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use East Syriac Marcus New as a web font see [East Syriac Marcus New Webfont Example](../web/EastSyriacMarcusNew-webfont-example.html). For detailed information see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Stylistic sets

_Some of the character variants below are also implemented as Stylistic sets._

### Kaph Mim Nun alternates

<span class='affects'>Affects: U+071F U+0721 U+0722  (this feature is primarily for outlines and only affects the isolate form)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='esmn-R normal'>&#x071F; &#x0721; &#x0722;</span> | `ss01=0`
Alternate  | <span class='esmn-R normal' style='font-feature-settings: "ss01" 1'>&#x071F; &#x0721; &#x0722;</span> | `ss01=1`

## Character variants

### Digit alternates

<span class='affects'>Affects: U+0030..U+0039  (this feature is provided for those who prefer serif digits with Syriac script)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='esmn-R normal'>0123456789</span> | `cv02=0`
Serif  | <span class='esmn-R normal' style='font-feature-settings: "cv02" 1'>0123456789</span> | `cv02=1`

### Kaph alternate

<span class='affects'>Affects: U+071F (this feature is primarily for outlines and only affects the isolate form)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='esmn-R normal'>&#x071F;</span> | `cv15=0`
Historic  | <span class='esmn-R normal' style='font-feature-settings: "cv15" 1'>&#x071F;</span> | `cv15=1`

### Mim alternate

<span class='affects'>Affects: U+0721 (this feature is primarily for outlines and only affects the isolate form)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='esmn-R normal'>&#x0721;</span> | `cv17=0`
Historic  | <span class='esmn-R normal' style='font-feature-settings: "cv17" 1'>&#x0721;</span> | `cv17=1`

### Nun alternate

<span class='affects'>Affects: U+0722 (this feature is primarily for outlines and only affects the isolate form)</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='esmn-R normal'>&#x0722;</span> | `cv18=0`
Historic  | <span class='esmn-R normal' style='font-feature-settings: "cv18" 1'>&#x0722;</span> | `cv18=1`

### He Yudh ligature

This ligature is also available as a "Discretionary Ligature".

<span class='affects'>Affects: U+0717 U+071D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='esmn-R normal'>&#x0717;&#x071D; &#x200D;&#x0717;&#x071D;</span> | `cv38=0`
Ligature | <span class='esmn-R normal' style='font-feature-settings: "cv38" 1'>&#x0717;&#x071D; &#x200D;&#x0717;&#x071D;</span> | `cv38=1` or `ss16`

### Sadhe Nun ligature

This ligature is also available as a "Discretionary Ligature".

<span class='affects'>Affects: U+0728 U+0722</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='esmn-R normal'>&#x0728;&#x0722; &#x200D;&#x0728;&#x0722;</span> | `cv55=0`
Ligature | <span class='esmn-R normal' style='font-feature-settings: "cv55" 1'>&#x0728;&#x0722; &#x200D;&#x0728;&#x0722;</span> | `cv55=1` or `ss17`

### Taw Alaph ligature

The first ligature is also available as a "Discretionary Ligature".

<span class='affects'>Affects: U+072C U+0710</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='esmn-R normal'>&#x072C;&#x0710; &#x200D;&#x072C;&#x0710;</span> | `cv59=0`
Triangle    | <span class='esmn-R normal' style='font-feature-settings: "cv59" 1'>&#x072C;&#x0710; &#x200D;&#x072C;&#x0710;</span> | `cv59=1` or `ss18`
Intertwined | <span class='esmn-R normal' style='font-feature-settings: "cv59" 2'>&#x072C;&#x0710; &#x200D;&#x072C;&#x0710;</span> | `cv59=2` or `ss19`

### Taw Yudh ligature

This ligature is also available as a "Discretionary Ligature".

<span class='affects'>Affects: U+072C U+071D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span dir="rtl" class='esmn-R normal'>&#x072C;&#x071D; &#x200D;&#x072C;&#x071D;</span> | `cv60=0`
Ligature | <span dir="rtl" class='esmn-R normal' style='font-feature-settings: "cv60" 1'>&#x072C;&#x071D; &#x200D;&#x072C;&#x071D;</span> | `cv60=1` or `ss20`

<!-- PRODUCT SITE ONLY
[font id='esmn' face='EastSyriacMarcusNew-Regular' size='150%' rtl=1]
-->
