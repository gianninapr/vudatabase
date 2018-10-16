A Database and UI for Villanova University's Eclipsing Binary Card Catalogue
============================================================================

This project uses the Django Framework to create a database for the eclipsing
binary card catalogue stored in the Department of Astrophysics and Planetary
Sciences at Villanova University. This project also includes a data entry
interface through Django's Admin website functionality, and a dynamic HTML
online catalog tied to the database. Images of the database schema and the
resulting UIs can be found at the bottom of this text.

Most scripts contain sufficient amount of comments, but more documentation will
be added as a per-file basis soon.

Catalogue Background and the 'Why' of this Project:
===================================================

"The Eclipsing Binary Card Catalog started at Princeton in the 1930s during the
time of Henry Norris Russell. But moved to the Astronomy Dept at the University
of Pennsylvania after World War II, maybe late 1940s. Univ. of Pennsylvania
was one of the world centers of eclipsing binary research then. Dr. F.B Wood
was in charge the Card Catalog while he was at Penn, followed by Robert Koch.
When F.B. Wood went to Univ. of Florida in 1968, the Catalog moved there. After
Dr. Wood's death, the Univ. of Florida (Gainesville) offered the Card
Catalog to Villanova during the 1990s and we accepted it. With internet and
the development of the web the Card Catalog stopped being updated with
new information - probably during the early 1990s. But the Card Catalog remains
valuable source on eclipsing binaries and historical data."

The archive is not only historically significant, but also contains information
that might contribute to studies in EBs such as: notable variations in RA and
DEC, qualitative comments, and quantitative observations that can be traced
back as far as the 1930’s. As well as maintaining a record of references that
were not found on the internet in order to make online journal query programs
such as ADS aware of the absence of these references

Things to Work On
=================

This was my first coding project therefore there are a few things that need to
be cleaned in terms of static directories, and syntax needs to be normalized,
which will also be done as soon as possible. Things that need to be done:

* The data-entry process needs to begin so that we can see where the database
  needs tweaking

* CSS should be added to the dynamic HTML template to refine the presentation
  of the output catalog.


Example Images and Database Schema
==================================


![Schema](../assets/schema.png?raw=true)


![UI](../assets/UI.png?raw=true)


![Catalog](../assets/catalog.png?raw=true)


![Demo Animation](../assets/card.png?raw=true)
