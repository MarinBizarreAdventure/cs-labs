import matplotlib.pyplot as plt
from collections import Counter
import nltk
from nltk.corpus import words
import string


english_frequency = {
    'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
    'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
    'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
    'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15,
    'Q': 0.10, 'Z': 0.07
}


encrypted_text = """Cinz wqvpv wrn cdgotzvgwts uixghxusvp cni pvsvhwxgj dptasv cxvsohxuqvip, Lvihlqnccp ovodhvo
pxy puvhxcxh ivbdxivzvgwp: (1) wqv pfpwvzpqndso av, xc gnw wqvnivwxhtssf dgaivtltasv,
dgaivtltasv xg uithwxhv; (2)hnzuinzxpv nc wqv pfpwvz pqndso gnw xghngkvgxvghv wqv
hniivpungovgwp;(3) wqv lvf pqndso av ivzvzavitasv rxwqndw gnwvp tgo pqndso av
vtpxsfhqtgjvtasv; (4) wqv hifuwnjitzp pqndso av witgpzxppxasv af wvsvjituq; (5)wqv tuutitwdp ni
onhdzvgwp pqndso av uniwtasv tgo nuvitasv af t pxgjsvuvipng; (6) wqv pfpwvz pqndso av vtpf,
gvxwqvi ivbdxixgj lgnrsvojv nc tsngj sxpw nc idsvp gni xgknskxgj zvgwts pwitxg.Wqvpv
ivbdxivzvgwp pwxss hnzuixpv wqv xovts rqxhq zxsxwtif hxuqvip txztw. Wqvf qtkv avvg ivuqitpvo,
tgo bdtsxwxvp wqtw sxv xzusxhxw qtkv -avvgztov vyusxhxw. Adw tgf znovig hifuwnjituqvi rndso
av kvif qtuuf xc tgfhxuqvi cdscxssvo tss pxy.Nc hndipv, xw qtp gvkvi avvg unppxasv wn on wqtw.
Wqviv tuuvtip wn av thviwtxg xghnzutwxaxsxwf tzngj wqvz wqtw ztlvp xw xzunppxasv wn
xgpwxwdwvtss nc wqvz tw nghv. Wqv ivbdxivzvgw wqtw xp dpdtssf pthixcxhvo xp wqv
cxipw.Lvihlqnccp tijdvo pwingjsf tjtxgpw wqv gnwxng nc t cxvso hxuqvi wqtw rndsopxzusf ivpxpw
pnsdwxng sngj vgndjq cni wqv niovip xw witgpzxwwvo wn avhtiixvo ndw. Wqxp rtp gnw vgndjq,
qv ptxo, ovhstixgj wqtw "wqv pvhivwztwwvi xg hnzzdgxhtwxngp pvgw nkvi t oxpwtghv kvif ncwvg
ivwtxgp xwpxzuniwtghv avfngo wqv otf ng rqxhq xw rtp witgpzxwwvo." Qv rtp ng wqvpxov nc wqv
tgjvsp, adw t uithwxhts cxvso hxuqvi wqtw xp dgaivtltasv rtpgnw unppxasv xg qxp otf, gni xp xw
wnotf, tgo pn zxsxwtif hifuwnjituqf qtppvwwsvo cni cxvso hxuqvip wqtw ovstf adw on gnw ovcvtw
hifuwtgtsfpxp.Uviqtup wqv znpw pwtiwsxgj ivbdxivzvgw, tw cxipw jstghv, rtp wqv pvhngo.
Lvihlqnccp vyustxgvo wqtw af "pfpwvz" qv zvtgw "wqvztwvixts utiw nc wqv pfpwvz; wtasvtdy,
hnov annlp, ni rqtwvkvizvhqtgxhts tuutitwdp ztf av gvhvpptif," tgo gnw "wqv lvf uinuvi."Lvihlqnccp
qviv ztlvp cni wqv cxipw wxzv wqv oxpwxghwxng, gnr atpxh wnhifuwnsnjf, avwrvvg wqv jvgvits
pfpwvz tgo wqv puvhxcxh lvf. Rqf zdpwwqv jvgvits pfpwvz "gnw ivbdxiv pvhivhf," tp, cni vytzusv,
t hnovannlivbdxivp xw? Rqf zdpw xw av "t uinhvpp wqtw. . . ndi gvxjqanip htg vkvghnuf tgo tonuw"?
Avhtdpv, Lvihlqnccp ptxo, "xw xp gnw gvhvpptif wnhngediv du xztjxgtif uqtgwnzp tgo wn pdpuvhw
wqv xghniiduwxaxsxwf ncvzusnfvvp ni pdatswvigp wn dgovipwtgo wqtw, xc t pfpwvz
ivbdxixgjpvhivhf rviv xg wqv qtgop nc wnn stijv t gdzavi nc xgoxkxodtsp, xw hndsoav hnzuinzxpvo
tw vthq vgjtjvzvgw xg rqxhq ngv ni tgnwqvi nc wqvzwnnl utiw." Wqxp qtp uinkvo wn av widv, tgo
Lvihlqnccp' pvhngoivbdxivzvgw qtp avhnzv rxovsf thhvuwvo dgovi t cniz wqtw xp pnzvwxzvphtssvo
wqv cdgotzvgwts tppdzuwxng nc zxsxwtif hifuwnjituqf: wqtw wqvvgvzf lgnrp wqv jvgvits pfpwvz.
Adw qv zdpw pwxss av dgtasv wn pnskvzvpptjvp xg xw rxwqndw lgnrxgj wqv puvhxcxh lvf. Xg
xwp znovigcnizdstwxng, wqv Lvihlqnccp onhwixgv pwtwvp wqtw pvhivhf zdpw ivpxovpnsvsf xg
wqv lvfp.Qto Lvihlqnccp zvivsf udasxpqvo qxp uvihvuwxngp nc wqv uinasvzpcthxgj unpwwvsvjituq hifuwnjituqf tgo qxp uivphixuwxngp cni ivpnskxgjwqvz, qv rndso qtkv tppdivo t usthv cni
qxzpvsc xg wqv utgwqvng nchifuwnsnjf. Adw qv oxo zniv. Qv hngwixadwvo t wvhqgxbdv nc
hifuwtgtsfpxpwqtw xp nc pduivzv xzuniwtghv wnotf. Htssvo "pduvixzunpxwxng,"
xwhngpwxwdwvp wqv znpw jvgvits pnsdwxng cni unsftsuqtavwxh pdapwxwdwxngpfpwvzp. Rxwq
cvr vyhvuwxngp, xw stfp gn ivpwixhwxngp ng wqv wfuv ni svgjwqnc lvfp, tp onvp wqv Ltpxplx
zvwqno, gni ng wqv tsuqtavwp, rqxhq ztf avxgwviivstwvo ni vgwxivsf xgovuvgovgw. Xw rtgwp ngsf
pvkvits zvpptjvp xgwqv ptzv lvf. Wqv hifuwtgtsfpw zdpw tsxjg wqvpv ngv tankv wqv nwqvi pnwqtw
svwwvip vghxuqvivo rxwq wqv ptzv lvfsvwwvi rxss ctss xgwn t pxgjsvhnsdzg. Xg wqv pxzusvpw
htpv, wqtw nc t idggxgj lvf (t kvif sngjhngwxgdndp wvyw dpvo tp t lvf, tp t gnkvs) wqtw ivpwtiwp
rxwq vthqzvpptjv, qv htg on wqxp pxzusf af usthxgj tss wqv cxipw svwwvip xg wqv cxipwhnsdzg,
tss wqv pvhngo svwwvip xg wqv gvyw hnsdzg, tgo pn ng."""


