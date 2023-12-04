/////////// 1
<?php

$a = builder(5);
echo $a(3).PHP_EOL; // 8
echo $a(1).PHP_EOL; // 9
echo $a(4).PHP_EOL; // 13

function builder(int $in) {
    $b = $in;

    return function ($in) use (&$b) {
        $b = $b + $in;
        return $b;
    }
}

///////// 2
<?php
namespace App/Response;

declare(strict_types=1);

// Некий класс ответа на запрос из нашего фреймворка. Приведен просто для референса
class Response
{
    protected $content string;
    protected $code int;

    public function __construct(
        public string $content,
        public int $code
    ) {
       $this->content = $content;
       $this->code = $code;
    }
}

class LogController
{
    /**
     * Метод numberOfErrors возвращает в ответ json, со следующей структурой:
     * {
     *   "found_errors": <int>
     * }
     *
     * Он выполняется максимум X мс, которые мы можем задать в конфиге.
     * Он проходится по файлу log.txt и ищет там ошибки с кодом $errorCode.
     * Он возвращает количество найденных ошибок за период времени.
     *
     * На сервере для PHP процесса выделяется 250 mb памяти. Размер файла log.txt - 10gb
     * Файл расположен в корне (/log.txt), его содержимое:
     * <timestamp>;<error_code>
     */
    protected $timer;

    public function __construct(DepencyInjection $timer) {
        $this->timer = $timer;
    }

    #[Route('numberOfErrors/{errorCode}')]
    public function numberOfErrors(int $errorCode): Response
    {
        $responseContent = [];
        $responseCode = 200;
        $ticker = $this->timer(new DateTime());
        $tickerEnd = $this->timer(new DateTime()->add($this->timer->getLimit()));

        $numErrors = 0;
        $connection = fopen('/log.txt', 'a');

        if ($connection === false) {
            $responseContent = [
                "error" => 'No file'
            ];
            $responseCode = 503;
        }

        while ($line = fgets($connection) && $ticker <= $tickerEnd) {
            [$timestamp, $code] = explode($line, ";");
            if ((int)$code === $errorCode) {
                $numErrors++;
            }
        }

        $responseContent = [
            "found_errors": $numErrors
        ]

        return new Response(json_encode($responseContent), $responseCode);
    }
}

$a = []; // 1mb
$b = $a; // 1mb
$b[1] = 0; // 2mb - copy-on-write