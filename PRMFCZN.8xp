:ClrHome
:Disp "PRIME FACTORIZATION"
:Disp "PROGRAM"
:Disp ""
:Disp "DETERMINE IF NUMBER IS"
:Disp "PRIME, IF NOT FIND"
:Disp "PRIME FACTORS"
:Disp ""
:Input "ENTER A NUMBER:",N
:
:If N≤1
:Then
:Disp N," IS NOT PRIME"
:Stop
:End
:
:If N≤3
:Then
:Disp N," IS PRIME"
:Stop
:End
:
:If remainder(N,2)=0 or remainder(N,3)=0
:Then
:Disp N," IS NOT PRIME"
:Goto PF
:End
:
:5→I
:1→P
:While I²≤N and P=1
:If remainder(N,I)=0 or remainder(N,I+2)=0
:0→P
:I+6→I
:End
:
:If P=1
:Then
:Disp N," IS PRIME"
:Stop
:End
:
:Lbl PF
:Disp N," IS NOT PRIME"
:Disp "PRIME FACTORIZATION:"
:
:ClrList L1
:0→F
:N→M
:2→I
:While I²≤M
:While remainder(M,I)=0
:F+1→F
:I→{L1}(F)
:M/I→M
:End
:I+1→I
:End
:If M>1
:Then
:F+1→F
:M→{L1}(F)
:End
:
:Disp "FACTORS: ",{L1}(1)
:For(K,2,F)
:Disp " × ",{L1}(K)
:End