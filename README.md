# Machine Learning Book

Un libro virtual diseñado como recurso de aprendizaje para los estudiantes del curso de Inteligencia Artificial (INFO257) de la carrera de Ingeniería Civil en Informática de la Universidad Austral de Chile. El libro fue escrito por Pablo Huijse y está en continuo desarrollo.

El código fuente del libro está en https://github.com/phuijse/MachineLearningBook. El libro virtual está publicado en : https://phuijse.github.io/MachineLearningBook/. El libro fue desarrollado utilizando jupyter-book. Si encuentras errores por favor deja un issue en el repositorio que contiene el libro.

**Contenidos**

- Fundamentos de aprendizaje supervisado
- Regresión Lineal y logística
- Árboles de decisión y ensambles
- Selección de características
- Redes Neuronales Artificiales 
- Aprendizaje Reforzado

**Referencias**

1. [I. Goodfellow and Y. Bengio and A. Courville, "Deep Learning", MIT PRESS, 2016](http://www.deeplearningbook.org/)
1. [A. Zhang, Z.C. Lipton, M. Li, A.J. Smola, "Dive into Deep Learning"](https://www.d2l.ai/)
1. [Hastie, Tibshirani, Friedman, "Elements of Statistical Learning", Springer, 2009](http://www.web.stanford.edu/~hastie/ElemStatLearn/)
1. [V. Francois-Lavet, et al., "An Introduction to Deep Reinforcement Learning", Foundations and Trends in Machine Learning: Vol. 11, No. 3-4, 2018](https://arxiv.org/abs/1811.12560)

**Como compilar este libro**

1. Clonar el repositorio: git clone https://github.com/phuijse/PythonBook.git
1. Instalar dependencias: pip install -r requirements.txt
1. Ejecutar los cuadernillos
1. Compilar libro: jupyter-book build .
1. (Opcional) Subir a github pages: ghp-import -n -p -f _build/html/
