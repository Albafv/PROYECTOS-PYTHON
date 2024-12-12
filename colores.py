# Formatea el texto en cuatro estilos
def messageFormatter(texto, tipo):
    if (tipo == 'info'):
        return '\033[34m' + ' ' + texto + ' ' + '\033[0m'
    elif (tipo == 'warning'):
        return '\033[33m' + ' ' + texto + ' ' + '\033[0m'
    elif (tipo == 'error'):
        return '\033[31m' + ' ' + texto + ' ' + '\033[0m'
    elif (tipo == 'success'):
        return '\033[32m' + ' ' + texto + ' ' + '\033[0m'
    else:
        return '\033[0m' + ' ' + texto + ' ' + '\033[0m'
