:ClrHome
:Disp "DIVISION ALGORITHM"
:Disp "MODULAR ARITHMETIC DEMO"
:Disp ""
:
:Lbl START
:Input "ENTER BASE VALUE X"
:Disp "(OR 0 TO QUIT):",X
:If X=0:Stop
:Input "ENTER EXPONENT FOR X"
:Disp "(1 IF NO EXPONENT):",A
:Input "ENTER BASE VALUE Y:",Y
:Input "ENTER EXPONENT FOR Y"
:Disp "(1 IF NO EXPONENT):",B
:
:remainder(X,10)→M
:remainder(Y,10)→N
:remainder(M^A,10)→P
:remainder(N^B,10)→Q
:remainder(P+Q,10)→R
:
:Disp "(",X,"^",A," + ",Y,"^",B,") MOD 10"
:Pause
:Disp "= [(",X," MOD 10)^",A
:Disp "+ (",Y," MOD 10)^",B,"] MOD 10"
:Pause
:Disp "= [(",M,"^",A," MOD 10)"
:Disp "+ (",N,"^",B," MOD 10)] MOD 10"
:Pause
:Disp "= [",P," + ",Q,"] MOD 10"
:Disp "= ",R
:Pause
:Goto START