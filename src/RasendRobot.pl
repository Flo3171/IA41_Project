% résolution du jeu de Rasend Robot en prolog


% on définit une position par une liste telle que [coordonéeX, coordonnéeY]
% on définit un robot par une liste telle que [couleur, position]
% on définit un objectif par une liste telle que [couleur, position]


% mur(direction, position).
% les mur qui délimitent les côté du plateau
mur(haut, [_, 0]).
mur(gauche, [0, _]).
mur(bas, [_, 15]).
mur(droite, [15,  0]).

% les autre murs partout sur le plateau (penser à bien les mettre 2 fois car un mur vertical empeche les déplacement qui viennent de la gauche et de la droite)
mur(haut, [3, 5]).
mur(bas, [3, 4]).


% deplacement(couleur robot, position initiale, position finale)
depalcement(_, [X, _], [X, _]).
deplacement(_, [_, Y], [_, Y]). 


% valide(cocouleur robotuleur,position initiale, position finale)

valide(_, _, _).

% deplacementValide(couleur robot, position initiale, position finale)

deplacementValide(C, I, F) :- depalcement(C, I, F), valide(C, I, F).


% findPath([robot1, ..., robot4], objectif)

% findPath([R1, R2, R3, R4], O) :- deplacementValide(C, I, F), findPath()



% findPath([[rouge, 0, 0], [jaune, [15, 0]], [vert, [15, 15]], bleu, [0, 15]], [bleu, [5, 3]]).
