# Problem 67 Fibonacci Sequence

# generate a fib sequence up to a specific region, say up to 100

def create_fib_list(upto):
    x = 0 # initial values, x = 1st and y = 2nd
    y = 1
    arrFib = [x,y]
    for a in range(2,upto,1):
        x = arrFib[a - 2]
        y = arrFib[a - 1]
        z = x + y
        arrFib.append(z)

    return arrFib

# print(create_fib_list(1000))

arr1 = [322615043836854783580186309282650000354271239929,
        3803519665686090773261824444390176450610990315946847165272163502295150248561608391620538293153837330784168723765437946791613,
        332442083566252894269656048603015447982636854069531262697354582877665624295015454568572631693823274175996053045252971212422756826669,
        1133597084613134447271848482284309025629966048359864130560049384871348807054284272752352079971127752695,
        2143402371193585144275731144820024112622791843221056597232,
        13803567055491817972029187936825113333650564850089197542855968899086435571688,
        107168651819712326877926895128666735145224,
        16873133642056375905587710582599649871950164914626667247549740605066847393904820916710717780724785740147644757432744668969451486247747335959167429000482522247,
        871347450517368352816615810882615488381,
        35559105761336317101675609727370949148835212692110487405124336036528197882112012622415685107849500590668384026215022724033031344,
        467801993911057346969253632393329698441821925792111695787002567703451068793258021745557947676079828499403918483241873884718402,
        7308805952221443105020355490,
        10770594215935749279482183257489712959102052723690265265,
        370532318199874315782677688100794941155488404597348693204345997904322010547405701940310497780567966177501005104836947950824141300138427142200651677,
        1981641046217181630223446776341037079709877940526002389528019162689081976878763560907850195126187133921809903075415013440832808,
        225851433717,
        1150732583658441619074960448378430992861528480716347129290817711494041692989741780046107406408657135607164206366170756194420090405553241842130709,
        668226711200301698374224176558256700160458774333255425461900331623619273605518323137569702870357755802337031006361339094239227806499153841600804020665750176206357,
        23770696554372451866815101694984845480039225387896643963981,
        27713991332898951849369141694887577580844268614029932119435071462261690126253987857716252505338630328337483625842233853861187686551179198305850552365314432013776222604488073014165694290306137408859517,
        259396630450514843945535792456880074043523940756078363514486570322782139633750401577338505233670220572153381665]


def find_index(fibSequence, arr2):
    rst = ""
    for b in range(len(arr2)):
        rst = rst + " " + str(fibSequence.index(arr2[b]))
    return rst


arrFib = create_fib_list(1000)
print(find_index(arrFib,arr1))