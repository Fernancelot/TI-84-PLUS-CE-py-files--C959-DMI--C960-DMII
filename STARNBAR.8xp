:ClrHome
:Disp "STAR-AND-BAR MULTISET"
:Disp "CALCULATOR"
:Disp ""
:Disp "CALCULATES WAYS TO"
:Disp "DISTRIBUTE N OBJECTS"
:Disp "INTO M BINS"
:Disp ""
:Input "ENTER NUMBER OF OBJECTS N:",N
:Input "ENTER NUMBER OF BINS M:",M
:
:If N<0 or M≤0
:Then
:Disp "ERROR: N≥0 AND M>0"
:Stop
:End
:
:(N+M-1)!/(((M-1)!)*N!)→R
:
:Disp "NUMBER OF WAYS TO"
:Disp "DISTRIBUTE ",N," OBJECTS"
:Disp "INTO ",M," BINS IS:",R