from matriz import escribirMatriz

def indicadoresV0(matrizAsignacion, matrizRegistro):
    # Se almacena los valores Cantidad,	Eficiencia,	Tasa de entrega y Nivel Cumplimiento
    matrizEficCamion = [
        [1,0,0,0,0],
        [2,0,0,0,0],
        [3,0,0,0,0],
        [4,0,0,0,0],
        [5,0,0,0,0]
    ]

    for i in range(len(matrizAsignacion)):

        if matrizAsignacion[i][2] > 0 and matrizAsignacion[i][3] > 0 and matrizRegistro[i][2] > 0 and matrizRegistro[i][3] > 0:
            #Ind. 1 - Eficiencia en tiempos de despacho = 
            # (Tiempo de despacho asignado - Tiempo de despacho registrado) 
            # / Tiempo de despacho asignado x 100	
            eficiencia = (( matrizAsignacion[i][2] - matrizRegistro[i][2] ) / matrizAsignacion[i][2] ) * 100

            # Ind. 2 - Tasa de entrega (Lt/min) = 
            # Cantidad de litros despachados / Tiempo total de despacho x100	
            tasaEntrega = ( matrizRegistro[i][3] / matrizRegistro[i][2] ) * 100

            # Ind. 3 - Nivel de Cumplimiento de los despachos = 
            # Litros despachados / Total de litros asignados x 100
            cumplimiento = ( matrizRegistro[i][3] / matrizAsignacion[i][3] ) * 100

            for j in range(len(matrizEficCamion)):
                if matrizAsignacion[i][1] == matrizEficCamion[j][0]:
                    matrizEficCamion[j][1] = matrizEficCamion[j][1] + 1 # cantidad de viajes
                    matrizEficCamion[j][2] = matrizEficCamion[j][2] + eficiencia  # acumular eficiencia
                    matrizEficCamion[j][3] = matrizEficCamion[j][3] + tasaEntrega # acumular tasa
                    matrizEficCamion[j][4] = matrizEficCamion[j][4] + cumplimiento # acumular cumplimiento
        else:
            print("¡Error, no debe tener valores menores de 1!")

    
    # Calcular promedio:
    for i in range(len(matrizEficCamion)):        
        matrizEficCamion[i][2] = matrizEficCamion[i][2] / matrizEficCamion[i][1]
        matrizEficCamion[i][3] = matrizEficCamion[i][3] / matrizEficCamion[i][1]
        matrizEficCamion[i][4] = matrizEficCamion[i][4] / matrizEficCamion[i][1]
    
    escribirMatriz(matrizEficCamion)
            





if __name__ == "__main__": 
    matrizAsignacion= [[1,5,1329,10], [2,4,2,35], [3,1,1462,54], [4,3,1222,35], [5,2,2000,44],[6,3,1389,52], [7,1,1500,35],
    [8,1,1419,50], [9,5,1355,44], [10,4,1000,36]]

    matrizDespachos=  [[1,5,1168,52], [2,4,1224,51], [3,1,1379,33], [4,3,1281,52], [5,2,1200,38], [6,3,1320,34],
    [7,1,1225,52], [8,1,1149,51], [9,5,1424,34], [10,4,1000,36]]
   
    indicadoresV0(matrizAsignacion,matrizDespachos)

  