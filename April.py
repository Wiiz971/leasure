# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:47:30 2019

@author: El Zorro
"""

import random
import numpy as np

# a partir une liste de nombre, on souhaite retourner une liste correspondant a des nombres aléatoies 
def yannick(L):
    M=[]
    for i in L:
        N=[]
        if i==L[0]:
            for h in range(i):
                q = random.randint(0,14)
                if q not in N:
                    N.append(q)
            M=M+[N]
            continue
        for k in range(i):
            x=0
            while x==0:
                q = random.randint(0,14)
                for b in range(len(M)):
                    if q in N or q in M[b]:
                        x=0
                        break
                    else:
                        x=1
                if x==1:
                    N.append(q)
        M=M+[N]
    return M

def yakari(m,n): # m lignes et n colonnes
    M=[[random.randint(0,99) for i in range(n)]for j in range(m)]
    Somme=[]
    mini,maxi=M[0][0],M[-1][-1]
    for i in M:
        s=0
        for j in i:
            s+=j
            if j<mini:
                mini=j
            if j>maxi:
                maxi=j
        Somme+=[s]
    L=''
    for i in range(m):
        L1=' la somme de la %s e ligne fait :'%(i+1)
        L+=L1+' %s'%Somme[i]+','
    return np.array(M),L,'le plus petit nombre est : %s'%mini,'le plus grand nombre est : %s'%maxi
 
#On veut une fonction qui genere une pyramide d'* a partir d'une nombre d'etage donné      
"""    
    *              
   * *
  * * *
 * * * *
* * * * *       
"""
def pyramide(n):
    L=' '.join(['*'*i for i in range(n+1,1,-1)])  
    L1 =L.split(' ')
    print(L1)
    S=[]
    j=0
    for i in L1:
        S=[' ']*j
        for char in i:
            S+=['%s '%char ]
        j+=1
        i=S
        S=[]
    return L1

def add(L):
    new=[]
    for i in L:
        if i==L[0]:
            new.append(i)
            continue
        a = i+new[-1]
        new.append(a)
    return new


#Faire une fonction qui renvoie la date de ton anniversaire a partir de l'agument l'année        
def bissec(annee):
    if annee%4==0 and annee%100!=0 or annee%400==0:
        return 1
    else:
        return -1
    
dref = "lundi 08 Avril 2019"
import datetime
def yanis():
    semaine = ['Lundi' 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi','Samedi', 'Dimanche']
    mois = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', ' Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    birthday = input('votre date d anniversaire sous la forme (dd/mm/yyyy) : ')
    annee = input('Quelle année souhaitez vous connaitre ?:')
    Ydaten = int(annee)
    if Ydaten < int(birthday[-4:]):
        return ('impossible de revenir dans le passé !')
    if Ydaten == int(birthday[-4:]):    
        anni = datetime.datetime(int(birthday[-4:]),int(birthday[-7:-5]),int(birthday[:-8])).weekday()
        return( 'Vous êtes nés le %s %s %s %s'%(semaine[anni-1],birthday[:-8],mois[int(birthday[-7:-5])-1], Ydaten ))      
    anniv = datetime.datetime(int(birthday[-4:]),int(birthday[-7:-5]),int(birthday[:-8])).weekday()
    a=0
    annee_anniv = birthday[-4:]
    for i in range(int(annee_anniv) +1,Ydaten):
        if bissec(i)==1:
            a+=2
        else:
            a+=1
    b = (anniv+a)%7
    return( 'Votre anniversaire tombera le %s %s %s %s'%(semaine[b],birthday[:-8],mois[int(birthday[-7:-5])-1], annee ))      
    
def yanis_bis():
    semaine = ['Lundi' 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi','Samedi', 'Dimanche']
    mois = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', ' Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    birthday = input('votre date d anniversaire sous la forme (dd/mm/yyyy) : ')
    annee = input('A quel age souhaitez-vous savor la date ?: ')
    Ydaten = int(birthday[-4:])+int(annee)
    anniv = datetime.datetime(int(birthday[-4:]),int(birthday[-7:-5]),int(birthday[:-8])).weekday()
    a=0
    annee_anniv = birthday[-4:]
    for i in range(int(annee_anniv) +1,Ydaten):
        if bissec(i)==1:
            a+=2
        else:
            a+=1
    b = (anniv+a)%7
    return( 'Votre anniversaire tombera le %s %s %s %s'%(semaine[b],birthday[:-8],mois[int(birthday[-7:-5])-1], Ydaten ))      
    
from bs4 import BeautifulSoup
import urllib3
import re
    
def distance_ville():
    def divEuclid(a,b):
        def divEuclid2(q,r):
            if b*q>a:
                return(q-1,a-b*(q-1))
            else:
                return divEuclid2(q+1,r)
        if a<b:
            return divEuclid(b,a)
        return divEuclid2(0,0)
    def day(h):
        q1,r = divEuclid(h,24)
        heure = int(r)
        minutes = r - heure
        return[q1,heure,int(minutes*60)]
    depart = input('Entrez la ville de depart : ')
    arrive = input("Entrer la ville d'arrivé : ")
    url = 'http://www.distance2villes.com/recherche?source=%s&destination=%s'%(depart, arrive)
    htt = urllib3.PoolManager()
    data = htt.request('GET', url)
    page = data.data.decode('utf-8')[2:]
    soup = BeautifulSoup(page, 'lxml')
    a = soup.find_all('strong', id="distanciaRuta")
    M = str(a[0])
    L = re.sub('<[^<]+?>', '',M)
    distance = int(L[:-3])
    velo,voiture,pied = distance/16,distance/110,distance/2.5
    L0 = [velo,voiture,pied]
    PO=[]
    for i in range(2):
        PO+= [day(L0[i])]
    print(PO)
    for i in PO:
        i[0]='%s jours'%i[0]
        i[1]='%s heures'%i[1]
        i[2]='%s minutes'%i[2]
    velo = ' '.join([i for i in PO[0]])
    voiture = ' '.join([i for i in PO[1]])
    #pied = ' '.join([i for i in PO[2]])        
    return 'Il y a %s entre ces deux villes, temps : velo (16km/h) = %s , voiture(110 km/h) = %s '%(L, velo, voiture)#, a pied = %s , pied)

""" calcul de moyenne"""
def valeur_moyenne(mesures):
    somme = (mesures[0]+mesures[-1])/2
    for i in range (1,len(mesures)-1):
        somme+=mesures[i]
    return somme/(len(mesures)-1)

""" 
créer une liste de nombres entiers aléatoires unique avec python
"""
def liste(a,b,n):
    return random.sample(range(a,b),n)
    

    
