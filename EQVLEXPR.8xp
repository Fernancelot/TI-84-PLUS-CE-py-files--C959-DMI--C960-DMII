:ClrHome
:Disp "EXPONENT DECOMPOSER"
:Disp ""
:Disp "DECOMPOSES BASE AND"
:Disp "EXPONENT INTO PRODUCT"
:Disp "OF SMALLER POWERS"
:Disp ""
:Input "ENTER BASE:",B
:Input "ENTER EXPONENT:",E
:
:If B≤0 or E≤0
:Then
:Disp "ERROR: BASE AND EXPONENT"
:Disp "MUST BE POSITIVE"
:Stop
:End
:
:ClrList L1
:0→C
:E→T
:0→P
:While T>0
:If remainder(T,2)=1
:Then
:C+1→C
:P→{L1}(C)
:End
:int(T/2)→T
:P+1→P
:End
:
:Disp B,"^",E," ="
:For(I,C,1,-1)
:2^{L1}(I)→X
:If I=1
:Then
:Disp B,"^",X
:Else
:Disp B,"^",X," × "
:End
:End