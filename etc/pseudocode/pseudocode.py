dataset_small_samples_total = 5000 - 2 * 625
N_min = 1
ds_samples_total = 9504 * 9


def get_all_divisors_less_than(k_max, n):
    return sorted(
        set(
            [
                i
                for d in (
                    [i]
                    for i in range(1, min(int(k_max**0.5) + 1, n + 1))
                    if k_max % i == 0
                )
                for i in d
            ]
        ),
        reverse=True,
    )


# Najveca podjela
k_max = ds_samples_total // dataset_small_samples_total

K = get_all_divisors_less_than(ds_samples_total, k_max)

iterations_max = N_min * K[0]

print(f"k_max = round({ds_samples_total} / {dataset_small_samples_total}) = {k_max}")
print(f"Factors of {ds_samples_total}, <= {k_max} = |{len(K)}|:\t", K, "\n")
for k in K:
    print(f"""\
    k = {k} => {k} x {ds_samples_total//k} = {k*(ds_samples_total//k)}\
    Iterations: {(N_min*K[0])//k} Remainder runs: {(N_min*K[0])%k}\
    """)

for iteration in range(iterations_max):
    print(f"Iteration {iteration}")
    for partition_count in K:
        samples_per_subset = ds_samples_total // partition_count

        real_partition_count = 0
        i_k = iterations_max // partition_count
        
        if iteration < i_k:
            real_partition_count = partition_count
        elif iteration == i_k and iterations_max % partition_count:
            real_partition_count = iterations_max % partition_count
        else:
            continue



        # Može i ovako ali real_partition_count će biti 0 u nekim slučajevima pa ne tribamo else 
        
        # real_partition_count = 0
        # if iteration < i_k:
        #     real_partition_count = partition_count
        # elif iteration == i_k:
        #     real_partition_count = iterations_max % partition_count

        

        print("[", end="")
        for partition in range(real_partition_count):
            print(
                f" {partition+1}/{partition_count}",
                end="",
            )

        print(" ]")
    print()
