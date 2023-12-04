/**
 * @param array[] $commits - двумерный массив.
 * Элементы массива являются ассоциативным массивом с ключами buildTime и hash.
 * @param int $thresholdTime - пороговое время
 * @return string
 */
function FindTheBrokenOne(array $commits, int $thresholdTime): string {
    $left = 0;
    $right = count($commits) - 1;

    if ($commits[0]['buildTime'] >= $thresholdTime) {
            return $commits[0]['hash'];
        }
    if ($commits[$right]['buildTime'] < $thresholdTime) {
            return "";
        }

    while ($left <= $right) {
        $mid = floor(($left + $right) / 2);

        if ($commits[$mid]['buildTime'] == $thresholdTime && $commits[$mid-1]['buildTime'] != $commits[$mid]['buildTime']) {
            return $commits[$mid]['hash'];
        }

        if ($commits[$mid]['buildTime'] > $thresholdTime) {
            $right = $mid - 1;
        }
        else {
            $left = $mid + 1;
        }
    }

    for ($i = max([min([$left, $right, $mid]) - 1, 0]); $i <= min([max([$left, $right, $mid]) + 1, count($commits)]) ; $i++) {
        if ($commits[$i]['buildTime'] >= $thresholdTime) {
            return $commits[$i]['hash'];
        }
    }

    return "";
}