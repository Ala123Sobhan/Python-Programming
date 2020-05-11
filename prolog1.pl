person("Thanos").
person("Captain America").
person("Peter Parker").
person("Tony Stark").
person("Nebula").
person("Drax").
person("Thor").


place("Titan").
place("Brooklyn").
place("Queens").
place("Manhattan").
place("Xander").
place("Asgard").

thing("Infinity Gauntlet").
thing(shield).
thing("his fingers").
thing(web).

adverb(vigorously).
adverb(anxious).

adjective(young).
adjective(obsessive).
adjective(narcissist).
adjective(vengeful).
adjective(worthy).
adjective(red).
adjective(blue).

verb(destroy).
verb(snap).
verb(wield).
verb(weave).
verb(fight).

aux_vb1(is).
aux_verb2(will).

verb_3(destroys).
verb_3(snaps).
verb_3(wields).
verb_3(weaves).
verb_3(fights).

cont_verb(destroying).
cont_verb(snapping).
cont_verb(wielding).
cont_verb(weaving).
cont_verb(fighting).

preposition(from).
preposition(in).


isValidSentence(A,B,C):- person(A), verb_3(B),place(C).
isValidSentence(A,B,C):- person(A), verb_3(B),person(C).
isValidSentence(A,B,C):- person(A), verb_3(B),thing(C).


isValidSentence(A,B,C,D):- person(A), verb_3(B),thing(C),adverb(D).
isValidSentence(A,B,C,D):- person(A), verb_3(B),person(C),adverb(D).
isValidSentence(A,B,C,D):- person(A), verb_3(B),place(C),adverb(D).

isValidSentence(A,B,C):- person(A), aux_vb1(B), adjective(C).

isValidSentence(A,B,C,D):- person(A), aux_vb1(B),cont_verb(C),place(D).
isValidSentence(A,B,C,D):- person(A), aux_vb1(B),cont_verb(C),person(D).
isValidSentence(A,B,C,D):- person(A), aux_vb1(B),cont_verb(C),thing(D).

isValidSentence(A,B,C,D,E):-person(A),aux_vb1(B),cont_verb(C),place(D),adverb(E).
isValidSentence(A,B,C,D,E):-person(A),aux_vb1(B),cont_verb(C),person(D),adverb(E).
isValidSentence(A,B,C,D,E):-person(A),aux_vb1(B),cont_verb(C),thing(D),adverb(E).


isValidSentence(A,B,C,D):- person(A), aux_verb2(B),verb(C),place(D).
isValidSentence(A,B,C,D):- person(A), aux_verb2(B),verb(C),person(D).
isValidSentence(A,B,C,D):- person(A), aux_verb2(B),verb(C),thing(D).


isValidSentence(A,B,C,D,E):- person(A), aux_verb2(B),verb(C),place(D),adverb(E).
isValidSentence(A,B,C,D,E):- person(A), aux_verb2(B),verb(C),person(D),adverb(E).
isValidSentence(A,B,C,D,E):- person(A), aux_verb2(B),verb(C),thing(D),adverb(E).

isValidSentence(A,B,C,D):- person(A), aux_vb1(B),preposition(C),place(D).
