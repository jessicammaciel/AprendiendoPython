#MEDIA DE NOTAS

n1 = float(input('Primera Evaluación: '))
n2 = float(input('Segunda Evaluación: '))

media = (n1+n2)/2

if media < 5:
    print('Su media es de {:.2f}, HAS SUSPENDIDO!'.format(media))
elif media >=5 and media < 7:
    print('Su media es de {:.2f}, A RECUPERAR EN JUNIO'.format(media))
else:
    print('Sua média é {:.2f}, HAS APROBADO'.format(media))