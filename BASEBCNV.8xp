:ClrHome
:Disp "BASE CONVERSION PROGRAM"
:Disp ""
:Disp "CONVERTS NUMBERS BETWEEN"
:Disp "DIFFERENT BASES (2-10)"
:Disp ""
:Input "ENTER NUMBER:",N
:Input "FROM BASE (2-10):",B
:Input "TO BASE (2-10):",B2
:If B<2 or B>10 or B2<2 or B2>10
:Then
:Disp "ERROR: BASES MUST BE"
:Disp "BETWEEN 2 AND 10"
:Stop
:End
:
:0→D
:N→T
:1→P
:While T>0
:remainder(T,10)→R
:If R≥B
:Then
:Disp "INVALID DIGIT FOR BASE"
:Stop
:End
:D+R*P→D
:P*B→P
:int(T/10)→T
:End
:
:""→Str1
:D→T
:If T=0:"0"→Str1
:While T>0
:remainder(T,B2)→R
:sub("0123456789",R+1,1)+Str1→Str1
:int(T/B2)→T
:End
:
:Disp N," IN BASE ",B
:Disp "IS ",Str1," IN BASE ",B2