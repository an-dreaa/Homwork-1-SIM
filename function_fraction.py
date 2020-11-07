# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:02:18 2019

@author: Andrea
"""

def add_frac(zaeler1, nenner1, zaeler2, nenner2):
   """Dieses Programm addiert 2 Brüche miteinander und kürzt sie mit ihrem größten gemeinsamen Teiler (ggt)"""

#Variablen einführen 
   zaeler=0
   nennerg=0
   ggt = 1

#überprüfen ob die Eingabe eine Ganzzahl ist   
   if not(isinstance(zaeler1,int) and isinstance(nenner1, int) and isinstance(zaeler2, int) and isinstance(nenner2, int)):
       print("Gib bitte nur ganze Zahlen ein")
       return 0

#neuen Nenner und neuen Zähler ausrechnen   
   else:  
       nennerg=nenner1*nenner2
       zaeler1neu=zaeler1*nenner2
       zaeler2neu=zaeler2*nenner1
       zaeler=zaeler1neu+zaeler2neu

      
       if zaeler<nennerg:
            maximum = zaeler
       else:
            maximum=nennerg
            
#ggt durch iterieren ermitteln        
       for i in range(1,maximum):
           ggt = maximum-i
           
           if (zaeler%ggt)==0 and (nennerg%ggt)==0:
                break
       
       return zaeler/ggt, nennerg/ggt
   



    
 