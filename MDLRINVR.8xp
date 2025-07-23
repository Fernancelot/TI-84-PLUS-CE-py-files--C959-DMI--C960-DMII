:ClrHome
:Disp "FIND MODULAR INVERSE"
:Disp "OF A UNDER MODULO M"
:Disp ""
:Disp "ASSUMPTION: M IS PRIME"
:Disp ""
:Input "ENTER A:",A
:Input "ENTER M (PRIME):",M
:
:Lbl GCD
:A→X
:M→Y
:While Y≠0
:remainder(X,Y)→T
:Y→X
:T→Y
:End
:
:If X≠1
:Then
:Disp "INVERSE DOESN'T EXIST"
:Stop
:End
:
:Lbl POWER
:1→R
:A→B
:M-2→E
:While E>0
:If remainder(E,2)=1
:remainder(R*B,M)→R
:int(E/2)→E
:remainder(B*B,M)→B
:End
:
:Disp "MODULAR MULTIPLICATIVE"
:Disp "INVERSE IS ",R