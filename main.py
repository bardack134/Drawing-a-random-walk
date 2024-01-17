# Importa las clases Turtle y Screen, y las funciones forward, onkeypress y setheading del módulo turtle
from turtle import Turtle, Screen, forward, onkeypress, setheading

# Importa el módulo random para generar números aleatorios
import random



#TODO:random color
# Esta función cambia el color de una tortuga de forma aleatoria
def change_color(turtle):
    
    # Genera un número aleatorio entre 0 y 1 para la componente roja del color
    R=random.random()   
    
    # Genera un número aleatorio entre 0 y 1 para la componente azul del color
    B=random.random()
    
    # Genera un número aleatorio entre 0 y 1 para la componente verde del color
    G=random.random()
    
    # Asigna el color generado a la tortuga usando el método color
    turtle.color(R,G,B)
    
    
#TODO: random walk
# Esta función hace que una tortuga se mueva de forma aleatoria
def random_walk(turtle):
    # Crea una lista con las posibles direcciones de movimiento
    walk=['forward', 'backward', 'left', 'right']

    # Elige una dirección al azar de la lista
    direccion=random.choice(walk)
    
    # Si la dirección es forward, avanza la tortuga 30 unidades
    if direccion == 'forward':
        
        turtle.forward(30)

    # Si la dirección es backward, retrocede la tortuga 30 unidades
    elif direccion == 'backward':
        
        turtle.backward(30)
        
    # Si la dirección es left, gira la tortuga 90 grados a la izquierda
    elif direccion == 'left':
        
        turtle.left(90)
        
    # Si la dirección es right, gira la tortuga 90 grados a la derecha
    elif direccion == 'right':
        
        turtle.right(90)
        
        


# Crea un objeto de la clase Turtle
turtle=Turtle()

# Cambia la forma de la tortuga a un círculo
turtle.shape("circle")


#TODO: aumentar el  grosor de la flecha 
# Aumenta el grosor del trazo de la tortuga a 15 unidades
turtle.pensize(15)


#TODO: aumentar la velocidad
# Aumenta la velocidad de la tortuga a la máxima posible
turtle.speed("fast")



# Repite 500 veces el siguiente bloque de código
for i in range(500):
    # Llama a la función change_color para cambiar el color de la tortuga
    change_color(turtle)
    
    # Llama a la función random_walk para mover la tortuga de forma aleatoria
    random_walk(turtle)






# Permite que el programa continue corriendo hasta que hagamos click en la pantalla , debemos crear un objeto de la clase Screen() para usar el metodo exitonclick()
# Debe ir al final de nuestro codigo
# Crea un objeto de la clase Screen
my_screen =Screen()

# Activa la escucha de eventos del teclado y el ratón
my_screen.listen()

# Cierra la ventana al hacer click en la pantalla
my_screen.exitonclick()
