taxa_chegada = float(input('Requisições por segundo: '))
entry = float(input('entry: '))
home = float(input('home: '))
search = float(input('search: '))
add = float(input('add: '))
pay  = float(input('pay: '))

#taxa de chegada de requisições
t_entry = taxa_chegada*entry
t_home = taxa_chegada*home
t_search = taxa_chegada*search
t_add = taxa_chegada*add
t_pay = taxa_chegada*pay

print('Taxa de chegada por funções')
print('Entry', t_entry)
print('Home', t_home)
print('Search', t_search)
print('Add', t_add)
print('Pay', t_pay)

#utilizaçao cpu e disco
print('')
print('utilizaçao de cpu e disco')
print('')



UDisco_h = (t_home * 0.015) 
UDisco_s= (t_search * 0.025) 
UDisco_a= (t_add * 0.015) 
UDisco_p= (t_pay * 0.010)

print('Disco home ',UDisco_h)
print('Disco Search ', UDisco_s)
print('Disco add ',UDisco_a)
print('Disco pay ',UDisco_p)

UCPU_h = (taxa_chegada * 0.010)
UCPU_s = (taxa_chegada * 0.015)
UCPU_a = (taxa_chegada * 0.010)
UCPU_p = (taxa_chegada * 0.020)

print('Cpu home', UCPU_h)
print('Cpu search', UCPU_s)
print('Cpu add', UCPU_a)
print('Cpu pay', UCPU_p)

#tempo de residencia

print('')
print('Tempo de residencia')
print('')


Rdisco_h = 0.015 / (1 - UDisco_h)
Rdisco_s = 0.025 / (1 - UDisco_s)
Rdisco_a = 0.015 / (1 - UDisco_a)
Rdisco_p = 0.010 / (1 - UDisco_p)

Rcpu_h = 0.010 / (1 - UCPU_h)
Rcpu_s = 0.015 / (1 - UCPU_s)
Rcpu_a = 0.010 / (1 - UCPU_a)
Rcpu_p = 0.020 / (1 - UCPU_p)

print("Disco Home", Rdisco_h)
print("Disco Search", Rdisco_s)
print("Disco Add", Rdisco_a)
print("Disco Pay", Rdisco_p)
print("")

print("Cpu Home", Rcpu_h)
print("Cpu Search", Rcpu_s)
print("Cpu Add", Rcpu_a)
print("Cpu Pay", Rcpu_p)




# tempo de resposta
print('')
print('Tempo de resposta')
print('')
Tes_h = Rdisco_h+Rcpu_h
Tes_s = Rdisco_s+Rcpu_s
Tes_a = Rdisco_a+Rcpu_a
Tes_p = Rdisco_p+Rcpu_p

print('Home',Tes_h)
print('Search', Tes_s)
print('Add', Tes_a)
print('Pay', Tes_p)

