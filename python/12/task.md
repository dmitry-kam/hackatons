## ДИАЛОГОВОЕ ДЕРЕВО
Речь Мейв представлена в виде диалогового дерева. Где каждый путь это возможный вариант продолжения разговора. 

Вам будет дано представление дерева возможных вариантов разговора Мейв.
Ваша задача найти количество всевозможных диалогов, которые состоят из 6 узлов и более.
Корень дерева обозначается 1. 
Диалог считается законченным, если при направлении движения от корня дерева, через родительские узлы к дочерним, вы пришли к элементу, у которого нет дочерних узлов. 


Например: на картинке изображено 3 диалога с длиной пути от 6-ти узлов и более. 
```
1-3-5-8-10-12
1-3-5-13-14-15
1-3-5-13-14-16-17
```
Входные данные: 
диалоговое дерево, представленное в виде связи родительских узлов с дочерними, где сначала указан родительский узел, через двоеточие его дочерние узлы, если узла нет среди родительских, то значит у этого узла нет дочерних элементов
Пример выходных данных: 
```
1:2,3
2:6
3:4,5
4:7
5:8,13
6:9
8:10,11
10:12
13:14
14:15,16
16:17
```
Пример выходных данных: 3
Количество узлов может доходить до 100.

