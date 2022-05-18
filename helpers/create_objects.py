"""
b1 = Book(title="Feed", author="Mira Grant", description="The year was 2014. We had cured cancer. We had beaten the common cold. But in doing so we created something new, something terrible that no one could stop.The infection spread, virus blocks taking over bodies and minds with one, unstoppable command: FEED. Now, twenty years after the Rising, bloggers Georgia and Shaun Mason are on the trail of the biggest story of their lives—the dark conspiracy behind the infected.The truth will get out, even if it kills them.", release=2010)
b2 = Book(title="Zone One", author="Colson Whitehead", description="Written by Colson Whitehead. A virus has laid waste to civilization, turning the infected into flesh-eating and mortally contagious zombies. But events have stabilized, and the rebuilding process has begun. Over a three-day span, 'Mark Spitz' and his fellow 'sweepers'—other survivors of the apocalypse—patrol portions of New York City, eliminating zombies as part of a mission to make the city habitable once again. Flashbacks pepper the narrative, explaining how Mark Spitz survived the apocalypse to date and got his nickname along the way.", release=2011)
b3 = Book(title="Undead Girl Gang", author="Lily Anderson", description="Mila Flores and her best friend Riley have always been inseparable. There's not much excitement in their small town of Cross Creek, so Mila and Riley make their own fun, devoting most of their time to Riley's favorite activity: amateur witchcraft. So when Riley and two Fairmont Academy mean girls die under suspicious circumstances, Mila refuses to believe everyone's explanation that her BFF was involved in a suicide pact. Instead, armed with a tube of lip gloss and an ancient grimoire, Mila does the unthinkable to uncover the truth: she brings the girls back to life.Unfortunately, Riley, June, and Dayton have no recollection of their murders, but they do have unfinished business to attend to. Now, with only seven days until the spell wears off and the girls return to their graves, Mila must wrangle the distracted group of undead teens and work fast to discover their murderer...before the killer strikes again.", release=2018)
l1 = List(title="March 2022", reviewer_id=1)
l2 = List(title="My Favorite Games", reviewer_id=1)
l3 = List(title="Watch With George", reviewer_id=1)

m1 = Movie(title="3 Hours Till Dead", description="An AWOL soldier with PTSD goes into hiding along with his brother and a few friends. They retreat into a rural farm area unaware that the outside world has ceased to function.  On their way back to civilization, his brother is attacked by an infected farmer. He quickly morphs into a rabid animal and lives for exactly three hours. Realizing they are in grave danger, they head back to the forest trying to outlive the legions of the infected.", release=2016)
m2 = Movie(title="8th Plague", description="When Launa’s sister doesn’t return from a camping trip in time for the sisters’ visit to their parent’s grave on the anniversary of their deaths she becomes obsessed with finding out why. Launa recruits a couple of friends to assist in the search, and the small group (along with an unwilling police officer and an even less willing ex-prison guard) soon finds themselves in an abandoned prison, surrounded by an ancient evil. A demonic curse has been unleashed and it seems there is no chance for escape.", release=2006)
m3 = Movie(title="13 Eerie", description="Six forensics undergraduates stay on a remote island to win an esteemed trainee position with the FBI, but no one knows that the site was used as an illegal biological testing ground and, now, horrifying creatures lurk in the shadows.", release=2013)

r1 = Reviewer(username="alixp")

t1 = Show(title="Acting Dead", description="Acting Dead is an American satirical dark comedy about the world of Hollywood zombies. The series focuses on Tate Blodgett, a zombie, and Alex Carbonneux, a ghost, as they both struggle with their new afterlife.", seasons=1, release=2014)
t2 = Show(title="All of Us Are Dead", description="After a failed science experiment, a local high school is overrun with zombies, and the trapped students struggle to survive. With no food or water, and communication cut-off by the government, they must use equipment around the school to protect themselves in the midst of a battleground or they will become part of the infected.", seasons=1, release=2022)

db.session.add(b1)
db.session.add(b2)
db.session.add(b3)
db.session.add(r1)
db.session.add(l1)
db.session.add(l2)
db.session.add(l3)
db.session.add(m1)
db.session.add(m2)
db.session.add(m3)
db.session.add(t1)
db.session.add(t2)
db.session.commit()
"""
g1 = Game(title="The Last of Us", description="", release=2013, platforms="PS3")