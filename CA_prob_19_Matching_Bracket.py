# Problem 19 Matching Brackets Jul 1st

ref = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

inv_ref = {v: k for k, v in ref.items()}


def check_seq(lst):
    opened = []
    for i in range(len(lst)):
        # print("currently reading %r" % (lst[i]))
        char = lst[i]
        if ref.get(char):           # if opened bracket, then append it.
            opened.append(char)
        elif inv_ref.get(char):     # if is a close bracket, then check if open already exist. 
            closed_char = inv_ref.get(char)
            try:
                if closed_char == opened[len(opened) - 1]:
                    opened.pop()
                else:
                    return 0
            except IndexError:
                return 0

    if len(opened) == 0:
        return 1
    else:
        return 0

ARR_Str = ["(a+[b*c]-{d/3})",
           "(a + [b * c) - 17]",
           "(((a * x) + [b] * y) + c",
           "auf(zlo)men [gy<psy>] four{s}"]

ARR_Str1 = ["<u><{h[+]<->{c}}[d(c)(%)][x]{{%} {d}{ }(e)}>",
            "{z}(v[%]){({-}e)v}(fu[/]{}( )(g)(u)(g)(z)())",
            "[{f}]({f}[v(^)[v]{z}]g){[<->*<e></>] }{x}</>(x)",
            "(<+}%)(t){(y{u{<*>e}}){{w>z}(/)<t>{c[t]}<z[x]>}{+}[^]{[v]w}{+}(g)",
            "(( ))[ ](^)[[c]{w}[e(%)][/]*{<b>t}<(u){{y}z{+[x]}}*> b>]",
            "<g>{{{*}[g]> }<+{z({ }<t>u)}}{h}[<<(-)c> (y)<g>>v][u](^<->)",
             "a>([w{[t]-}](w)<[y]h>h<d>){h}[g]<t>(z(d)){*({c}d<u[e]>)}{}",
            "[(*){( ){[y]<b><{%}^{h[-]}>g}w}[+(a)](w)({/}%)]",
            "{z}(f){%[a]}[ ]<{ }>(^(z)[[y[e<d>]<c>][<y><b{b}>u) ][%]<b>]<f><u>",
            "<+(<w<%>>e)<<x<[-][t]d>><+(a){w(e)<g{v}>}{b}>c >{<x>}",
            "(g){b(z(/))}{-}(f){f{-}<[g](w){ }u>{+}}[{+}[f]{h}]",
            "{}{u}}z{[a]-(^)<>(a)[ (h(f[y{[a]%(b)}]))](<t{<b<x>>w}>e)",
            "[v][(w)/](e)[*][+]([[<e> ]y[[*]u]]){-[a]<h>}",
            "<{t}d>{u}<v>{{y<v<f>> b<z>}[< >w](){+}{a(*)}<+><z>{t}",
            "(g){h}(u)(h)<[x]< h}( )v[u]><{^}a><{v}{w}<v><{>{d}d>><t>(u)<u>",
            "{(h) }({[h<x><x>]<+>y< (z){g(^)}[w]>[v]<c>})",
            "[f]<a><g><{{y[w](^)}*}[<</><^>f<e>[b]>*][g]{z}<z>><%>(a){[e]d}",
            "<<^>h>[d]([{ {t}} ]{{c(-)}<[[e]d]f>e}(w[y])[w])(d){ }",
            "(u[t])[<b>[c] <t>[ct]<(t)<<(a)]<( )<x>z>>z>(u)( )<< >t>>{f}"
            ]

for ls in ARR_Str1:
    print(check_seq(ls), end=" ")