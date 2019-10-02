
Coloquei os parêntes que faltavam e podiam causar problemas de contas e 
prejudicar o programa !




def calc_raiz(a,b,c):

    delta = b*b - (4*a*c)

    if (delta > 0) :
        print('A função possui duas raizes reais e distintas')
        x1= (-b + (delta**(1/2)))/(2*a)
        x2= (-b - (delta**(1/2)))/(2*a)
        print('x1 = ',x1)
        print('x2 = ',x2)
        return 0

    if(delta < 0) :
        print('A função possui duas raízes complexas e distintas')
        realx= (-b)/(2*a)
        imx= ((-delta)**(1/2))/(2*a)
        print('Re(x1) = ',realx,' Im(x1) = ',imx)
        print('Re(x2) = ',realx,' Im(x2) = ',-imx)
        return 1
    
    if(delta == 0) :

        print('A função possui uma raiz real de multiplicidade 2')
        x= (-b)/(2*a)
        print('A raiz é : ',x)
        return 0 