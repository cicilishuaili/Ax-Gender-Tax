# Ax the Gender Tax

## Motivation
Language is powerful, and not only in the ways we use it for communication and expression. Studies have shown that the medium with which we share our thoughts, ideas, beliefs in, inadvertently influences and shapes us. From [national identity](https://www.npr.org/sections/parallels/2017/09/29/554327011/for-catalonias-separatists-language-is-the-key-to-identity), to [our spending habits](http://www.anderson.ucla.edu/faculty/keith.chen/papers/LanguageWorkingPaper.pdf), to perceptions of [time](http://journals.sagepub.com/doi/abs/10.1177/0956797610386621), [agency](https://www.frontiersin.org/articles/10.3389/fpsyg.2010.00162/full), and [art](https://www.frontiersin.org/articles/10.3389/fpsyg.2010.00244/full), the features of language matter more than you may think. As a speaker of two languages without grammatical gender, I found it especially interesting the way that can affect [how inanimate objects are described](https://web.stanford.edu/class/linguist156/Boroditsky_ea_2003.pdf), showing just how certain ideas, stereotype or not, can be ingrained and propagated via language.

The pervasiveness of the feminine connotation and the ability for that to transfer to objects is also met from the other side, as "Shrink it and pink it" has been the marketing mantra that goes into product design for women. Recalling the infamous Bic's "for her" pens, the assumption has always been that ladies are obvious dainty and love all shades of magenta. This has also translated into economic implications, where gender-specific item pricing implies a surcharge of [7 percent for women](https://www1.nyc.gov/site/dca/partners/gender-pricing-study.page). Beyond the not easily dismissed financial implications, I became curious; how are these male-female versions of products being described? Have we evolved much from the era of pink and shrink? Are we still, consciously through marketing, or unconsciously through masculine and feminine adjectives, transferring something in those words?

Fascinated by the ways description and perceptions are embedded in our lives, I aim to probe at the intersection of objects, language, and gender.

## Story (optional reading)
[Read about it here](https://github.com/cicilishuaili/Pink-and-Shrink/blob/master/Optional_Origin_Story.md)

## Problem
How do product descriptions vary across the gender aisle? Are they a reflection of specialized functional design or an appeal to more stereotypical perception? Can we predict the "gender" of an item, solely based on its descriptions?

## Data Source
There is no online market more ubiquitous than Amazon. The product descriptions can be available via their [Amazon Product Advertisement API](https://docs.aws.amazon.com/AWSECommerceService/latest/DG/Welcome.html), requiring an associates account which unfortunately became restricted during the course of this project. Amazon offers a wealth of information on how to navigate their API (including their own [scratchpad](https://webservices.amazon.com/scratchpad/index.html) to tryout playing with it). Although it is a bit restrictive in the amount of information that is accessible (e.g. they only allow a search to fetch 10 pages of results now instead of the old 100 back in the days), it will do as initial exploration that can still reveal useful insights.

I was a relatively new to interacting with APIs, I looked for and used one of the more [well documented wrapper for Python](https://python-amazon-product-api.readthedocs.io/en/latest/index.html). It performs adequately and served its purpose well for Amazon API. But the big thing I realized a bit late is that its compatibility is limited to Python 2.7 so I may be motivated to switch to one that also supports Python 3. There is another [perhaps more flexible wrapper](https://github.com/lionheart/bottlenose), to experiment with in the future should I want to do something like play with the parsing option. I don't foresee the need, unless one feels particularly ambitious, for scraping, especially since amazon's robots.txt seem to be quite restrictive.

The sections of the API output that I will be using as product description is technically called "Editorial Review". It is the section you see often to the right of the picture, traditionally under the prices. They vary from nonexistent to brief or generic to detailed.

## Analysis
The plan of approach:

1. Find product categories that are, or should be, essentially functional equivalents in use, regardless of gender.
2. Obtain product descriptions for items that are for women vs. men.
3. Use NLP and other techniques to determine the key differences between the two categories of description. Naive bayes chosen given its simplicity and ease of interpretation.
4.
