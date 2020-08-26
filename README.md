# gpu-burn
Multi-GPU CUDA stress test
http://wili.cc/blog/gpu-burn.html


### Build

```

make
```


### Run Test

```
time=20
name="$(hostname)"

num_gpu="$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)"
num_cpu="$(nproc --all)"

./gpu_burn $time | tee "log/"$name".txt" & stress -c $num_cpu --timeout ${time}s & ./log_cpu_temp.sh $time $name


cat "log/"$name".txt" | grep temps | tee "log/"$name"_gpu_temp.txt" 
```


### Gather temperature results

```
python display_temp.py $name $num_gpu
```