### Generator: Password

A generator used to generate passwords (obviously).

### Commandline arguments/parameters:
Copied from the commandline, using the '--help' parameter:

    -h, --help          show this help message and exit
    
    -o FLAGOUTPUT, --output=FLAGOUTPUT
                        File to output passwords to in the format of
                        "Password1\nPassword2\n"
                        
    -w FLAGWHITELIST, --whitelist=FLAGWHITELIST
                        List or file containing characters/words to be used
                        for the password generation. The characters/words need
                        to be separated by \r\n
                        
    -b FLAGBLACKLIST, --blacklist=FLAGBLACKLIST
                        List of file containing characters/words which
                        shouldn't be used for password generation. The
                        characters/words need to be separated by \r\n
                        
    -a FLAGAMOUNT, --amount=FLAGAMOUNT 
                        Amount of passwords to generate
                        
    -l FLAGLENGTH, --length=FLAGLENGTH 
                        Lengths for the passwords
                        
    --llc=FLAGLLC       Use lowercase letters
    --luc=FLAGLUC       Use uppercase letters
    --num=FLAGNUMBERS   Use numbers
    --sc=FLAGSC         Use special characters
    --sca=FLAGSCA       Use additional (generally not accepted) special characters
    
### Applications
If no arguments are given, gPass will generate a single password using upper- & lower-case letters, numbers and special characters with a length of 8 characters.

Using the blacklist argument you can prevent certain words (racist or in other ways mean) from being generated (even though the chance for a word being generated using the default setup is about 0%).

Disabling all predefined character collections and using the whitelist argument with a list of words (maybe from a dictionary), and maybe enabling numbers, you can create simple passwords that are somewhat safe and can still be remembered easily (even though I discourage the use of simple passwords). 

