segundos_str = input("Por favor, entre com o numero de segundos que deseja converter:")
total_segs = int(segundos_str)

a = total_segs//86400
segs_restantes01 = total_segs% 86400
b = segs_restantes01//3600
segs_restantes02 = total_segs% 3600
c = segs_restantes02//60
d = segs_restantes02%60

print(a,"dias,",b,"horas,",c,"minutos e", d,"segundos.")
