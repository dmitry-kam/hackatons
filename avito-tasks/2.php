<?php
/*

Мы хотим складывать очень большие числа, которые превышают емкость базовых типов, поэтому мы храним их в виде массива неотрицательных чисел.
Нужно написать функцию, которая примет на вход два таких массива, вычислит сумму чисел, представленных массивами, и вернет результат в виде такого же массива.

# Пример 1
# ввод
arr1 = [1, 2, 3] # число 123
arr2 = [4, 5, 6] # число 456
# вывод
res = [5, 7, 9] # число 579. Допустим ответ с первым незначимым нулем [0, 5, 7, 9]

# Пример 2
# ввод
arr1 = [5, 4, 4] # число 544
arr2 = [4, 5, 6] # число 456
# вывод
res = [1, 0, 0, 0] # число 1000

*/

function sumArrays($arr1, $arr2) {
    $length1 = count($arr1);
    $length2 = count($arr2);
    $canonicalLength = max($length1, $length2);

    // array_fill(int $start_index, int $count, mixed $value): array
    if ($length1 < $length2) {
        //[0, 0 , 0]
        $arr1 = array_fill(0, $length2 - $length1, 0) + $arr1;
    } elseif ($length1 > $length2) {
        //[0, 0 , 0]
        $arr2 = array_fill(0, $length1 - $length2, 0) + $arr2;
    }
    // [1, 0] -> [0, 1, 0]
    //[5, 4, 4]
    //arr1 = [5, 4, 4] # число 544
    //arr2 = [4, 5, 6] # число 456
    $order = 0;
    $resultArray = [];

    for ($i = $canonicalLength; $i >= 0; $i--) {
        if (($arr1[$i] + $arr2[$i] + $order) >= 10) {
             array_push($resultArray, ($arr1[$i] + $arr2[$i] + $order)%10);
             $order = 1;
        } else {
            array_push($resultArray, $arr1[$i] + $arr2[$i] + $order);
            $order = 0;
        }
        if ($i == 0 && $order == 1) {
            array_push($resultArray, 1);
        }
    }
    return array_reverse($resultArray);
}

/*

Дан массив целых чисел nums и целое число k. Нужно написать функцию, которая вынимает из массива nums k наиболее часто встречающихся элементов.

Пример
# ввод
nums = [1,1,1,2,2,3]
k = 2
# вывод (в любом порядке)
[1, 2]

*/


function getElements($arr1, $k) {
    $arrayByQty = [];
    for ($i = 0; $i < count($arr1); $i+) {
        if (isset($arrayByQty[$arr1[$i]])) {
            $arrayByQty[$arr1[$i]]++;
        } else {
            $arrayByQty[$arr1[$i]] = 1;
        }
    }
    // asort(array &$array, int $flags = SORT_REGULAR): true
    asort($arrayByQty); //ASC

    // n + n log n + C + n -> n log n

    return array_slice(
        array_keys($arrayByQty), count($arrayByQty) - $k,  count($arrayByQty) - 1
    );
}

