# Machine Learning Book

Un libro sobre métodos de *Machine Learning* enfocado en su aplicación utilizando librerías del lenguaje Python. El código fuente del libro está en https://github.com/phuijse/MachineLearningBook. El libro está publicado en: https://phuijse.github.io/MachineLearningBook/. Este libro fue desarrollado utilizando [jupyter-book](https://jupyterbook.org/en/stable/intro.html). Si encuentra errores por favor deja un *issue* en el repositorio que contiene el libro. El libro fue escrito por [Pablo Huijse](https://phuijse.github.io/) y está en continuo desarrollo.

**Contenidos**

El libro incluye los siguientes temas

- Fundamentos de aprendizaje supervisado
- Regresión Lineal y logística
- Máquinas de Soporte Vectorial
- Árboles de decisión y ensambles
- Selección de características
- Redes Neuronales Artificiales 
- Aprendizaje Reforzado

A lo largo del libro encontrará ejemplos en base a las librerías [scikit-learn](https://scikit-learn.org/stable/) y [PyTorch](https://pytorch.org/)

**Referencias**

Aprendizaje supervisado:

1. [Hastie, Tibshirani, Friedman, "Elements of Statistical Learning", Springer, 2009](http://www.web.stanford.edu/~hastie/ElemStatLearn/)
1. [A. Burkov, "Machine Learning ENGINEERING", True Positive INC, 2020](http://www.mlebook.com/wiki/doku.php)

Redes Neuronales Artificiales:

1. [I. Goodfellow and Y. Bengio and A. Courville, "Deep Learning", MIT PRESS, 2016](http://www.deeplearningbook.org/)
1. [A. Zhang, Z.C. Lipton, M. Li, A.J. Smola, "Dive into Deep Learning"](https://www.d2l.ai/)

Aprendizaje Reforzado:

1. [Sutton y Barto, "Reinforcement Learning: An Introduction", MIT Press, 2nd ed, 2018](http://www.incompleteideas.net/book/the-book.html)
1. [V. Francois-Lavet, et al., "An Introduction to Deep Reinforcement Learning", Foundations and Trends in Machine Learning: Vol. 11, No. 3-4, 2018](https://arxiv.org/abs/1811.12560)
1. [D. Silver, "Reinforced Learning Course"](https://www.youtube.com/watch?v=2pWv7GOvuf0&list=PLqYmG7hTraZDM-OYHWgPebj2MfCFzFObQ)



**Dedicatoria**

Este libro fue diseñado como recurso de aprendizaje para los estudiantes del curso de Inteligencia Artificial (INFO257) de la carrera de Ingeniería Civil en Informática de la Universidad Austral de Chile. 

**Como compilar/publicar este libro**

1. Clonar el repositorio: git clone https://github.com/phuijse/MachineLearningBook.git
1. Instalar dependencias: pip install -r requirements.txt
1. Ejecutar los cuadernillos
1. Compilar con: jupyter-book build .
1. Subir a github pages: ghp-import -n -p -f _build/html/
