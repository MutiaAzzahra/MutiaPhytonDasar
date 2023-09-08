import turtle

# Fungsi rekursif untuk menggambar pohon Fibonacci
def fibonacci_tree(t, branch_len, angle, level):
    if level > 0:
        t.forward(branch_len)
        t.left(angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.right(2 * angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.left(angle)
        t.backward(branch_len)

# Konfigurasi awal Turtle
window = turtle.Screen()
window.bgcolor("white")
my_turtle = turtle.Turtle()
my_turtle.color("black")
my_turtle.speed(0)  # Set kecepatan normal

# Atur posisi awal dan sudut
my_turtle.left(90)
my_turtle.up()
my_turtle.backward(100)
my_turtle.down()

# Gambar pohon Fibonacci dengan panggilan fungsi
fibonacci_tree(my_turtle, 100, 30, 5)

# Tutup jendela saat selesai
window.exitonclick()