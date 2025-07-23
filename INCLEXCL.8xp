:ClrHome
:Disp "INCLUSION-EXCLUSION"
:Disp "PRINCIPLE CALCULATOR"
:Disp ""
:Disp "ENTER 2 FOR TWO SETS"
:Disp "ENTER 3 FOR THREE SETS"
:Input "CHOICE:",C
:
:If C=2
:Then
:Input "ENTER |A|:",A
:Input "ENTER |B|:",B
:Input "ENTER |A ∩ B|:",X
:A+B-X→U
:Disp "|A ∪ B| =",U
:End
:
:If C=3
:Then
:Input "ENTER |A|:",A
:Input "ENTER |B|:",B
:Input "ENTER |C|:",D
:Input "ENTER |A ∩ B|:",X
:Input "ENTER |A ∩ C|:",Y
:Input "ENTER |B ∩ C|:",Z
:Input "ENTER |A ∩ B ∩ C|:",W
:A+B+D-X-Y-Z+W→U
:Disp "|A ∪ B ∪ C| =",U
:End
:
:If C≠2 and C≠3
:Then
:Disp "INVALID CHOICE"
:Disp "PLEASE SELECT 2 OR 3"
:End