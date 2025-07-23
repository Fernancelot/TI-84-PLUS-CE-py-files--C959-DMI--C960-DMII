:ClrHome
:Disp "SEQUENCE MODULO SOLVER"
:Disp ""
:Disp "COMPUTES VALUE OF A_N"
:Disp "BASED ON RECURSIVE"
:Disp "SEQUENCE WITH MOD 3 RULES"
:Disp ""
:Input "ENTER INITIAL VALUE A1:",A
:Input "ENTER TARGET TERM N:",N
:
:If A<0 or N<1
:Then
:Disp "ERROR: A1 MUST BE"
:Disp "NON-NEGATIVE AND N≥1"
:Stop
:End
:
:A→C
:For(I,1,N-1)
:If remainder(C,3)=0
:int(C/3)→C
:If remainder(C,3)=1
:int((C-1)/3)→C
:If remainder(C,3)=2
:int((C+1)/3)→C
:End
:
:Disp "THE VALUE OF A_",N
:Disp "IS:",C