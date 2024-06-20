#
# Importar bibliotecas
#
import sys
from sys import argv
import math

#
# Tipos de erros que podem ocorrer
# -1 -> numero de parametros menor do que 8
# -2 -> se algum dado estiver fora do limite esperado
# -3 -> se houver algum digito nao numerico
# -4 ->  numero de parametros maior do que 8
# -5 ->  algum erro inesperado
#
# Para executar este sistema, basta fazer tal como o exemplo
# python3 predBicudo.py  3.77  7.81  82.77  4.21  11.05  5.516857  11.28 2
# python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3
#
#
# Ler os dados de entrada e verificar se existem dados invalidos
#
n = len(sys.argv[1:])

if( n < 8): # o numero de parametros eh 7. Foram passados menos parametros
  print('codigo -1')
  print('numero de parametros menor do que 8.')
  print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
  print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
  sys.exit(0)

if( n > 8): # o numero de parametros eh 7. Foram passados mais parametros
  print('codigo -4')
  print('numero de parametros maior do que 8.')
  print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
  print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
  sys.exit(0)

for value in sys.argv[1:]:
   try:
      arg = float(value)
   except:
      print('codigo -3')
      print('Existe algum digito nao numerico.')
      print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
      print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
      sys.exit(0)

   if math.isnan(arg):
     print('codigo -3')
     print('Existe algum digito nao numerico.')
     print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
     print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
     sys.exit(0)

#
# Verificar se os parametros esto dentro dos
# limites permitidos
#

radSolar = float(sys.argv[0:][1])
precipt = float(sys.argv[0:][2])
ur = float(sys.argv[0:][3])
temp = float(sys.argv[0:][4])
vv = float(sys.argv[0:][5])
eto = float(sys.argv[0:][6])
torv = float(sys.argv[0:][7])
mes = float(sys.argv[0:][8])

if precipt < 0 or precipt > 100:
   print('codigo -2')
   print('O valor da precipitacao esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

if radSolar < 0 or radSolar > 1000:
   print('codigo -2')
   print('O valor da radiacao solar esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

if ur < 0 or ur > 100:
   print('codigo -2')
   print('O valor da umidade relativa do ar esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

if temp < -20 or temp > 60:
   print('codigo -2')
   print('O valor da temperatura do ar esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

if vv  < 0 or vv > 100:
   print('codigo -2')
   print('O valor da velocidade do vento esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

if eto < 0 or eto > 1000:
   print('codigo -2')
   print('O valor da evapotranspiracao esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

if torv < -40 or torv > 80:
   print('codigo -2')
   print('O valor da temperatura de orvalho esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

if mes < 0 or mes > 12:
   print('codigo -2')
   print('O valor d0 mes esta fora do limite previsto.')
   print('Exemplo de execucao: python3 predBicudo.py  15.32  1.64  82.75  2.57  7.67  2.9399768762287  20.32 3')
   print('python3 predBicudo.py <radiacao solar> <precipitacao> <umidade relativa> <temperatura do ar> <velocidade do vento> <evapotranspiracao> <temperatura de orvalho> <numero do mes, 1 a 12> ')
   sys.exit(0)

#
# Executar o modelo
#
 
      

mes1 = 0
mes2 = 0
mes3 = 0
mes4 = 0
mes5 = 0
mes6 = 0
mes7 = 0
mes8 = 0
mes9 = 0
mes10 = 0
mes11 = 0
mes12 = 0
 

if(mes == 1):  
      mes1 = 1
else:
      if(mes == 2):  
         mes2 = 1
      else:
        if(mes == 3):  
             mes3 = 1
        else:
          if(mes == 4):  
             mes4 = 1
          else:
            if(mes == 5):  
               mes5 = 1
            else:
              if(mes == 6):  
                 mes6 = 1
              else:
                if(mes == 7):  
                    mes7 = 1
                else:
                  if(mes == 8):  
                     mes8 = 1
                  else:
                    if(mes == 9):  
                       mes9 = 1
                    else:
                      if(mes == 10):  
                         mes10 = 1
                      else:
                        if(mes == 11):  
                           mes11 = 1
                        else:
                          if(mes == 12):  
                              mes12 = 1



if ( ur < 42.97 ):

      if(temp < 26.3): 
          print ("muito baixa")
      
      else:
            if(mes10 < 0.5):

               if(mes9 < 0.5):
                               if(temp < 26.61):
                                                print ("muito baixa")
                               else:
                                                print ("baixa")
                
               else:
                               if(temp < 29.08 ):
                                                print ("muito baixa")
                               else:
                                      if( precipt < 0.55):
                                                print ("muito alta")
                                      else:
                                                print ("muito baixa")
                   
            
            else:
                print ("muito baixa")
 
else :
           if(vv < 2.34):
                  print ("muito baixa")
           else:
                 if(ur < 53.06):
                                         if( vv < 3.45):
                                                print ("muito alta")
 
                                         else:
                                                if(temp < 21.19):
                                                     print ("muito alta")
                                                else:
                                                     print ("muito baixa")
 
                 else:
                        if(temp < 22.71):
                           print ("muito alta")
                        else:
                           print ("muito baixa")
 
print ("\n")

