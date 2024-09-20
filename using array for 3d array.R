vec1=c(1:9)
vec2=c(10,11,12)
arr=array(c(vec1,vec2))
arr
arr=array(c(vec1,vec2),dim =c(2,3,2))
arr
dim(arr)
row_names=c("r1","r2")
column_names=c("c1","c2","c3")
mat_names=c("mat1","mat2")
arr1=array(c(vec1,vec2),dim=c(2,3,2),dimnames= list(row_names,column_names,mat_names))
arr1
