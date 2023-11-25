## Комментарий к решению

- входные аргументы переименованы
- из-за определенных ограничений (возвращаемый тип, принимаемые типы,
типы ключей в самом массиве) решение усложняется за счет многочисленных 
проверок (иначе можно было бы обойтись map/reduce)
- нет указания о единообразности типов значений по выбранному ключу, 
хотя возвращение в виде объекта приведет все ключи в строки (сольются
ключи "1" и 1, например),
а Map не соответствует условиям задачи => возможны коллизии при приведении типов
- нет указания о поведении функции в случае повторения ключа (оставлять первый объект
или перезаписывать)
- сама функция, видимо, реализует hashmap для однократной обработки большого массива 
и дальнейших быстрых проверок на наличие ключа и вытаскивания значения (первого? любого?)
по этому ключу, но выглядит со всеми примочками довольно странно
- проще было бы список уникальных ключей и значения по ключам получить через Set/Map,
избавившись и от коллизий по типу, и реализовав это очень лаконично, не уделяя большое
внимание проверкам, а уделить внимание качеству и однородности данных, чуть увеличив 
алгоритмическую сложность (сложно представить, чтобы на фронтенде это вызвало проблемы)
- учитывая вышеописанное решение получилось таким
    - комментариев нет, так код желательно понимать по самому коду
    - Map/Set не применены (и из-за условия по типу, и из-за алгоритмической сложности)
    - были идеи применения генератора, но отказался
    - изучил вопрос по скорости различных обходов массивов (остановился на reduce, не из-за скорости)  
    - изучил вопрос по четким проверкам на тип объект, вынес в отдельную функцию, чтобы упростить вид условия

## Само задание:

Напишите функцию mapArrayToHashByKey. 
Она принимает два аргумента: массив объектов array и строку key.

```
const hash = mapArrayToHashByKey(data, "id");
```

А возвращает объект со структурой:
```
{ array[0][key]: array[0],
 array[1][key]: array[2],....
_${key}s: [array[0][key], array[1][key], ... ]}
```

Пример данных на вход:

```
const data = [  {
    id: 1,    age: 25,
    address: {      city: "New York",
      zipCode: 10001,    },
    name: "John",    surname: "Doe",
  },  {
    id: 2,    age: 30,
    address: {      city: "Los Angeles",
      zipCode: 90001,    },
    name: "Jane",    surname: "Smith",
  },];
const hash = mapArrayToHashByKey(data, "age")
```

Пример результата функции:
```
{  "25": {
    id: 1,    age: 25,
    address: {      city: "New York",
      "zipCode": 10001    },
    name: "John",    surname: "Doe"
  },  "30": {
    id: 2,    age: 30,
    address: {      city: "Los Angeles",
      zipCode: 90001    },
    name: "Jane",    surname: "Smith"
  },  "_ages": [
    "25",    "30"
  ]
  }
```  

**Ограничения и гарантии:**
- гарантируется, что значения ключей объектов в массиве array (и вложенных объектов) имеют только следующие типы данных:
    - string;
    - number;
    - null;
    - undefined;
    - boolean;

Рекомендуемая временная сложность функции -- O(n).
- параметр array может принимать значения null или undefined - в этом случае выполнение функции не должно завершиться ошибкой.
- если аргумента key нет среди ключей объектов массива array - функция должна вернуть структуру вида:

``` 
{  _${key}s: []; }
``` 

## Ссылки

- https://beautifulcode.sber.ru/task/frontend
- https://habr.com/ru/companies/sberbank/articles/762796/