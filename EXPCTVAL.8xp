:ClrHome
:Disp "EXPECTED VALUE"
:Disp "CALCULATOR"
:Disp ""
:Input "HOW MANY VALUES:",N
:If N<1 or N>10
:Then
:Disp "ERROR: ENTER 1-10 VALUES"
:Stop
:End
:
:0→S
:For(I,1,N)
:Disp "VALUE ",I
:Input "ENTER VALUE:",{L1}(I)
:Input "ENTER PROBABILITY:",{L2}(I)
:If {L2}(I)<0 or {L2}(I)>1
:Then
:Disp "ERROR: PROBABILITIES"
:Disp "MUST BE BETWEEN 0 AND 1"
:Stop
:End
:S+{L2}(I)→S
:End
:
:If abs(S-1)>0.001
:Then
:Disp "ERROR: PROBABILITIES"
:Disp "MUST SUM TO 1"
:Stop
:End
:
:0→E
:For(I,1,N)
:E+{L1}(I)*{L2}(I)→E
:End
:
:Disp "EXPECTED VALUE =",E