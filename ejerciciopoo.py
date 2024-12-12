# Clase Persona (Clase Padre)
class Persona:
    def __init__(self, nombre, apellidos, id_fiscal):
        self.nombre = nombre
        self.apellidos = apellidos
        self.__id_fiscal = id_fiscal  # id_fiscal es privado
    
    # Getter para id_fiscal
    @property
    def id_fiscal(self):
        return self.__id_fiscal
    
    # Método abstracto (no se implementa aquí, se implementará en las clases hijas)
    def saludar(self):
        raise NotImplementedError("Este método debe ser implementado en la clase hija")

# Clase Cliente (Clase Hija de Persona)
class Cliente(Persona):
    contador_clientes = 0  # Contador estático de clientes
    
    def __init__(self, nombre, apellidos, id_fiscal, id_cliente, email):
        super().__init__(nombre, apellidos, id_fiscal)
        self.id_cliente = id_cliente
        self.email = email
        Cliente.contador_clientes += 1  # Aumentamos el contador al crear un cliente
    
    # Getter para email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        self.__email = email
    
    # Método para saludar
    def saludar(self):
        return f"Hola, soy {self.nombre} {self.apellidos}, mi ID fiscal es {self.id_fiscal}."

    # Método estático para obtener el número de clientes creados
    @staticmethod
    def obtener_numero_clientes():
        return Cliente.contador_clientes
    
    # Método especial __str__ para representar al cliente como un string
    def __str__(self):
        return f"Cliente {self.nombre} {self.apellidos} (ID Cliente: {self.id_cliente}, Email: {self.email})"
    
    # Método especial __eq__ para comparar dos clientes por su id_fiscal
    def __eq__(self, other):
        if isinstance(other, Cliente):
            return self.id_fiscal == other.id_fiscal
        return False

# Clase Factura
class Factura:
    def __init__(self, id_factura, cliente):
        self.id_factura = id_factura
        self.cliente = cliente  # El cliente debe ser una instancia de la clase Cliente

    # Método especial __str__ para representar la factura como un string
    def __str__(self):
        return f"Factura ID: {self.id_factura}, Cliente: {self.cliente.nombre} {self.cliente.apellidos}"

# Ejemplo de uso
# Crear clientes
cliente1 = Cliente("Ana", "González", "12345678A", "C001", "ana@example.com")
cliente2 = Cliente("Juan", "Pérez", "87654321B", "C002", "juan@example.com")

# Saludar a un cliente
print(cliente1.saludar())

# Ver el número total de clientes
print(f"Número de clientes creados: {Cliente.obtener_numero_clientes()}")

# Mostrar los datos del cliente
print(cliente1)

# Comparar dos clientes
print(cliente1 == cliente2)  # False porque tienen diferentes id_fiscal

# Crear una factura
factura1 = Factura("F001", cliente1)

# Mostrar los datos de la factura
print(factura1)