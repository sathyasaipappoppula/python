def sum_mat(mat1,mat2):
    mat3=[]
    for i in range(len(mat1)):
        l1=[]
        for j in range(len(mat1[0])):
            l1.append(mat1[i][j]+mat2[i][j])
        mat3.append(l1) 
    return mat3

mat1=[[1,2,3],[1,2,3],[1,2,3]]
mat2=[[1,2,3],[1,2,3],[1,2,3]]
if(len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0])):
    print(sum_mat(mat1,mat2))
else:
    print("matrix addition not possible")
