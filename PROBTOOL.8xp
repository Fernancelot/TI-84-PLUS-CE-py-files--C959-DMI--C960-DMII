:ClrHome
:Disp "UNIT 5: PROBABILITY TOOLS"
:Disp ""
:Disp "1. CONDITIONAL PROBABILITY"
:Disp "   AND BAYES' THEOREM"
:Disp "2. COMBINATORIAL PROBABILITY"
:Disp "3. PROBABILITY DISTRIBUTIONS"
:Disp "4. EXIT"
:Input "ENTER YOUR CHOICE:",C
:
:If C=1
:Then
:Disp "CONDITIONAL PROBABILITY"
:Disp "AND BAYES' THEOREM"
:Input "ENTER P(A):",A
:Input "ENTER P(B):",B
:Input "ENTER P(B|A):",X
:If B=0
:Then
:Disp "ERROR: P(B) CANNOT BE 0"
:Stop
:End
:(X*A)/B→Y
:Disp "P(A|B):",round(Y,4)
:End
:
:If C=2
:Then
:Disp "COMBINATORIAL PROBABILITY"
:Input "TOTAL OUTCOMES (N):",N
:Input "DESIRED OUTCOMES (R):",R
:Input "SAMPLE SIZE (K):",K
:N!/(R!*(N-R)!)→T1
:N!/(K!*(N-K)!)→T2
:If T2=0
:Then
:Disp "ERROR: DENOMINATOR IS 0"
:Stop
:End
:T1/T2→P
:Disp "PROBABILITY:",round(P,4)
:End
:
:If C=3
:Then
:Disp "PROBABILITY DISTRIBUTIONS"
:Disp "ENTER UP TO 5 OUTCOMES"
:Input "HOW MANY OUTCOMES:",M
:If M>5 or M<1
:Then
:Disp "ERROR: 1-5 OUTCOMES ONLY"
:Stop
:End
:0→S
:0→E
:For(I,1,M)
:Disp "OUTCOME ",I
:Input "VALUE:",{L1}(I)
:Input "PROBABILITY:",{L2}(I)
:S+{L2}(I)→S
:E+{L1}(I)*{L2}(I)→E
:End
:If abs(S-1)>0.001
:Then
:Disp "ERROR: PROBABILITIES"
:Disp "MUST SUM TO 1"
:Stop
:End
:Disp "OUTCOME  PROBABILITY"
:For(I,1,M)
:Disp {L1}(I),"    ",round({L2}(I),4)
:End
:Disp "EXPECTED VALUE:",round(E,4)
:End
:
:If C=4
:Then
:Disp "EXITING PROGRAM"
:Stop
:End
:
:If C<1 or C>4
:Then
:Disp "INVALID CHOICE"
:Disp "SELECT FROM MENU"
:End