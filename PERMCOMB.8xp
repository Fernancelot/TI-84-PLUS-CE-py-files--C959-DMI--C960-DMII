:ClrHome
:Disp "PERMUTATIONS AND"
:Disp "COMBINATIONS CALCULATOR"
:Disp ""
:Disp "1: PERMUTATIONS P(N,R)"
:Disp "2: COMBINATIONS C(N,R)"
:Input "ENTER CHOICE (1 OR 2):",C
:If C≠1 and C≠2
:Then
:Disp "INVALID CHOICE"
:Disp "PLEASE SELECT 1 OR 2"
:Stop
:End
:Input "ENTER N (TOTAL ITEMS):",N
:Input "ENTER R (ITEMS CHOSEN):",R
:If N<0 or R<0 or R>N
:Then
:Disp "ERROR: ENSURE 0≤R≤N"
:Stop
:End
:If C=1
:Then
:N!/(N-R)!→P
:Disp "P(",N,",",R,") =",P
:End
:If C=2
:Then
:N!/(R!*(N-R)!)→P
:Disp "C(",N,",",R,") =",P
:End