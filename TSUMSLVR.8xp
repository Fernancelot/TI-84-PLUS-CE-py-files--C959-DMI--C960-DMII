:ClrHome
:Disp "TELESCOPING SUM SOLVER"
:Disp ""
:Disp "COMPUTES P(N) DEFINED"
:Disp "AS TELESCOPING SUM"
:Disp ""
:Input "ENTER POSITIVE INTEGER N:",N
:
:If N<1
:Then
:Disp "ERROR: N MUST BE"
:Disp "POSITIVE INTEGER"
:Stop
:End
:
:0→R
:For(K,1,N)
:R+(1/K)-(1/(K+1))→R
:End
:
:Disp "THE VALUE OF P(",N,") IS:"
:Disp R