### Generation speed
I've quickly tested how fast a password can be generated. For this I've generated 8 passwords with a length of 256 characters (no, I don't know why anybody would need or could even correctly enter a 256 long password). 
 
    1.5 ms | 0.5 ms | 1.0 ms | 0.5 ms | 0.5 ms | 1.0 ms | 1.0 ms | 0.5 ms  

Original output:  

    [#] Password 1: kONAV=S4kP,r+?@[C3lY_GK0PKU&y+a_nX")z'$QU:Nb[€T6&UkEgJN**Z2NY@Y0s0=eEx{uf8/bc/I+aT"D/pX9YMP5Iti26ubm}$twuS4FACB6x9&1}m=?S?aax&=%ODe)Chq{]@?_K~T%OYKqJ;+!ynw{VMjcb%fMVZx"K,bf1@p;@n&EzGpJ*Ph(QuY_PYXdhYU%+Yw'bh-9l=syP6CkO[W3&b0W[0_&ma3!*v0h/G7"z=XVw8'9nqG?LYsS (1.5ms)
    [#] Password 2: EQRN*)L[(_r?3Y7!?oEFxBz$P]}khR'%DE=YW;BPKe5:fNGmt5Ug!VR)rWP}{)p1?sxVe!{R,LCjkGgfJsWY%~N3LcFnvecBSic:,*JUQ7jN]R=S$UFHl]--ZRIwwB4+kx2_ZNU[y4UDbm}G=i5t]4EYnsE€#rSUvV.)H:{6EY?;b9f\&u'$~d?{cVg9PFmY.NQt'Yz,8S€$E=Ky.6bRoQ[UUD:oM+/;XCM*kSW$aAb%890-tv2z,[Y$E_OG+XwQ (0.500244140625ms)
    [#] Password 3: MO2WcDxwfRug]Vpg~(UCn@o;kYFuS%fK4yL#l_.iMY,R)1pBg[A/dFaiF,$!x=SQ-H"8+!EMJ,tWxV37W3?Aem0=DoMbtt6j.=€:8CCPd6?{*'((y4.,aWPboGLF)pEOkBsqQ#drvnG5/RqtBlr;/!~f#7{ozO/mIkkoMmMUTX\h?EX€qlm'pG*€7W]}+S,}Y~HJD\FutZwW0LXP_P~t[w.#$B*'8~c]6csG:f2t/}%Q1OA$rre'fl'w3.*{cm;X (0.99951171875ms)
    [#] Password 4: lO{pwyoI&QXDtQCqe*G"Tu-x9}hO#q)cyO/U(@d@YJYW",]'('Yy8:wAJM"E8//%wdwT€}_};p}wZ":e\wlBbBy"%(j@spgc,(b?Rug1&QE(-€nolgP4uin+pLgdm${Bv"PY@5X(mi0#t~sr9~W66A,[ax5z$?/7?@@8zrBY;tN\chEt&?s6$agq\uiczDWMpdcevw!_n4j8;t*+%yIr6h!ho;p&Mcw.@cgA!J)z}wS/rU-F-UZe€=cV&G4OS@'# (0.50048828125ms)
    [#] Password 5: AF*M[KpyUo&Jff:x3h,D,?ZX%vV,€ZGurdiIv?_NJ73@$RGZwtki#n?V/zRFsQaTSo~z~v+{SgAwCnTmITeX/N=jQt4DrbaCn*s{\%/Z2Y:gTvdNdHhk'0Tzx**pCE€ugy_.Op?8h!{+\cm+}~dQq3dqws-S&BU1?hhaVj\G)XkOp#Ivd@EI'AS=tosj~-GfaT@"WxQ'mBOF?kj8a&,K]€Adx!Oq1=5*6#})Y48{*V1X,C]Bg5"%y€v3{{PVY@S& (0.493896484375ms)
    [#] Password 6: dhnx3.#.[z*Yce.K)f28\uX+j;'?C&wzo6Y*y2&?tqA&l'Lq{6h@%\VhvrY+A?MI,ieztw0eSo_n?lb5+hG;#)rzk-f€6=D"Y3_~S18d?Lts@&"sUoUsy"~4J~+tQNX)0x[$6riOiw"T%a9$$i0g5'OV;6cWGyR{vE3ugAxxKhgQEQY*AvTVcnAP%ea:5Q$$maIY]v%++8kMWaErrEeT(F5o!SI8ZbU.qS[ln0/Zk]8-H~l)?LrH(=G"GaUcskir (0.9990234375ms)
    [#] Password 7: NpRE"}l{eL]8+)y2Qf\&CvKFFZt\6i"xMU[c7&xQ;:*bm€U?a@p74~p+AJ=;:S/wv]UU4gJ$bN#a€pSft+c;U,3&yQnKEFw2Pit&@NL@L1}5j#€p!+,hl.L"}B=eExbxwQW:;EptQ:1S(lcYa8cNR35Yd:8Om)@e&gi'dBubs{qgXjD%%/4%#/)T7OiV?yFWAo0$d?H~G3A1tcu[M"/Iwd9Fy€.[I@$M[€"oIxRD;P6u)EXu90FKq79-hiJq}+pX (1.0ms)
    [#] Password 8: uu[;ehf+€@F/@x9w&j_ULDct0+Y,K5YQ9:p@KvSk+~0_S*(€-\Hv}C}"-"eI22v@/&FLK.2\vwC4%_MC8ZE){"8;wosrp~!/&;~\%KkZ.KLkeJU€-/f8T:ts{=7-BP=q/EfWAqbVA0':b9TVT!g5kP]7@48G[41J3_vu+WA~1aD,yz\"h](0lyzC€v8;P*g{,G9*y?B.UFiG3=hzdQ{JBtLO$Mc,0eN]x_eUycYeH2:I}9P=f,q)N?4$JqE~€W$V (0.53271484375ms)
    
It's pretty fast, so no worries there.

(Tested on an AMD FX-8350 @ 4.00GHz on Windows 10 Version 1703 using Python 3.6.0 inside PyCharm 2017.1.2)
