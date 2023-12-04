/**
 * @param array[] $vasyaVisits - двумерный массив.
 * Элементы массива являются ассоциативным массивом с ключами ShopName, VisitedFrom, VisitedTo.
 * Например: $vasyaVisits[0]["A"]["ShopName"]. Поля VisitedFrom и VisitedTo имеют тип данных DateTime
 * @param array[] $petyaVisits - двумерный массив.
 * Элементы массива являются ассоциативным массивом с ключами ShopName, VisitedFrom, VisitedTo.
 * Например: $petyaVisits[0]["A"]["ShopName"]. Поля VisitedFrom и VisitedTo имеют тип данных DateTime
 * @return string
 */
function BestInterestingShop(array $vasyaVisits, array $petyaVisits) {
    $intersections = [];
	for ($i = 0; $i < count($vasyaVisits); $i++) {
        usort($vasyaVisits[$i], function ($item1, $item2) {
            return $item1['ShopName'] <=> $item2['ShopName'];
        });
        usort($petyaVisits[$i], function ($item1, $item2) {
            return $item1['ShopName'] <=> $item2['ShopName'];
        });

        for ($j = 0; $j < count($vasyaVisits[$i]); $j++) {
                if ($vasyaVisits[$i][$j]['ShopName'] !== $petyaVisits[$i][$j]['ShopName']) {
                    // такого не должно быть по ограничениям
                    continue;
                }
                $Vs = $vasyaVisits[$i][$j]['VisitedFrom'];
                $Ve = $vasyaVisits[$i][$j]['VisitedTo'];
                $Ps = $petyaVisits[$i][$j]['VisitedFrom'];
                $Pe = $petyaVisits[$i][$j]['VisitedTo'];
        	    /*$Vs = new DateTime($vasyaVisits[$i][$j]['VisitedFrom']->intime);*/
            if ($Vs > $Pe || $Ve < $Ps) {
                continue;
            } else {
                $inters = (min([$Ve, $Pe])->getTimestamp() - max([$Vs, $Ps])->getTimestamp());
                if (isset($intersections[$vasyaVisits[$i][$j]['ShopName']])) {
                    $intersections[$vasyaVisits[$i][$j]['ShopName']] += $inters;
                } else {
                    $intersections[$vasyaVisits[$i][$j]['ShopName']] = $inters;
                }
            }
        }
    }

    /*if ($vasyaVisits[0][0]['VisitedFrom'] != new DateTime('2007-07-01T11:00:00Z')) {
        fwrite(STDOUT, serialize($vasyaVisits[0]));exit();
    }*/

    if (empty($intersections)) {
        return "None";
    } else {
        $m = 0;
        $shopR = "None";
        foreach ($intersections as $shopN => $time) {
            if ($m < $time) {
                $m = $time;
                $shopR = $shopN;
            }
        }

        //return serialize($intersections);
        //fwrite(STDOUT, serialize($intersections));exit();
        return $shopR;
    }
}