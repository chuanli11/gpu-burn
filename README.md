# gpu-burn
Multi-GPU CUDA stress test
http://wili.cc/blog/gpu-burn.html


### Build

```
sudo apt install stress
sudo apt install lm-sensors

make
```

### Run Test (GPU only)
```
time=20
name="$(hostname)"

num_gpu="$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)"

./gpu_burn $time | tee "log/"$name".txt"
```

### Run Test (GPU and CPU)

```
time=20
name="$(hostname)"

num_gpu="$(nvidia-smi --query-gpu=name --format=csv,noheader | wc -l)"
num_cpu="$(nproc --all)"

./gpu_burn $time | tee "log/"$name".txt" & stress -c $num_cpu --timeout ${time}s & ./log_cpu_temp.sh $time $name
```

### Gather temperature results

```
cat "log/"$name".txt" | grep temps | tee "log/"$name"_gpu_temp.txt" 

python display_temp.py $name $num_gpu
```
