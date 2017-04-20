
#!/bin/bash
mapfile -t n_array < names
mapfile -t p_array < passwords
for ((i=0;i<${#n_array[@]};++i)); do
    useradd ${n_array[i]}
    passwd ${n_array[i]}
    echo  ${p_array[i]}
done
