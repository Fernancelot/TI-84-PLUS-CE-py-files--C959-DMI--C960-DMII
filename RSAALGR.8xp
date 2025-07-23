:ClrHome
:Disp "RSA ALGORITHM"
:Disp "FOR TI-BASIC"
:Disp ""
:Input "ENTER PRIME P:",P
:Input "ENTER PRIME Q:",Q  
:Input "ENTER PUBLIC EXP E:",E
:
:P*Q→N
:(P-1)*(Q-1)→F
:
:Lbl GCD
:E→A
:F→B
:While B≠0
:B→T
:remainder(A,B)→B
:T→A
:End
:If A≠1
:Then
:Disp "INVALID E. MUST BE"
:Disp "COPRIME WITH PHI(N)"
:Stop
:End
:
:Lbl MODINV
:F→A
:E→B
:0→U
:1→V
:While B≠0
:int(A/B)→G
:B→T
:remainder(A,B)→A
:T→B
:V→T
:U-G*V→V
:T→U
:End
:If A≠1
:Then
:Disp "NO MODULAR INVERSE"
:Stop
:End
:remainder(U,F)→D
:If D<0:D+F→D
:
:Disp "PUBLIC KEY:"
:Disp "E=",E," N=",N
:Disp "PRIVATE KEY:"
:Disp "D=",D," N=",N
:
:Input "ENTER PLAINTEXT:",M
:
:Lbl MODEXP
:1→R
:M→B
:E→X
:While X>0
:If remainder(X,2)=1
:remainder(R*B,N)→R
:int(X/2)→X
:remainder(B*B,N)→B
:End
:
:Disp "CIPHERTEXT:",R
:
:1→S
:R→B
:D→X
:While X>0
:If remainder(X,2)=1
:remainder(S*B,N)→S
:int(X/2)→X
:remainder(B*B,N)→B
:End
:
:Disp "DECRYPTED:",S