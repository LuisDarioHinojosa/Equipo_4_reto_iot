# OXIMETRO_IOT
OXIMETRO para curar el covid (clase ITESM iot)
Luis Dario
Edgar Rostro
Jaime Emilio
Resetear Auto Increment de oxygen_meditions y hearbeat_meditions-> ALTER TABLE `table` AUTO_INCREMENT = 0;
# Busquedas hardcore ejemplos:
use iot_reto;
select persons.name, persons.birth_date, oxygen_meditions.oxygen_blood
from iot_reto.persons
JOIN iot_reto.oxygen_meditions
on iot_reto.persons.id_person = iot_reto.oxygen_meditions.id_person;

# 2 
select * from iot_reto.oxygen_meditions
where oxygen_meditions.oxygen_blood > 100
order by oxygen_meditions.rate_date ASC;