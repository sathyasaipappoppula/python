def is_identity(mat):
    rows=len(mat)
    columns=len(mat[0])
    if(rows!=columns):
         return False
    for i in range(rows):
        for j in range(columns):
            
                if(i==j and mat[i][j]!=1):
                    return False 
                elif(i!=j and mat[i][j]!=0):
                    return False 
                
    return True 
    
                
            

mat=[[1,0,0],[0,1,0],[1,0,1]]
print(is_identity(mat))