"""
b1 = Book(title="Feed", author="Mira Grant", description="The year was 2014. We had cured cancer. We had beaten the common cold. But in doing so we created something new, something terrible that no one could stop.The infection spread, virus blocks taking over bodies and minds with one, unstoppable command: FEED. Now, twenty years after the Rising, bloggers Georgia and Shaun Mason are on the trail of the biggest story of their lives—the dark conspiracy behind the infected.The truth will get out, even if it kills them.", release=2010)
b2 = Book(title="Zone One", author="Colson Whitehead", description="Written by Colson Whitehead. A virus has laid waste to civilization, turning the infected into flesh-eating and mortally contagious zombies. But events have stabilized, and the rebuilding process has begun. Over a three-day span, 'Mark Spitz' and his fellow 'sweepers'—other survivors of the apocalypse—patrol portions of New York City, eliminating zombies as part of a mission to make the city habitable once again. Flashbacks pepper the narrative, explaining how Mark Spitz survived the apocalypse to date and got his nickname along the way.", release=2011)
b3 = Book(title="Undead Girl Gang", author="Lily Anderson", description="Mila Flores and her best friend Riley have always been inseparable. There's not much excitement in their small town of Cross Creek, so Mila and Riley make their own fun, devoting most of their time to Riley's favorite activity: amateur witchcraft. So when Riley and two Fairmont Academy mean girls die under suspicious circumstances, Mila refuses to believe everyone's explanation that her BFF was involved in a suicide pact. Instead, armed with a tube of lip gloss and an ancient grimoire, Mila does the unthinkable to uncover the truth: she brings the girls back to life.Unfortunately, Riley, June, and Dayton have no recollection of their murders, but they do have unfinished business to attend to. Now, with only seven days until the spell wears off and the girls return to their graves, Mila must wrangle the distracted group of undead teens and work fast to discover their murderer...before the killer strikes again.", release=2018)
l1 = List(title="March 2022", reviewer_id=1)
l2 = List(title="My Favorite Games", reviewer_id=1)
l3 = List(title="Watch With George", reviewer_id=1)


r1 = Reviewer(username="alixp")
db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(r1)

"""

"""
{
    title: "Resident Evil",
    description:"Written by Mira Grant. The year was 2014. We had cured cancer. We had beaten the common cold. But in doing so we created something new, something terrible that no one could stop.

    The infection spread, virus blocks taking over bodies and minds with one, unstoppable command: FEED. Now, twenty years after the Rising, bloggers Georgia and Shaun Mason are on the trail of the biggest story of their lives—the dark conspiracy behind the infected.
    
    The truth will get out, even if it kills them.",
    image: "ALT TEXT FOR NOW"
},
{
    title: "Days Gone",
    description:"Written by Mira Grant. The year was 2014. We had cured cancer. We had beaten the common cold. But in doing so we created something new, something terrible that no one could stop.

    The infection spread, virus blocks taking over bodies and minds with one, unstoppable command: FEED. Now, twenty years after the Rising, bloggers Georgia and Shaun Mason are on the trail of the biggest story of their lives—the dark conspiracy behind the infected.
    
    The truth will get out, even if it kills them.",
    image: "ALT TEXT FOR NOW"
},
{
    title: "The Last of Us",
    description:"Written by Mira Grant. The year was 2014. We had cured cancer. We had beaten the common cold. But in doing so we created something new, something terrible that no one could stop.

    The infection spread, virus blocks taking over bodies and minds with one, unstoppable command: FEED. Now, twenty years after the Rising, bloggers Georgia and Shaun Mason are on the trail of the biggest story of their lives—the dark conspiracy behind the infected.
    
    The truth will get out, even if it kills them.",
    image: "ALT TEXT FOR NOW"
},
"""