% parents

% first generation
p(victoria, edward_vii).
p(albert, edward_vii).

% second generation
p(edward_vii, george_v).
p(edward_vii, mary).
p(alexandra, george_v).
p(alexandra, mary).

% third generation
p(george_v, edward_mill).
p(george_v, george_vi).
p(mary, edward_mill).
p(mary, george_vi).

% fourth generation
p(george_vi, elizabeth_ii).
p(george_vi, margaret).
p(elizabeth, elizabeth_ii).
p(elizabeth, margaret).

% fifth generation
p(philip, charles).
p(philip, anne).
p(philip, andrew).
p(philip, edward).
p(elizabeth_ii, charles).
p(elizabeth_ii, anne).
p(elizabeth_ii, andrew).
p(elizabeth_ii, edward).

% sixth generation
p(charles, william).
p(charles, harry).
p(diana, william).
p(diana, harry).

% seventh generation
p(william, george).
p(william, charlotte).
p(william, louis).
p(catherine, george).
p(catherine, charlotte).
p(catherine, louis).


% gender

male(albert).
male(edward_vii).
male(george_v).
male(edward_mill).
male(george_vi).
male(philip).
male(charles).
male(andrew).
male(edward).
male(william).
male(harry).
male(george).
male(louis).


% rules

g(X, Y) :- p(X, Z), p(Z, Y).
f(X, Y) :- p(X, Y), male(X).