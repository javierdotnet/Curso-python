 # PEMDAS 
 Orden de las operaciones

Cuando realiza operaciones aritméticas hay exactamente una respuesta correcta. Para evitar confusiones, los matemáticos han ideado un order estándar de operaciones para los cálculos que involucran más de una operación aritmética.

      1 er : Realice cualquier calculo dentro de los p aréntesis, realizando primero los más internos.

      2 do : Simplifique cualesquiera expresiones e xponenciales.

      3 er : Trabaje todas las m ultiplicaciones y d ivisiones, de izquierda a derecha, como aparezcan.

      4 to : Trabajes todas las s umas y r estas, de izquierda a derecha, como aparezcan.    

Para que no se confunda recuerde el PEMDAS que es la abreviatura para Parentheses (Paréntesis), Exponents (Exponentes) , Multiplication-Division (Multiplicación-División), Addition-Subtraction (Suma y resta). 




2**3 = 8 . 2 potencia 3 = 2*2*2 = 8


# Funciones desde la consola de Python
```
>>> dir(10)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> nombre='javier'
>>> dir(nombre)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> esUnico=False
>>> dir(esUnico)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>>


```



# Virtualenv

* pip3 install virtualenv
  - virtualenv venv --> crea un entorno virtual 
  - virtualenv --python=python2.7 venv
  - source venv/bin/activate
  - pip freeze ( para ver lo que tenemos instalado )




# Git 
  Borrar git rm -r --cached "directorio" -> Borra un directorio de git 

     * Ver rama :
         git branch
     * Crear rama :
            git branch apps
     * Cambiar de rama :
            git checkout apps

      * Ver estado :
            git status

      * Hacer commit y subir :
            git commit -am 'mensaje'
      * Fusionar una rama:
        git checkout master 
        git merge "nombrerama" -m "union de apps a master"

      Primero hacer "fetch"