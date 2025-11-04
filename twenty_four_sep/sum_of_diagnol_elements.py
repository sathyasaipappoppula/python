def sum_diagnol_mat(mat1,mat2):
    l1=[]
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            if(i==j):
                l1.append(mat1[i][j]+mat2[i][j])
    return l1

mat1=[[1,2,3],[1,2,3],[1,2,3]]
mat2=[[1,2,3],[1,2,3],[1,2,3]]
if(len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0])):
    print(sum_diagnol_mat(mat1,mat2))
else:
    print("matrix addition is not possible")
