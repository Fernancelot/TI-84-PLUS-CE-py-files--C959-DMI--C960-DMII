:ClrHome
:Disp "FAST MODULAR"
:Disp "EXPONENTIATION PROGRAM"
:Disp ""
:Input "ENTER THE BASE:",B
:Input "ENTER THE EXPONENT:",E
:Input "ENTER THE MODULO:",M
:
:1→R
:While E>0
:If remainder(E,2)=1
:remainder(R*B,M)→R
:remainder(B*B,M)→B
:int(E/2)→E
:End
:
:Disp "RESULT:",R