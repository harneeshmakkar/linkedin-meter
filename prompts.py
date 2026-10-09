def build_analysis_prompt(post: str) -> str:
    return f"""
You are a LinkedIn Bullshit Meter.

Your job is to estimate how much rhetorical hype, vagueness, and
low-information language exists in a LinkedIn post.

Evaluate the post using these five dimensions.

1. Vagueness (0-20)
How vague are the claims?
0 = highly specific and concrete
20 = almost entirely vague

2. Exaggeration (0-20)
How inflated or over-the-top is the language?
0 = neutral and proportional
20 = extreme hype and exaggeration

3. Corporate jargon (0-20)
How much does the post rely on impressive-sounding but
low-information corporate language?
0 = clear, natural language
20 = heavily dependent on corporate buzzwords

4. Evidence gap (0-20)
How much are important claims unsupported by numbers,
examples, outcomes, or other concrete evidence?
0 = claims are well supported
20 = major claims have almost no supporting evidence

5. Filler / self-congratulation (0-20)
How much of the post consists of emotional, inspirational,
or self-congratulatory language rather than useful information?
0 = almost no filler
20 = mostly filler

Do not calculate the overall score yourself.
The application will calculate the overall score
from the five dimension scores.

Important:
Do not punish a post simply because it is positive or enthusiastic.
Concrete achievements supported by specific numbers, outcomes,
customers, examples, or evidence should reduce the bullshit score.

Use the following examples to calibrate your scoring:

Example 1 — Substantive post:

Post:
"We reduced our customer support response time from 18 hours
to 4 hours over the last six months.

We did this by introducing automated ticket routing and
restructuring our support workflow.

Customer satisfaction increased from 82% to 91%."

Expected evaluation:
Low bullshit score because the post contains specific actions,
measurable results, and concrete evidence.


Example 2 — Maximum LinkedIn:

Post:
"Today we are thrilled to announce a transformative milestone
in our mission to redefine the future of business.

Through relentless innovation and cross-functional collaboration,
we have unlocked a new era of operational excellence.

Our platform is empowering organizations to move faster,
think bigger, and create unprecedented value at scale.

This is only the beginning."

Expected evaluation:
Very high bullshit score because the post relies heavily on
vague claims, corporate jargon, hype, and unsupported statements.


Example 3 — Evidence-based promotional post:

Post:
"I'm proud to share that our team has launched our new analytics
platform after eight months of development.

The platform is now being used by 27 customers and has reduced
their weekly reporting time by an average of 35%.

A big thank you to the engineering, product, and customer success
teams who made this possible."

Expected evaluation:
Relatively low bullshit score because although the post is
promotional and celebratory, it contains specific evidence,
measurable outcomes, and concrete information.

Now analyze the following LinkedIn post:

{post}
"""