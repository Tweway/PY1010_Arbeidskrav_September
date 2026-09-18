Kilometer_i_året=10000
Dager_i_året=365
FG=7500 #som står for forsikring Golf
TG=8.38*Dager_i_året #som står for trafikkforsikringavgift Golf
DG=1.0*Kilometer_i_året #som står for drivstofbruk Golf
BG=0.3*Kilometer_i_året #som står for bompenger Golf
print("Årlig utgifter for Golf:",FG+TG+DG+BG,"kr") 

FT=5000 #som står for forsikring Tesla
TT=8.38*Dager_i_året #som står for trafikkforsikringavgift Tesla
DT=0.2*Kilometer_i_året*2.0 #som står for drivstofbruk Tesla i en formel som regner kWh, Km/år og lading
BT=0.3*Kilometer_i_året #som står for bompeenger Tesla
print("Årlig utgifter for Tesla:",FT+TT+DT+BT,"kr")

Golf_vs_Tesla=(FG+TG+DG+BG)-(FT+TT+DT+BT)
Tekst="""
Etter å ha sett disse tallene kan vi se at en Golf vil koste oss """ + str(Golf_vs_Tesla)+ """ kr,- mer enn hva en Tesla vil i året, 
dermed er årlig kosnadsdifferansen mellom en Golf og en Tesla """ +str(Golf_vs_Tesla)+ """ kr,- Dette betyr at det er mer økonomisk å eie en Tesla enn en Golf, 
spesielt hvis man kjører mye i løpet av året. Dette var bare et eksempel med """ +str(Kilometer_i_året)+ """ km i året. I tillegg til de økonomiske fordelene, 
har elbiler også miljømessige fordeler som reduserte utslipp og mindre støyforurensning.
"""
print(Tekst)

#Oppgave "Tekst" som jeg har laget er koblet opp med alle tallene som en type kalkulator. Som gjør at hvis jeg endrer "kilometer_i_året", 
#eller noen av de andre verdiene som ladepris eller forsikringspris osv. så vil teksten i sin helhet endres og kunne gi nye utregnet svar:D 
