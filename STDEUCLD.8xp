:ClrHome
:Disp "CALCULATING GCD USING"
:Disp "EUCLIDEAN ALGORITHM"
:Disp ""
:Input "ENTER FIRST INTEGER:",A
:Input "ENTER SECOND INTEGER:",B
:
:A→A0
:B→B0
:
:Disp "STEPS:"
:While B≠0
:int(A/B)→Q
:remainder(A,B)→R
:Disp A," = ",B," × ",Q," + ",R
:B→A
:R→B
:End
:
:Disp ""
:Disp "GCD OF ",A0," AND ",B0
:Disp "IS: ",A