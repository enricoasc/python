codigo = 10
salario = 1500.00
nome = 'Jose'
situacao = True

tipo = type(salario )

print(salario)
print(tipo)

print('Codigo: ',codigo,' Nome: ',nome,' O salario atual é de :',salario)
print('Código: '+str(codigo)+' Nome: '+nome+' O salário atual é de : '+str(salario))

# ------------------------------------------------------------------------------

# Máscara	        Tipo de             Descrição
# %d ou %i	        Int (inteiro)	    Exibe um valor inteiro.
# %f	            Float ou double	    Exibe um valor decimal.
# %ld	            Long Int	        Exibe um número inteiro longo.
# %e ou %E	        Float e double	    Exibe um número exponencial (número científico).
# %c	            Char (caractere)	Exibe um caractere.
# %o	            Int	                Exibe um número inteiro em formato octal.
# %x ou %X	        Int	                Exibe um número inteiro no formato hexadecimal.
# %s	            Char	            Exibe uma cadeia de caracteres (string).
# %r	            Boolean	            Exibe true ou false (verdadeiro ou falso).

# ------------------------------------------------------------------------------
print('Código : %d' %codigo )
print('Nome: %s' %nome)
print('Salario : %.2f' %salario)
print('Status : %r' %situacao)

# Enrico