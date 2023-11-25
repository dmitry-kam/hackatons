Долорес с Уильямом попали в необычное минное поле. Поле прямоугольное, поделено на меньшие клетки, мины расположены в клетках в шахматном порядке. 

```
X - изображены мины
D - местоположение Долорес
W - местоположение Уильяма
```

В пустых клетках пустое пространство. 

Мины могут ранить только Долорес, но ни Уильяма. 

Мины взрываются от Уильяма, но не от Долорес. 

Если на мину наступит Уильям, то эта мина взорвется и взорвутся все по диагонали от нее. 
В первый момент все мины целы, после чего Долорес и Уильям делают шаг, каждый в заданную им сторону, при этом Долорес может ранить, если она окажется в клетке со взываемой миной. 
На рисунках ниже, представлен пример, как взрываются мины. При этом Уильям встал на одну из мин, которая в том числе  взорвется.

z - взорванные мины
Изначально Уильям и Долорес стоят на пустом пространстве. Ваша задача найти ранит ли мина Долорес. 
Входные данные: минное поле, вместе с расположением Долорес и Уйльяма
Шаги в одном из направлений: right, left, up, down. Сначала шаг Долорес, потом Уйльяма
Шаг делается только один
Обозначения: 
```
0 - пустое пространство
X - изображены мины
D - местоположение Долорес
W - местоположение Уильяма
```
Минное поле размеров до 10 на 10
Пример входных данных: 
```
X0X0X0X0X
0X0X0X0X0
XWX0X0X0X
0X0X0X0X0
X0X0X0X0X
0X0X0X0X0
X0X0X0X0X
0X0X0X0X0
X0X0XDX0X
right
left
```
Выходные данные: Yes, если ранило, No если нет. 
