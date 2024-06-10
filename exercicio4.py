def possivel(x1,y1,x2,y2):
   
   m1 = (x1+2 , y1+1)
   m2 = (x1+1 , y1+2)
   m3 = (x1-1 , y1+2)
   m4 = (x1-2 , y1+1)
   m5 = (x1-2 , y1-1) 
   m6 = (x1-1 , y1-2)
   m7 = (x1+1 , y1-2) 
   m8 = (x1+2 , y1-1)

   if x2>=1 and x2<=8 and y2>=1 and y2<=8:
      pos = (x2,y2)

      if m1 == pos : return True
      elif m2 == pos : return True
      elif m3 == pos : return True
      elif m4 == pos : return True
      elif m4 == pos : return True
      elif m5 == pos : return True
      elif m6 == pos : return True
      elif m7 == pos : return True
      elif m8 == pos : return True
      else : return False 

   else : return False