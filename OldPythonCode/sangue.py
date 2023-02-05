entrada = input()
total = 0
entradaString = entrada.split(" ")
numeros = [int(numero) for numero in entradaString]
on, op, an, ap, bn, bp, abn, abp = numeros
entradaPacientes = input()
pacientesString = entradaPacientes.split(" ")
pacientes = [int(pacNum) for pacNum in pacientesString]
pon, pop, pan, pap, pbn, pbp, pabn, pabp = pacientes
if on < pon:
    pon = on
    on = 0
    v1 = pon
if on >= pon:
    on -= pon
    v1 = pon
if op < pop:
    pop -= op
    v2 = op
    op = 0
    
    if on != 0 and on < pop:
        pop -= on
        on = 0
        v2 += pop
    if on != 0 and on >= pop:
        on -= pop
        v2 += pop
        
if op >= pop:
    op -= pop
    v2 = pop
    
if an < pan:
    pan -= an
    v3 = an
    an = 0
    if on != 0 and on < pan:
        v3 += on
        pan -= on
        on = 0
    if on != 0 and on >= pan:
        v3+= pan
        on -= pan
if an >= pan:
    an -= pan
    v3 = pan

if ap < pap:
    pap -= ap
    v4 = ap
    ap = 0
    if an != 0 and an < pap:
         v4 += an
         pap -= an
         an = 0
    if an != 0 and an >= pap:
         an -= pap
         v4 += pap
         if op != 0 and op < pap:
             v4 += op
             pap -= op
             op =0
         if op != 0 and op >= pap:
             v4 += pap
             op -= pap
             if on != 0 and on < pap:
                 v4 += on
                 pap -= on
                 on = 0
             if on != 0 and on >= pap:
                 v4 += pap
                 on -= pap
if ap >= pap:
    ap -= pap
    v4 = pap

if bn < pbn:
    pbn -= bn
    v5 = bn
    bn = 0
    if on != 0 and on < pbn:
        pbn -= on
        v5 += on
        on = 0
    if on != 0 and on >= pbn:
        on -= pbn
        v5 += pbn
if bn >= pbn:
    bn -= pbn
    v5 = pbn
    
if bp < pbp:
    pbp -= bp
    v6 = bp
    bp = 0
    if bn != 0 and bn < pbp:
        pbp -= bn
        v6 += bn
        bn = 0
    if bn != 0 and bn >= pbp:
        bn -= pbp
        v6 += pbp
if bp >= pbp:
    bp -= pbp
    v6 = pbp
    
if abn < pabn:
    pabn -= abn
    v7 = abn
    abn = 0
    if bn != 0 and bn < pabn:
        pabn -= bn
        v7 += bn
        bn = 0
    if bn != 0 and bn >= pabn:
        bn -= pabn
        v7 += pabn
        if an != 0 and an < pabn:
            pabn -= an
            v7 += an
            an = 0
        if an != 0 and an >= pabn:
            an -= pabn
            v7 += pabn
            if on != 0 and on < pabn:
                pabn -= on
                v7 += on
                on =0
            if on != 0 and on >= pabn:
                on -= pabn
                v7 += pabn

if abn >= pabn:
    abn -= pabn
    v7 = pabn

if abp < pabp:
    pabp -= abp
    v8 = abp
    abp = 0
    if abn != 0 and abn < pabp:
        pabp -= abn
        v8 += abn
        abn = 0
    if abn != 0 and abn >= pabp:
        abn -= pabp
        v8 += pabp
        if bp != 0 and bp < pabp:
            pabp -= bp
            v8 += bp
            bp = 0
        if bp != 0 and bp >= pabp:
            bp -= pabp
            v8 += pabp
            
            if bn != 0 and bn < pabp:
                pabp -= bn
                v8 += bn
                bn = 0
            if bn != 0 and bn >= pabp:
                bn -= pabp
                v8 += pabp
                if ap != 0 and ap < pabp:
                    pabp -= ap
                    v8 += ap
                    ap = 0
                if ap != 0 and ap >= pabp:
                    ap -= pabp
                    v8 += pabp
                    if an != 0 and an < pabp:
                        pabp -= an
                        v8 += an
                        an = 0
                    if an != 0 and an >= pabp:
                        an -= pabp
                        v8 += pabp
                        if op != 0 and op < pabp:
                            pabp -= op
                            v8 += op
                            op = 0
                        if op != 0 and op >= pabp:
                            op -= pabp
                            v8 += pabp
                            if on != 0 and on < pabp:
                                pabp -= on
                                v8 += on
                                on = 0
                            if on  != 0 and on >= pabp:
                                on -= pabp
                                v8 += on
if abp >= pabp:
    abp -= pabp
    v8 = pabp
total = (v1+v2+v3+v4+v5+v6+v7+v8)  
print(total)              