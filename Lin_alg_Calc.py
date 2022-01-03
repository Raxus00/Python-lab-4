import numpy as np
import matplotlib.pyplot as plt


def enter_vectors():
    vector=[]
    temp=[]
    while len(vector)!=3:
        vector=[]
        new_str=''
        v=str(input("enter your vector, with spaces in between the numbers:"))
        temp=v.split(' ')
        try:
            for i in temp:
                value = float(i)
                vector.append(value)
        except ValueError:
            print("Not a number")
    vector= np.array(vector)
    return vector

def display_vectors(a_vec, b_vec, res_vec, inpt):
    size=0
    start=[0,0,0]
    for i in a_vec, b_vec, res_vec:
        try:
            for j in i:
                if abs(j)>size:
                    size=abs(j)
        except:
            size=abs(i)
    fig=plt.figure()
    axis = fig.gca(projection='3d')
    axis.set_xlabel('X')
    axis.set_ylabel('Y')
    axis.set_ylabel('Z')
    axis.set_xlim(-size,size)
    axis.set_ylim(-size,size)
    axis.set_zlim(-size,size)

    if inpt==3:
        axis.set_title("Vector Addition")
        plt.quiver(*start, *a_vec, color='green')
        plt.quiver(*a_vec, *b_vec, color='red')
        plt.quiver(*start, *res_vec ,color='blue')    
    
    elif inpt ==4:
        axis.set_title("Vector Subtraction")
        plt.quiver(*start, *a_vec, color='green')
        plt.quiver(*start, *b_vec, color='red')
        plt.quiver(*b_vec, *res_vec, color='blue')
    
    elif inpt==5:
        axis.set_title("Multiplication with a scalar")
        plt.quiver(*start, *a_vec, color='red')
        plt.quiver(*start, *res_vec, color='green')
    
    elif inpt == 7:
        axis.set_title("Vector product")
        plt.quiver(*start, *a_vec, color='green')
        plt.quiver(*start, *b_vec, color='red')
        plt.quiver(*start, * res_vec, color='Blue')
    
    fig.show()
    save=input("Do you want to save the picture? j/n:")
    if save=='j' or save=='J':
        fig.savefig(input("filename:"))
    plt.close(fig)
    
def add_vectors(a_vec, b_vec):
    new_vector=[]
    if len(a_vec) ==0 or len(b_vec)==0:
        print("You are missing at least one vector")
        return 
    else:
        new_vector=np.add(a_vec, b_vec)
        print(f"{a_vec} + {b_vec} = {new_vector}")
        display_vectors(a_vec, b_vec, new_vector, 3)
    return new_vector

def subtract_vectors(a_vec, b_vec):
    new_vector=[]
    if len(a_vec)==0 or len(b_vec)==0:
        print("you are missing at least one vector")
    else:
        new_vector= np.subtract(a_vec, b_vec)
        print(f"{a_vec} - {b_vec} = {new_vector}")
        display_vectors(a_vec, b_vec, new_vector, 4)
    return new_vector

def scalar_multiplication(a_vec):
    new_vector=[]
    if len(a_vec)==0:
        print("Vector a is missing values")
    scalar=input("Enter a scalar:")
    try:
        scalar=float(scalar)
        new_vector = a_vec * scalar
        
    except ValueError:
        print("Not a number")
    print(f"{a_vec} * {scalar} = {new_vector}")
    display_vectors(a_vec, scalar, new_vector, 5)
    return new_vector

def scalar_product(a_vec, b_vec):
    if len(a_vec)==0 or len(b_vec)==0:
        print("At leasat one vector is missing values")
        return -1
    else:
        product=np.dot(a_vec, b_vec)
        return product

def vector_product(a_vec, b_vec):
    new_vector=[]
    if len(a_vec)==0 or len(b_vec)==0:
        print("At least one of the vector is missing values")
    else:
        new_vector = np.cross(a_vec, b_vec)
        display_vectors(a_vec, b_vec, new_vector, 7)
    return new_vector

def enter_plane():
    plane=[]
    while len(plane)!=4:
        plane=[]
        temp=[]
        print("The equation för a plan is a*x + b*y +c*z +d = 0")
        choice=input("enter your choices for a b c d:")
        temp=choice.split(' ')
        try:
            for i in temp:
                value=float(i)
                plane.append(value)
        except ValueError:
            print("Not a number")
    plane=np.array(plane)
    return plane

