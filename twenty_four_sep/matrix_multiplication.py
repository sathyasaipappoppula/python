def mat_mul(mat1,mat2):
    mat3=[]
    for i in range(len(mat1)):
        l1=[]
        for j in range(len(mat2[0])):
            sum=0 
            for k in range(len(mat2)):
                sum+=(mat1[i][k]*mat2[k][j])
            l1.append(sum) 
        mat3.append(l1) 
    return mat3
        
mat1=[[1,2,3],[1,2,3],[1,2,3]]
mat2=[[1,2,3],[1,2,3],[1,2,3]]
if(len(mat1[0])==len(mat2)):
    print(mat_mul(mat1,mat2))
else:
    print("matrix multiplication is not possible")