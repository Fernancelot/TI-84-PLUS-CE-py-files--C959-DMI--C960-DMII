:ClrHome
:Disp "EXTENDED EUCLIDEAN"
:Disp "ALGORITHM"
:Disp ""
:Input "ENTER FIRST INTEGER:",A
:Input "ENTER SECOND INTEGER:",B
:
:A→A0
:B→B0
:1→X0
:0→X1
:0→Y0
:1→Y1
:
:While B≠0
:int(A/B)→Q
:B→T
:A-Q*B→A
:T→B
:X1→T
:X0-Q*X1→X1
:T→X0
:Y1→T
:Y0-Q*Y1→Y1
:T→Y0
:End
:
:Disp "GCD:",A
:Disp "COEFFICIENTS X AND Y:"
:Disp X0," AND ",Y0
:Disp "INTEGER A (COEFF FOR"
:Disp A0,") IS:",X0
:Disp "INTEGER B (COEFF FOR"
:Disp B0,") IS:",Y0
:
:If A=1
:Then
:Disp "MULTIPLICATIVE INVERSE"
:Disp "EXISTS"
:remainder(X0,B0)→I
:If I<0:I+B0→I
:Disp "INVERSE OF ",A0," MOD"
:Disp B0," IS ",I
:Else
:Disp "MULTIPLICATIVE INVERSE"
:Disp "DOES NOT EXIST"
:End