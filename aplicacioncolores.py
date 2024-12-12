from colores import messageFormatter

print(messageFormatter("Esto es un error", "error"))
print(messageFormatter("Esto es un éxito", "success"))
print(messageFormatter("Esto es una advertencia", "warning"))
print(messageFormatter("Esto es un dato", "info"))
print("Esto no tiene formato")