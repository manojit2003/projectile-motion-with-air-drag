{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e9e2c4da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div id=\"glowscript\" class=\"glowscript\"></div>"
      ],
      "text/plain": [
       "<IPython.core.display.HTML object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/javascript": [
       "if (typeof Jupyter !== \"undefined\") { window.__context = { glowscript_container: $(\"#glowscript\").removeAttr(\"id\")};}else{ element.textContent = ' ';}"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from vpython import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "7d0465f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "finalpossition= <-0.74686, 0.231085, 0> m\n",
      "Time= 1.0300000000000007 s\n"
     ]
    }
   ],
   "source": [
    "g=vector(0,-9.8,0)\n",
    "R=0.06\n",
    "M=0.01\n",
    "rho=1.2\n",
    "A=pi*R**2\n",
    "C=0.47\n",
    "\n",
    "v0=10\n",
    "theta=pi/5\n",
    "\n",
    "ground=box(pos=vec(0,0,0), size=vector(10,0.5,2),color=color.green)\n",
    "ball=sphere(pos=vector(-4.5,1,0),radius=2*R, make_trail=True)\n",
    "\n",
    "ball.m=M\n",
    "ball.p=ball.m*v0*vector(cos(theta),sin(theta),0)\n",
    "\n",
    "t=0\n",
    "dt=0.01\n",
    "while ball.pos.y>0.25:\n",
    "    rate(100)\n",
    "    ball.v=ball.p/ball.m\n",
    "    F=ball.m*g-0.5*rho*A*C*mag(ball.v)**2*norm(ball.v)\n",
    "    ball.p+=F*dt\n",
    "    ball.pos+=ball.p*dt/ball.m\n",
    "    t+=dt\n",
    "    \n",
    "print(\"finalpossition=\",ball.pos,\"m\")\n",
    "print(\"Time=\",t,\"s\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25187702",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
