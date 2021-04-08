'''
安装 pyopengl

pip 默认安装的是32位版本的pyopengl，而我的操作系统是64位的。建议点击 https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl 下载适合自己的版本，直接安装.whl文件。我是这样安装的：

我下载的 PyOpenGL-3.1.5-cp37-cp37m-win_amd64.whl
放到 D:\pyj\st\study>  目录下

因为我 在该虚拟环境下 安装

(venv) D:\pyj\st\study>pip install PyOpenGL-3.1.5-cp37-cp37m-win_amd64.whl


教程 https://blog.csdn.net/xufive/article/details/86565130

'''
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
 
#  示例1 水壶
def 水壶():

    def Draw():
        glClear(GL_COLOR_BUFFER_BIT)
        glRotatef(0.5, 0, 1, 0)
        glutWireTeapot(0.5)
        glFlush()
    
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowSize(400, 400)
    glutCreateWindow("test")
    glutDisplayFunc(Draw)
    glutIdleFunc(Draw)
    glutMainLoop() 

# 水壶()

# 示例2 实现点线面的绘制工作

def 点线面的绘制():
    def init():
        glClearColor(0.0, 0.0, 0.0, 1.0)
        gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    
    def drawFunc():
        glClear(GL_COLOR_BUFFER_BIT)
    
        glBegin(GL_LINES)
        glVertex2f(-1.0, 0.0)
        glVertex2f(1.0, 0.0)
        glVertex2f(0.0, 1.0)
        glVertex2f(0.0, -1.0)
        glEnd()
    
        glPointSize(5.0)
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.0, 0.0)
        glVertex2f(0.3, 0.3)
        glColor3f(0.0, 1.0, 0.0)
        glVertex2f(0.6, 0.6)
        glColor3f(0.0, 0.0, 1.0)
        glVertex2f(0.9, 0.9)
        glEnd()
    
        glColor3f(1.0, 1.0, 0)
        glBegin(GL_QUADS)
        glVertex2f(-0.2, 0.2)
        glVertex2f(-0.2, 0.5)
        glVertex2f(-0.5, 0.5)
        glVertex2f(-0.5, 0.2)
        glEnd()
    
        glColor3f(0.0, 1.0, 1.0)
        glPolygonMode(GL_FRONT, GL_LINE)
        glPolygonMode(GL_BACK, GL_FILL)
        glBegin(GL_POLYGON)
        glVertex2f(-0.5, -0.1)
        glVertex2f(-0.8, -0.3)
        glVertex2f(-0.8, -0.6)
        glVertex2f(-0.5, -0.8)
        glVertex2f(-0.2, -0.6)
        glVertex2f(-0.2, -0.3)
        glEnd()
    
        glPolygonMode(GL_FRONT, GL_FILL)
        glPolygonMode(GL_BACK, GL_LINE)
        glBegin(GL_POLYGON)
        glVertex2f(0.5, -0.1)
        glVertex2f(0.2, -0.3)
        glVertex2f(0.2, -0.6)
        glVertex2f(0.5, -0.8)
        glVertex2f(0.8, -0.6)
        glVertex2f(0.8, -0.3)
        glEnd()
    
        glFlush()
    
    glutInit()
    glutInitDisplayMode(GLUT_RGBA|GLUT_SINGLE)
    glutInitWindowSize(400, 400)
    glutCreateWindow("Sencond")
    
    glutDisplayFunc(drawFunc)
    init()
    glutMainLoop()

# 点线面的绘制()

# 示例3 实现对y=x^3的函数曲线

def 函数曲线():
    def init():
        #初始化背景
        glClearColor(1.0, 0.0, 1.0, 1.0)
        gluOrtho2D(-5.0, 5.0, -5.0, 5.0)
    
    def plotfunc():
        glClear(GL_COLOR_BUFFER_BIT)
        glPointSize(5.0)

        #绘制坐标系
        glColor3f(1.0, 1.0, 0.0)
        glBegin(GL_LINES) #画线
        glVertex2f(-5.0, 0.0)
        glVertex2f(5.0, 0.0)
        glVertex2f(0.0, 5.0)
        glVertex2f(0.0, -5.0)
        glEnd()
    
        #绘制y = x*x*x (-5.0 < x < 5.0) 的图像
        glColor3f(0.0, 0.0, 0.0)
        glBegin(GL_LINES)#画线
        #for x in arange(-5.0, 5.0, 0.1):
        for x in (i * 0.1 for i in range(-50, 50)):
            y = x * x * x
            glVertex2f(x, y) #绘制每个0.1个步长的点
        glEnd()
    
        glFlush()
    
    def main():
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
        glutInitWindowPosition(50,50)
        glutInitWindowSize(400,400)
        glutCreateWindow("Function Plotter")
        glutDisplayFunc(plotfunc)
        init()
        glutMainLoop()
    
    main()

# 函数曲线()