def display_plane(plane):
    a, b, c, d = plane[0],plane[1], plane[2], plane[3]
    size=0
    for i in a,b,c,d:
        if i > size:
            size=int(i)
    if a ==0:
        if b==0:
            if c==0:
                    print('\n' "all constents are zero can not display a plane")
                    return -1
            else:
                x, y = np.meshgrid(range((size)), range((size)))
                z=-(a*x+b*y+d)/c
        else:
            x, z = np.meshgrid(range((size)), range((size)))
            y=-(a*x+c*z+d)/b
            
    else:
        y, z = np.meshgrid(range((size)), range((size)))

        x=-(b*y+c*z+d)/a
        
    fig=plt.figure()
    axes = fig.gca(projection='3d')
    axes.plot_surface(x,y,z)
    plt.show()
    save=input("Do you want to save your plot? (j/n)")
    if save =='j'  or save=='J':
        fig.savefig(input("filnamn:"))
    else:
        print("Invalid input plot was not saved")
    plt.close(fig)

def menu():
    condition=0
    a_vec=[]
    b_vec=[]
    p=[]
    while condition==0:
        print( '\n' "1. Input vector a" '\n' "2. Input vector b" '\n' "3. Calculate a+b" '\n' "4. Calculate a-b" '\n' "5. Multiplay a with a scalar" '\n' "6. Calculate the scalar product between a and b" '\n' "7. Calculate the vector product between a and b" '\n' "8. input a palne p" '\n' "9. Show the plane p" '\n' "0. Terminate program")
        choice=input("Select what you want to do:")
        if choice =='1':
            a_vec=enter_vectors()
            print(f"Vector a is {a_vec}")

        elif choice=='2':
            b_vec=enter_vectors()
            print(f"Vector b is {b_vec}")
        
        elif choice=='3': 
            added_vector=add_vectors(a_vec, b_vec)
            if len(added_vector) != 0:
                save=input("Do you want to save this to vector a or b, other inuts will see it deleted:")
                if save== 'a' or save=='A':
                    a_vec=added_vector
                    print(f"a is now{a_vec}")
                elif save=='b' or save=='B':
                    b_vec=added_vector
                    print(f"b is now{b_vec}")
       
        elif choice=='4':
            subtracted_vector = subtract_vectors(a_vec, b_vec)
            if len(subtracted_vector) !=0:
                save=input("Do you want to save this to vector a or b, other inuts will see it deleted:")
                if save== 'a' or save=='A':
                    a_vec=subtracted_vector
                    print(f"a is now{a_vec}")
                elif save=='b' or save=='B':
                    b_vec=subtracted_vector
                    print(f"b is now{b_vec}")
       
        elif choice =='5':
            scalar_vector=scalar_multiplication(a_vec)
            if len(scalar_vector) != 0:
                save=input("Do you want to save this to vector a or b, other inuts will see it deleted:")
                if save=='a' or save=='A':
                    a_vec=scalar_vector
                    print(f"a is now{a_vec}")
                elif save=='b' or save=='B':
                    b_vec=scalar_vector
                    print(f"b is now{b_vec}")
       
        elif choice=='6':
            sp=scalar_product(a_vec, b_vec)
            if sp !=-1: 
                print(f"The scalar product of {a_vec} and {b_vec} is {sp}")
        
        elif choice=='7':
            vp=vector_product(a_vec,b_vec)
            if len(vp) != 0:
                print(f"The vector product between {a_vec} and {b_vec} is {vp}")
                save=input("Do you want to save this vector to a or b, other inputs will see it deleted")
                if save =='a' or save=='A':
                    a_vec=vp
                if save == 'b' or save=='B':
                    b_vec=vp
       
        elif choice =='8':
            p=enter_plane()
            print(f"{p[0]}*x + {p[1]}*y + {p[2]}*z + {p[3]} = 0")
       
        elif choice == '9':
            if len(p) ==0:
                print("No plane exists")
            else:
                display_plane(p)
       
        elif choice== '0':
            condition+=1
        else:
            print("Not a valid input")
menu()