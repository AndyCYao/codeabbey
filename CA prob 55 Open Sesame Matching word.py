# Problem 55 Jun 23rd 2015 Open Sesame Matching word

strInput = "gyk dak meq zeq rit gyc rik bac nox let dak noq vok jas bis jit duc bok boh dus bys met ruc beh deq nyk vyt byt vas lys lef bak lih juq myx ris maq rat joc nyt mak boc baf beq zox liq zaf moq buq rus dif rep vok lyf ris lax max mes ruq vos nyp jyf jox noh vus boc niq vut bec mik mah mys jax lak vus dic goq zek dec zif loh bep zuh luf guf nec jap roc rix zoq reh dik voh rif veq zap zec nip duf daf beh muh vyt dof bop rix rif vep miq mip gos rit geh vec jat jef zoh lap gac gaq zys vyc bik gat mak jof zoq gyp laq res nyf maq lef zec mef gof zuf bak rux nuh myk rek gaq nek bux goc gex las rix duh jeh dyt gih lex zok gef roh dus gyq ryf viq bip ryk zoh zek bus lyk daq moh vyh vac joq mik muf lep dah buk ryh map ruf zyq luq nof nef meq lyt loh zox jok zak luk doc jit gyk lak ves ryt guc lac rus gef bex jyh zof res dat neq jec naf vef das byf nyt zeq dyt lyq vis zik gef vis gix jof baf rik lux bys jyk bah jek gus ryt gek bik bop noq doh but dos nuf mus zeq nyf vih lut jas mac muc dut luk bep muk zoc gak luc nih dop joc raf gok rik meh lyf rix jef gis rek byk laf baq gek bac vys guh goh rox joc dih juk zit zof byq vyh gaf nuk gyt zek zaq bax gyk nik dos nuk myc nys jaq myk max zuf muc bos lox gup end"
# ARR_Str1 = ["nun", "lam", "mip", 'tex', 'bal', 'pif', 'sot', 'bal', 'bod', 'tex', 'end']

ARR_Str = sorted(strInput.split())

cnt = {}

for wrd in ARR_Str:
    if cnt.get(wrd):
        i = cnt[wrd]
        cnt[wrd] = i + 1
    else:
        cnt[wrd] = 1

print(cnt)

arrDup = []
for k in cnt:
    if cnt[k] > 1:
        arrDup.append(k)

print(" ".join(sorted(arrDup)))