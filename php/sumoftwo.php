<?php
// https://www.algoexpert.io/questions/Two%20Number%20Sum

/* 
First version
A loop within a loop, not ideal
*/
function sumOfTwo($array, $target){
    $len = count($array);
    $result = [];
    for($i = 0; $i < $len; $i++){
        for($j = $i+1; $j < $len; $j++){
            if($array[$i] + $array[$j] == $target){
                $result = [$array[$i], $array[$j]];
                var_dump($result);
                return $result;
            }
        }
    }
    return $result;
}
$array1 = [3, 5, -4, 8, 11, 1, -1, 6];
$target1 = 10;
sumOfTwo($array1, $target1);
$array2 = [4, 6, 1, -3];
$target2 = 3;
sumOfTwo($array2, $target2);
?>