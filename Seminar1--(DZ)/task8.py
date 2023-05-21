#Требуется определить, можно ли от шоколадки 
#размером n × m долек отломить ровно k долек, 
#если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).
    #*Пример:*
    #3 2 4 -> yes   
    #3 2 1 -> no

slicesLength = int(input('Введите длину шоколадки: '))
slicesWidth = int(input('Введите ширину шоколадки: '))
itogSlices= slicesLength * slicesWidth
print (itogSlices)
needAslice = int(input('Введите сколько необходимо отломить долек от шоколадки: '))
if (needAslice > itogSlices): print ('много хочешь, просите меньше')
else: 
    if ((itogSlices - needAslice)% slicesLength == 0) or ((itogSlices - needAslice)%slicesWidth == 0):
        print ('    Да, можно отломить ровненько :)')
    else: print ('    Ровненько отломить не получится :((( ')
