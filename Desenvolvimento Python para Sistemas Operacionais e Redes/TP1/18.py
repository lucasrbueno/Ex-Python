import psutil

print(f"Memória principal: {round(psutil.virtual_memory().total/(1024 * 1024 * 1024), 2)} GB")

print(f"Memória de paginação: {round(psutil.swap_memory().total/(1024 * 1024 * 1024), 2)} GB")