nascimento=input("escreva a sua data de nascimento dd/mm/aaaa:")
a=0
if nascimento[3:5]=="01":
    a=("janeiro")


if nascimento[3:5]=="02":
    a=("fevereiro")
if nascimento[3:5]=="03":
    a=("março")
if nascimento[3:5]=="04":
    a=("abril")
if nascimento[3:5]=="05":
    a=("maio")
if nascimento[3:5]=="06":
    a=("junho")
if nascimento[3:5]=="07":
    a=("julho")
if nascimento[3:5]=="08":
    a=("agosto")
if nascimento[3:5]=="09":
    a=("setembro")
if nascimento[3:5]=="10":
    a=("outubro")
if nascimento[3:5]=="11":
    a=("novembro")
if nascimento[3:5]=="12":
    a=("dezembro")
print("você nasceu em",nascimento[0:2],"e o mes e",a,"e o ano e",nascimento[6:10])