filtered_text = ''.join([char for char in encrypted_text if char.isalpha()]).upper()
text_length = len(filtered_text)


frequency_counter = Counter(filtered_text)
cipher_frequency = {char: (count / text_length) * 100 for char, count in frequency_counter.items()}


sorted_english_freq = dict(sorted(english_frequency.items(), key=lambda item: item[1], reverse=True))
sorted_cipher_freq = dict(sorted(cipher_frequency.items(), key=lambda item: item[1], reverse=True))


def plot_frequencies(english_freq, cipher_freq):
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    plt.bar(english_freq.keys(), english_freq.values(), color='blue', alpha=0.7)
    plt.title("English Letter Frequencies")
    plt.xlabel("Letters")
    plt.ylabel("Frequency (%)")

    plt.subplot(1, 2, 2)
    plt.bar(cipher_freq.keys(), cipher_freq.values(), color='red', alpha=0.7)
    plt.title("Cipher Text Letter Frequencies")
    plt.xlabel("Letters")
    plt.ylabel("Frequency (%)")

    plt.tight_layout()
    plt.show()


decrypted_text = encrypted_text.upper()

decrypted_text = decrypted_text.replace('V', 'e')
decrypted_text = decrypted_text.replace('W','t')
decrypted_text = decrypted_text.replace('T','a')
decrypted_text = decrypted_text.replace('X','i')
decrypted_text = decrypted_text.replace('Q','h')
decrypted_text = decrypted_text.replace('G','n')
decrypted_text = decrypted_text.replace('O','d')
decrypted_text = decrypted_text.replace('I','r')
decrypted_text = decrypted_text.replace('P','s')
decrypted_text = decrypted_text.replace('N','o')
decrypted_text = decrypted_text.replace('C','f')
decrypted_text = decrypted_text.replace('A','b')
decrypted_text = decrypted_text.replace('R','w')
decrypted_text = decrypted_text.replace('L','k')
decrypted_text = decrypted_text.replace('F','y')
decrypted_text = decrypted_text.replace('Z','m')
decrypted_text = decrypted_text.replace('D','u')
decrypted_text = decrypted_text.replace('J','g')
decrypted_text = decrypted_text.replace('K','v')
decrypted_text = decrypted_text.replace('U','p')
decrypted_text = decrypted_text.replace('S','l')
decrypted_text = decrypted_text.replace('H','c')
decrypted_text = decrypted_text.replace('Y','x')
decrypted_text = decrypted_text.replace('B','q')
decrypted_text = decrypted_text.replace('E','j')



print("Encrypted Text: ", encrypted_text, "\n\n\n\n\n")
print("Decrypted Text: ", decrypted_text)


words = decrypted_text.split()
from collections import defaultdict

length_groups = defaultdict(list)
for word in words:
    length_groups[len(word)].append(word)

for length in sorted(length_groups):
    print(" ".join(length_groups[length]))



words_with_n = [word for word in words if 'E' in word]

words_with_n_sorted = sorted(words_with_n, key=len)

print("\nWords containing 'N':")
for word in words_with_n_sorted:
    print(word)

plot_frequencies(sorted_english_freq, sorted_cipher_freq)
