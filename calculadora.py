#!/usr/bin/env python
# coding: utf-8

# In[1]:


#titulo da calculadora e textos

print("******************* Calculadora Python Diogo Martins *******************\n")


# In[2]:


#Definindo funções

def soma(x, y):
    return x + y
def subtração(x, y):
    return x - y
def divisão(x, y):
    return x / y
def multiplicação(x, y):
    return x * y 


# In[3]:


print("Selecione a opção desejada:\n")

print("1-Adição")
print('2-Subtração')
print("3-Divisão")
print('4-Multiplicação')


# In[5]:


escolha = input('Digite: 1 , 2 , 3 ou 4 : ')


# In[6]:


num1 = int(input('Digite o primeiro numero:\n'))
num2 = int(input('\nDigite o segundo numero:\n'))

if escolha == '1':
    print('\n')
    print(num1,'+',num2,'=', soma(num1,num2))
    print('\n')
elif escolha == '2':
    print('\n')
    print(num1,'-',num2,'=', subtração(num1,num2))
    print('\n')
elif escolha == '3':
    print('\n')
    print(num1,'/',num2,'=', divisão(num1,num2))
    print('\n')
elif escolha == '4':
    print('\n')
    print(num1,'*',num2,'=', multiplicação(num1,num2))
    print('\n')
else:
    print('Opção inválida!')


# In[ ]:





# In[ ]:




