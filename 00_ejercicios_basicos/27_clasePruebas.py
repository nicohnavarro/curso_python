def compruebaMail(mailUsuario):
    """
    La Funcion compurebaMail evalua un mail
    recibido en busca de la @. Si tiene una @
    es correcto, si tiene mas de una @ es incorrecto
    si la @ esta al final es incorrecto

    >>> compruebaMail('juan@cursos.com')
    True

    >>> compruebaMail('juancursos.com@')
    False

    >>> compruebaMail('juancursos.com')
    False

    >>> compruebaMail('juan@cursos@.com')
    False

    """
    arroba=mailUsuario.count('@')
    if(arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1)or mailUsuario.find('@')==0):
        return False
    else:
        return True

import doctest
doctest.testmod()