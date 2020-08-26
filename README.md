# gpu-burn
Multi-GPU CUDA stress test
http://wili.cc/blog/gpu-burn.html


### Build

```
make
```


### Run Test

```
time=100
name="$(hostname)"

./gpu_burn $time | tee "log/"$name".txt" 
```


### Gather temperature results

```
name="$(hostname)"
num_gpu="$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)"
cat "log/"$name".txt" | grep temps | tee "log/"$name"_temp.txt" 

python display_temp.py $name $num_gpu
```