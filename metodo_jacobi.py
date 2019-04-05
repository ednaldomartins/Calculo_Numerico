#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:17:08 2019

@author: ednaldo
"""
from numpy import dot

A = [[ 0, 0, 2, 0, 0, 0, 0, 0],
     [ 0, 0, 0, 0, 0, 1, 0, 0],
     [ 0,-2, 0, 0, 0, 0, 0, 2],
     [ 0, 0, 0, 0, 1, 0, 0, 0],
     [-4,-4, 7, 4, 2, 3, 4, 1],
     [-1, 0, 2, 0, 0, 1, 2, 0],
     [-1, 0, 0, 1, 0, 0, 0, 0],
     [ 0,-1, 0,10, 0, 1, 0, 0]
     ]
b = [7, 66, 96, 42, 24, 0, 0, 0]
    
''' Métodos Auxiliares '''
def permutacao(A, tamanho):
    v, aux, verifica = [], [], []
    for i in range(tamanho): verifica.append(False)
    copia_A = A.copy()
    
    for i in range(tamanho):
        #procura linha a linha as equacoes em que a variavel eh diferente de 0
        for j in range(tamanho):
            if (A[j][i] != 0):
                #se for, entao guarde a posicao da equacao 
                aux.append(j)
        #agora guarde a posicao das equacoes em que a variavel exixste no 
        #vetor que irah guardar essa informacao de todas as variaveis
        v.append(aux)
        aux = []
    
    for i in range(tamanho):
        #o objetivo eh guardar a quantidade de equacoes disponiveis para cada
        #letra, e tambem guardar a letra que eh prioridade no momento
        #exemplo: prioridade = 2, entao prioriade é a letra 'c'
        qnt_equacoes = float('inf')
        prioridade = 0
        for i in range(tamanho):
            #verifica[i] para verificar se a letra atual ja tem uma equacao
            #selecionada para ela, e tambem se ela tem menos equacoes que 
            #a letra com maior prioridade no momento
            if verifica[i] != True and len(v[i]) < qnt_equacoes:
                #se true, entao guarde o numero de equacoes para essa letra
                #e tambem qual a posicao da letra. lembrando: 2='c', 3='d'...
                qnt_equacoes = len(v[i])
                prioridade = i
                
        #apos identificar quem tem maior prioridade, devemos pegar uma equacao
        #em que essa prioridade(letra) exista(fazemos isso atraves do vetor v
        #que guardou as equacoes disponiveis para cada letra), e atualizamos
        #a matriz A sem perder a original atraves da copia_A
        A[prioridade] = copia_A[v[prioridade][0]]
        #identificamos qual equacao serah removidade das equacoes disponiveis
        remover = v[prioridade][0]
        verifica[prioridade] = True
        #removemos a equacao separada para a letra, de todas as outras que 
        #tem ela como disponivel, para aumentar a prioridade de quem nao tem
        #mais essa equacao disponivel
        for j in range(tamanho):
            k = 0
            while k < len(v[j]):
                if verifica[j] != True and v[j][k] == remover :
                    v[j].pop(k) 
                    break
                k += 1
    return A

def chute_inicial(tamanho_A):
    x = []
    for i in range(tamanho_A): x.append(1)
    return x    
   
def diagonal(A):
    diagonal = []
    for i in range(len(A)): diagonal.append(A[i][i])
    return diagonal

def diagonal_zero(A):
    C = A.copy()
    for i in range(len(C)): C[i][i] = 0
    return C

def jacobi(A, b, n = 10, x = chute_inicial(len(A))):
    print ("\n\nx0: \n", x)
    #diagonal contem os valores que serao o divisor das equacoes
    d = diagonal(A)
    print ("\n\ndiagonal: \n", d)
    
    #criar C
    C = diagonal_zero(A)
    print ("\n\nC: \n", C)
    
    #iteracao
    for k in range (n):
        print('\nx'+str(k)+'\n', x)
        #substitui os valores de xk nas equacoes do sistema -C 
        x = (b - dot(C,x))/d
    print('\nx'+str(n)+'\n', x)
  
if __name__ == "__main__":

    tamanho_A = len(A)
    tamanho_b = len(b)
    print ("\n\nA: \n", A)
    print ("\n\nb: \n", b)
    
    #organizar matriz A
    A = permutacao(A, tamanho_A)   
    
    jacobi(A, b, 10)
    