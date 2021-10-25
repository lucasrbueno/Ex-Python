import psutil

uso_disco = psutil.disk_usage(path=psutil.disk_partitions()[0][0])

print(f"Espaço livre do disco: {round(uso_disco[2] / (1024 * 1024 * 1024), 2)} GB")